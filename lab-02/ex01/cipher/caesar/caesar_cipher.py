from cipher.caesar import ALPHABET

class CaesarCipher:
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(ALPHABET)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = ALPHABET.index(letter)
            output_index = (letter_index + key) % alphabet_len
            encrypted_text.append(ALPHABET[output_index])
            
        return "".join(encrypted_text)
    
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(ALPHABET)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = ALPHABET.index(letter)
            output_index = (letter_index - key) % alphabet_len
            decrypted_text.append(ALPHABET[output_index])     
        return "".join(decrypted_text)