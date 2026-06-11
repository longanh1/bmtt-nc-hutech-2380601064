import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plaintext": self.ui.txt_plaintext.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data.get("encryptmessage", ""))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption successful!")
                msg.exec_()
            else:
                print("Error while calling API:")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setText(data.get("decryptmessage", ""))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption successful!")
                msg.exec_()
            else:
                print("Error while calling API:")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())