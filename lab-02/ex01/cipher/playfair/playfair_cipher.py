class PlayfairCipher:
    def __init__(self):
        pass
    
    def create_matrix(self, key):
        key = key.upper().replace("J", "I")
        unique_key = []
        for char in key:
            if char not in unique_key and char.isalpha():
                unique_key.append(char)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix_flat = unique_key.copy()
        
        for char in alphabet:
            if char not in matrix_flat:
                matrix_flat.append(char)
                
        playfair_matrix = [matrix_flat[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1
                      
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.upper().replace("J", "I")
        
        formatted_text = ""
        i = 0
        while i < len(plain_text):
            formatted_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    formatted_text += "X"
                else:
                    formatted_text += plain_text[i+1]
                    i += 1
            i += 1
            
        if len(formatted_text) % 2 != 0:
            formatted_text += "X"
            
        encrypted_text = ""
        for i in range(0, len(formatted_text), 2):
            pair = formatted_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        if decrypted_text.endswith("X"):
            decrypted_text = decrypted_text[:-1]
            
        return decrypted_text