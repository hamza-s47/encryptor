from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from .controllers.controller import TextEncryptor

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins":["https://textlok.vercel.app", "http://localhost:1357", "chrome-extension://ffjlmdagmlmmdialpfmhblciipklieic"]}})

@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')


@app.route('/api/encrypt', methods=['POST'])
def enc_route():

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    
    try:
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
            text = TextEncryptor().decrypt_text(str.encode(enc_text), str.encode(key))
            body = {
                "message": "Decrypted successfully",
                "status": 200,
                "data": { "text": text }
            }
            return jsonify(body)
    
    except Exception as e:
        return jsonify({"error": "Invalid key or encrypted text", "message":str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
