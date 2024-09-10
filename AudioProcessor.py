import sys

from scipy.io import wavfile
import numpy as np


class AudioProcessor:

    # constructor
    def __init__(self, messageEncoder, frame_length=1024):
        self.frame_length = frame_length
        self.messageEncoder = messageEncoder

    def encode(self, audio_path, encrypted_message, stego_audio_path):
        try:
            sample_rate, audio = wavfile.read(audio_path)

            if len(audio.shape) > 1:
                audio = audio[:, 0]

            # splits the encrypted message to ASCII numbers
            # and converts the numbers to binary.
            message_bits = self.messageEncoder.text_to_bits(encrypted_message)
            message_length = len(message_bits)

            if message_length > self.frame_length // 2 - 32:
                raise ValueError("Message is too long to be encoded in the audio file.")

            frames = audio[:self.frame_length].astype(np.float32)
            fft_frames = np.fft.fft(frames)
            magnitudes = np.abs(fft_frames)
            phases = np.angle(fft_frames)

            # Encode message length
            length_bits = format(message_length, '032b')
            for i, bit in enumerate(length_bits):
                phases[i] = 0 if bit == '0' else np.pi

            # Encode message
            for i, bit in enumerate(message_bits):
                if i + 32 < self.frame_length // 2:
                    phases[i + 32] = 0 if bit == '0' else np.pi

            encoded_fft = magnitudes * np.exp(1j * phases)
            encoded_frame = np.fft.ifft(encoded_fft).real

            encoded_audio = np.concatenate((encoded_frame, audio[self.frame_length:]))
            encoded_audio = np.float64(encoded_audio / np.max(np.abs(encoded_audio)) * 32767)

            # Denormalize the encoded audio data
            max_abs_value = np.max(np.abs(audio))
            encoded_audio = np.int32(encoded_audio * max_abs_value)  # a very critical point

            # save file to disk using the output path
            wavfile.write(stego_audio_path, sample_rate, encoded_audio)
            print(f"Message was successfully encoded in the specified audio file.")

        except Exception as e:
            print(f"Error during encoding: {str(e)}", file=sys.stderr)
            sys.exit(1)

    def decode(self, audio_path, password):
        try:
            sample_rate, audio = wavfile.read(audio_path)
        except Exception as e:
            print(f"Error during decoding: {str(e)}", file=sys.stderr)
            sys.exit(1)
