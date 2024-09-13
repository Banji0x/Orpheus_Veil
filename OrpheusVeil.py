import sys
import argparse
from AudioProcessor import AudioProcessor
from Encryptor import Encryptor
from MessageEncoder import MessageEncoder


class OrpheusVeil:
    def __init__(self, frame_length=1024):
        self.audio_processor = AudioProcessor(MessageEncoder(), frame_length)
        self.encryptor = Encryptor()

    def encrypt_encode(self, input_audio, message, output_stego_audio_path, secret_key):
        print(f"Encrypting and encoding message into {input_audio}...")
        encrypted_message = self.encryptor.encrypt(message, secret_key)
        self.audio_processor.encode(input_audio, encrypted_message, output_stego_audio_path)
        print(f"Message successfully hidden in {output_stego_audio_path}")

    def decode_decrypt(self, stego_audio_path, secret_key):
        print(f"Decoding and decrypting message from {stego_audio_path}...")
        decoded_text = self.audio_processor.decode(stego_audio_path)
        decrypted_text = self.encryptor.decrypt(decoded_text, secret_key)
        print("Message successfully revealed")
        return decrypted_text


def main():
    parser = argparse.ArgumentParser(description="OrpheusVeil: Audio steganography tool with AES Encryption.")
    parser.add_argument('action', choices=['encode', 'decode'], help="Action to perform")
    parser.add_argument('input_file', help="Input audio file for encoding or stego audio file for decoding")
    parser.add_argument('secret_key', help="Secret key for encryption/decryption")
    parser.add_argument('-m', '--message', help="Message to encode (required for encoding)")
    parser.add_argument('-o', '--output', help="Output audio file (required for encoding)")
    parser.add_argument('-f', '--frame_length', type=int, default=1024, help="Frame length (optional, default: 1024)")

    args = parser.parse_args()
    orpheus_veil = OrpheusVeil(args.frame_length)

    if args.action == "encode":
        if not args.message or not args.output:
            print("Error: Encoding requires both message and output file.", file=sys.stderr)
            print("\nExample usage for encoding:")
            print("python OrpheusVeil.py encode input_audio.wav my_secret_key -m \"Hello, world!\" -o output_audio.wav")
            parser.print_help()
            sys.exit(2)
        orpheus_veil.encrypt_encode(args.input_file, args.message, args.output, args.secret_key)
        print(f"\nEncoding complete. Your message has been hidden in {args.output}")
        print("To decode this message, use:")
        print(f"python OrpheusVeil.py decode {args.output} my_secret_key")

    elif args.action == "decode":
        decrypted_text = orpheus_veil.decode_decrypt(args.input_file, args.secret_key)
        print(f"Decoded message: {decrypted_text}")
        print("\nTo hide a new message, use:")
        print("python OrpheusVeil.py encode input_audio.wav my_secret_key -m \"Your secret message\" -o new_output.wav")

    else:
        print("Invalid action. Use 'encode' or 'decode'.", file=sys.stderr)
        print("\nExample usage:")
        print(
            "For encoding: python OrpheusVeil.py encode input_audio.wav my_secret_key -m \"Hello, world!\" -o "
            "output_audio.wav")
        print("For decoding: python OrpheusVeil.py decode output_audio.wav my_secret_key")
        parser.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
