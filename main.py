from flask import Flask, render_template, request, send_file, redirect, url_for
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load or generate a persistent encryption key
KEY_FILE = 'secret.key'
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, 'rb') as f:
        key = f.read()
else:
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

fernet = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt_upload', methods=['GET', 'POST'])
def encrypt_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            with open(filepath, 'rb') as f:
                encrypted_data = fernet.encrypt(f.read())

            encrypted_path = os.path.join(UPLOAD_FOLDER, 'enc_' + file.filename)
            with open(encrypted_path, 'wb') as f:
                f.write(encrypted_data)

            return render_template('success.html', action='encrypted', filename='enc_' + file.filename)
    return render_template('preview.html', action='encrypt')

@app.route('/decrypt_upload', methods=['GET', 'POST'])
def decrypt_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            try:
                with open(filepath, 'rb') as f:
                    decrypted_data = fernet.decrypt(f.read())

                decrypted_path = os.path.join(UPLOAD_FOLDER, 'dec_' + file.filename)
                with open(decrypted_path, 'wb') as f:
                    f.write(decrypted_data)

                return render_template('success.html', action='decrypted', filename='dec_' + file.filename)
            except Exception as e:
                return f"<h2>Error during decryption: {str(e)}</h2>"
    return render_template('preview.html', action='decrypt')

@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
