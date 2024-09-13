# OrpheusVeil: Audio Steganography Tool with AES Encryption

## Overview

OrpheusVeil is a powerful and user-friendly audio steganography tool that combines the art of hiding messages in audio files with the security of AES encryption. Named after Orpheus, the legendary musician of Greek mythology, this tool allows you to conceal your secrets within the harmony of sound.

## Features

- **Message Hiding**: Embed secret messages within audio files.
- **AES Encryption**: Secure your hidden messages with state-of-the-art AES encryption.
- **Message Extraction**: Easily retrieve hidden messages from steganographic audio files.
- **Customizable Frame Length**: Advanced users can adjust the frame length for encoding.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Banji0x/Orpheus_Veil.git/
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

OrpheusVeil provides two main functionalities: encoding (hiding) messages and decoding (revealing) messages.

### Encoding a Message

To hide a message in an audio file:

```
python OrpheusVeil.py encode input_audio.wav your_secret_key -m "Your secret message" -o output_audio.wav
```

Optional: Specify a custom frame length (default is 1024):
```
python OrpheusVeil.py encode input_audio.wav your_secret_key -m "Your secret message" -o output_audio.wav -f 2048
```

### Decoding a Message

To reveal a hidden message from an audio file:

```
python OrpheusVeil.py decode stego_audio.wav your_secret_key
```

## Parameters

- `action`: Choose between 'encode' or 'decode'.
- `input_file`: The input audio file (for encoding) or the stego audio file (for decoding).
- `secret_key`: Your secret key for encryption/decryption.
- `-m, --message`: The secret message you want to hide (required for encoding).
- `-o, --output`: The output audio file name (required for encoding).
- `-f, --frame_length`: Optional frame length (default: 1024).

## Security Considerations

- Keep your secret key safe. Anyone with the key can decode your hidden messages.
- The security of your hidden message relies on both the steganography technique and the encryption. Treat the output audio file as sensitive information.
- While OrpheusVeil uses encryption, it's always wise to avoid hiding extremely sensitive information in audio files.

## Contributing

Contributions to OrpheusVeil are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and ethical use only. The authors are not responsible for any misuse or illegal activities conducted with this software.