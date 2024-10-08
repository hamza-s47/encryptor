from .controllers.controller import encrypt_text, decrypt_text, encrypt_file, decrypt_file

abc= encrypt_text("My name is Hamza")

# abc = b'gAAAAABnBCGnl4nVY9bK5Fkm8Gb_Yod5vT5ySvnICtBgXMAPQw72P_R54uDaExXe1rLMAdG-ysfJBacRicJPkOEB_VgC5nIyaQfDdS7gz4pjZAnxXtgY3Kc='

print(decrypt_text(abc))