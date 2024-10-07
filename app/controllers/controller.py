from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt text
def encrypt_text(plain_text):
    return cipher.encrypt(plain_text.encode())

# Decrypt text
def decrypt_text(encrypted_text):
    return cipher.decrypt(encrypted_text).decode()

# Encrypt file
def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

# Decrypt file
def decrypt_file(encrypted_file_path, key):
    cipher = Fernet(key)
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(encrypted_file_path.replace('.encrypted', ''), 'wb') as file:
        file.write(decrypted_data)

# Example usage
# if __name__ == "__main__":
#     # Generate a key and save it (important!)
#     key = Fernet.generate_key()
#     with open('secret.key', 'wb') as key_file:
#         key_file.write(key)

#     # Encrypt a file
#     encrypt_file('example.txt', key)

#     # Decrypt the file
#     decrypt_file('example.txt.encrypted', key)
