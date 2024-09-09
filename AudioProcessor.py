import sys

import wavfile


class AudioProcessor:

    def __init__(self, frame_length):
        # constructor
        self.frame_length = frame_length

    def encode(self, audio_path, encrypted_message, stego_audio_path):
        try:
            sample_rate, audio = wavfile.read(audio_path)
        except Exception as e:
            print(f"Error during encoding: {str(e)}", file=sys.stderr)
            sys.exit(1)

    def decode(self, audio_path, password):
        try:
            sample_rate, audio = wavfile.read(audio_path)
        except Exception as e:
            print(f"Error during decoding: {str(e)}", file=sys.stderr)
            sys.exit(1)
