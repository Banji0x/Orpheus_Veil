class MessageEncoder:

    def text_to_bits(self, text):
        return ''.join(format(ord(char), '08b') for char in text)

    def bits_to_text(self, bits):
        return ''.join(chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8))