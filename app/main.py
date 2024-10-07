from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Function to encrypt text
def encrypt_text(plain_text):
    return cipher.encrypt(plain_text.encode())

# Function to decrypt text
def decrypt_text(encrypted_text):
    return cipher.decrypt(encrypted_text).decode()

# Example usage
if __name__ == "__main__":
    text = "Hello, World!"
    encrypted = encrypt_text(text)
    print("Encrypted:", encrypted)

    decrypted = decrypt_text(encrypted)
    print("Decrypted:", decrypted)
