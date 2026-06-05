from flask import Flask, render_template, request
from ex01.cipher.caesar import CaesarCipher
from ex01.cipher.playfair import PlayfairCipher 
from ex01.cipher.railfence import RailfenceCipher 
from ex01.cipher.vigenere import VigenereCipher 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# ==========================================
# 1. CAESAR CIPHER
# ==========================================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText'].upper().replace(" ", "")
    key = int(request.form['inputKeyPlain'])
    
    if key < 1 or key > 25:
        return "<h3 style='color:red;'>LỖI: Khóa Caesar bắt buộc phải từ 1 đến 25!</h3><a href='/caesar'>Quay lại</a>"
        
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"<h3 style='color: #0a4275;'>Kết quả Mã hóa Caesar</h3><b>Text:</b> {text}<br/><b>Key:</b> {key}<br/><b>Encrypted text:</b> <span style='color: #00b894; font-size: 1.2rem; font-weight: bold;'>{encrypted_text}</span><br/><br/><a href='/caesar'>Quay lại</a>"

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText'].upper().replace(" ", "")
    key = int(request.form['inputKeyPlain'])
    
    if key < 1 or key > 25:
        return "<h3 style='color:red;'>LỖI: Khóa Caesar bắt buộc phải từ 1 đến 25!</h3><a href='/caesar'>Quay lại</a>"
        
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"<h3 style='color: #0a4275;'>Kết quả Giải mã Caesar</h3><b>Cipher text:</b> {text}<br/><b>Key:</b> {key}<br/><b>Decrypted text:</b> <span style='color: #d63031; font-size: 1.2rem; font-weight: bold;'>{decrypted_text}</span><br/><br/><a href='/caesar'>Quay lại</a>"

# ==========================================
# 2. PLAYFAIR CIPHER
# ==========================================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText'].upper().replace(" ", "")
    key = request.form['inputKeyPlain'].upper().replace(" ", "") 
    
    if not text.isalpha() or not key.isalpha():
        return "<h3 style='color:red;'>LỖI: Playfair chỉ chấp nhận chữ cái A-Z!</h3><a href='/playfair'>Quay lại</a>"
    if len(key) > 25:
        return "<h3 style='color:red;'>LỖI: Khóa Playfair không được vượt quá 25 ký tự!</h3><a href='/playfair'>Quay lại</a>"

    Playfair = PlayfairCipher()
    matrix = Playfair.create_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    
    matrix_html = "<br/><br/><b style='font-size: 18px; color: #0a4275;'>Ma trận Playfair 5x5 sinh ra từ khóa:</b><br/>"
    matrix_html += "<table style='border-collapse: collapse; text-align: center; margin-top: 15px; font-family: monospace; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>"
    for row in matrix:
        matrix_html += "<tr>"
        for char in row:
            matrix_html += f"<td style='width: 60px; height: 60px; border: 2px solid #2c3e50; font-size: 26px; font-weight: bold; color: #0a4275;'>{char}</td>"
        matrix_html += "</tr>"
    matrix_html += "</table><br/><a href='/playfair'>Quay lại</a>"

    return f"<h3 style='color: #0a4275;'>Kết quả Mã hóa Playfair</h3><b>Text:</b> {text}<br/><b>Key:</b> {key}<br/><b>Encrypted text:</b> <span style='color: #00b894; font-size: 1.2rem; font-weight: bold;'>{encrypted_text}</span>" + matrix_html

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText'].upper().replace(" ", "")
    key = request.form['inputKeyPlain'].upper().replace(" ", "")
    
    if not text.isalpha() or not key.isalpha():
        return "<h3 style='color:red;'>LỖI: Playfair chỉ chấp nhận chữ cái A-Z!</h3><a href='/playfair'>Quay lại</a>"
    if len(key) > 25:
        return "<h3 style='color:red;'>LỖI: Khóa Playfair không được vượt quá 25 ký tự!</h3><a href='/playfair'>Quay lại</a>"

    Playfair = PlayfairCipher()
    matrix = Playfair.create_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    
    matrix_html = "<br/><br/><b style='font-size: 18px; color: #0a4275;'>Ma trận Playfair 5x5 sinh ra từ khóa:</b><br/>"
    matrix_html += "<table style='border-collapse: collapse; text-align: center; margin-top: 15px; font-family: monospace; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>"
    for row in matrix:
        matrix_html += "<tr>"
        for char in row:
            matrix_html += f"<td style='width: 60px; height: 60px; border: 2px solid #2c3e50; font-size: 26px; font-weight: bold; color: #0a4275;'>{char}</td>"
        matrix_html += "</tr>"
    matrix_html += "</table><br/><a href='/playfair'>Quay lại</a>"

    return f"<h3 style='color: #0a4275;'>Kết quả Giải mã Playfair</h3><b>Cipher text:</b> {text}<br/><b>Key:</b> {key}<br/><b>Decrypted text:</b> <span style='color: #d63031; font-size: 1.2rem; font-weight: bold;'>{decrypted_text}</span>" + matrix_html

