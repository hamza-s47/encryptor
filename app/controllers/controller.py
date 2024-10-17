from cryptography.fernet import Fernet

class EncryptorData:
    def __init__(self) -> None:
        self.__key = None

    def __generate_key(self):
        self.__key = Fernet.generate_key()
    
    @property
    def my_key(self):
        if self.__key is None:
            self.__generate_key()
            return self.__key

class TextEncryptor(EncryptorData):
    
    def encrypt_text(self, text):
        key = self.my_key
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt(text.encode())
        data = {
            "encrypted_text":encrypted_text,
            "private_key":key
        }
        return data
    
    def decrypt_text(self, encrypted_text, key):
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_text).decode()  
    
class FileEncryptor(EncryptorData):

    def encrypt_file(self, file_path):
        """Encrypt a file."""
        if self.key is None:
            raise ValueError("Key is not set. Please generate or provide a key.")
        cipher = Fernet(self.key)
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path + '.encrypted', 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, encrypted_file_path):
        """Decrypt a file."""
        if self.key is None:
            raise ValueError("Key is not set. Please generate or provide a key.")
        cipher = Fernet(self.key)
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(encrypted_file_path.replace('.encrypted', ''), 'wb') as file:
            file.write(decrypted_data)