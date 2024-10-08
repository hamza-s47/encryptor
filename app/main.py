from flask import Flask, render_template
from .controllers.controller import encrypt_text, decrypt_text, encrypt_file, decrypt_file

app = Flask(__name__)

# abc= encrypt_text("I love automation")
# print(abc)

print(decrypt_text(b'gAAAAABnBS-0pL0ltnIfMy1GgIVX3AzaB0CeGnij-dJ87b8zXgHn4raADsrQkei2w4pcS4Xe-sZtuZ0HcyLiyLJ-xA_tOPj1-v3zC3dcaDyorhX_NQ2xPpM=', b'covqtWq7K1S6zDKDEDSfBWyJqPjw2POiuuYAQ3g_EG8='))

@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)