# ==========================================
# 3. RAILFENCE CIPHER
# ==========================================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText'].replace(" ", "")
    key = int(request.form['inputKeyPlain']) 
    
    if key < 2:
        return "<h3 style='color:red;'>LỖI: Số hàng rào phải từ 2 trở lên!</h3><a href='/railfence'>Quay lại</a>"
    if key >= len(text):
        return f"<h3 style='color:red;'>LỖI: Số hàng rào ({key}) không được lớn hơn hoặc bằng độ dài bản rõ ({len(text)} ký tự)!</h3><a href='/railfence'>Quay lại</a>"

    Railfence = RailfenceCipher()
    encrypted_text = Railfence.rail_fence_encrypt(text, key)
    return f"<h3 style='color: #0a4275;'>Kết quả Mã hóa Railfence</h3><b>Text:</b> {text}<br/><b>Key (Rails):</b> {key}<br/><b>Encrypted text:</b> <span style='color: #00b894; font-size: 1.2rem; font-weight: bold;'>{encrypted_text}</span><br/><br/><a href='/railfence'>Quay lại</a>"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText'].replace(" ", "")
    key = int(request.form['inputKeyPlain'])
    
    if key < 2:
        return "<h3 style='color:red;'>LỖI: Số hàng rào phải từ 2 trở lên!</h3><a href='/railfence'>Quay lại</a>"
    if key >= len(text):
        return f"<h3 style='color:red;'>LỖI: Số hàng rào ({key}) không được lớn hơn hoặc bằng độ dài bản mã ({len(text)} ký tự)!</h3><a href='/railfence'>Quay lại</a>"

    Railfence = RailfenceCipher()
    decrypted_text = Railfence.rail_fence_decrypt(text, key)
    return f"<h3 style='color: #0a4275;'>Kết quả Giải mã Railfence</h3><b>Cipher text:</b> {text}<br/><b>Key (Rails):</b> {key}<br/><b>Decrypted text:</b> <span style='color: #d63031; font-size: 1.2rem; font-weight: bold;'>{decrypted_text}</span><br/><br/><a href='/railfence'>Quay lại</a>"

# ==========================================
# 4. VIGENÈRE CIPHER
# ==========================================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText'].upper().replace(" ", "")
    key = request.form['inputKeyPlain'].upper().replace(" ", "") 
    
    if not text.isalpha() or not key.isalpha():
        return "<h3 style='color:red;'>LỖI: Vigenère chỉ chấp nhận chữ cái A-Z!</h3><a href='/vigenere'>Quay lại</a>"
    if len(key) > len(text):
        return f"<h3 style='color:red;'>LỖI: Độ dài khóa ({len(key)}) không được vượt quá độ dài bản rõ ({len(text)})!</h3><a href='/vigenere'>Quay lại</a>"

    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.encrypt_text(text, key)
    return f"<h3 style='color: #0a4275;'>Kết quả Mã hóa Vigenère</h3><b>Text:</b> {text}<br/><b>Key:</b> {key}<br/><b>Encrypted text:</b> <span style='color: #00b894; font-size: 1.2rem; font-weight: bold;'>{encrypted_text}</span><br/><br/><a href='/vigenere'>Quay lại</a>"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText'].upper().replace(" ", "")
    key = request.form['inputKeyPlain'].upper().replace(" ", "")
    
    if not text.isalpha() or not key.isalpha():
        return "<h3 style='color:red;'>LỖI: Vigenère chỉ chấp nhận chữ cái A-Z!</h3><a href='/vigenere'>Quay lại</a>"
    if len(key) > len(text):
        return f"<h3 style='color:red;'>LỖI: Độ dài khóa ({len(key)}) không được vượt quá độ dài bản mã ({len(text)})!</h3><a href='/vigenere'>Quay lại</a>"

    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.decrypt_text(text, key)
    return f"<h3 style='color: #0a4275;'>Kết quả Giải mã Vigenère</h3><b>Cipher text:</b> {text}<br/><b>Key:</b> {key}<br/><b>Decrypted text:</b> <span style='color: #d63031; font-size: 1.2rem; font-weight: bold;'>{decrypted_text}</span><br/><br/><a href='/vigenere'>Quay lại</a>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)