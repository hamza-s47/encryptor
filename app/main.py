from flask import Flask, render_template, jsonify, request
from .controllers.controller import TextEncryptor

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')


@app.route('/api/encrypt', methods=['POST'])
def enc_route():
    # Get JSON data from the request
    data = request.get_json()

    # Check if the request was successful and if data is not None
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400

    if data.get('isEncrypt'):
        text = data.get('plainText')
        encrypted_text = TextEncryptor().encrypt_text(text)
        body = {
            "message": "Encrypted successfully",
            "status": 200,
            "data": encrypted_text
        }
        return jsonify(body)
    else:
        enc_text = data.get('encryptedText')
        key = data.get('key')
        decrypted_text = TextEncryptor().decrypt_text(str.encode(enc_text), str.encode(key))
        body = {
            "message": "Decrypted successfully",
            "status": 200,
            "data": decrypted_text
        }
        return jsonify(body)

if __name__ == '__main__':
    app.run(debug=True)
