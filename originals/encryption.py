from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

def encrypt_aes(key, data):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    padded_data = data + b'\0' * (16 - len(data) % 16)  # Pad data to a multiple of 16 bytes
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return urlsafe_b64encode(ciphertext)

def decrypt_aes(key, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    data = urlsafe_b64decode(ciphertext)
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return decrypted_data.rstrip(b'\0')  # Remove padding

if __name__ == "__main__":
    key = b'sixteen byte key'  # Change this to your desired key (must be 16, 24, or 32 bytes)
    user_input = input("Enter a message to encrypt: ").encode()

    ciphertext = encrypt_aes(key, user_input)
    print(f"Ciphertext: {ciphertext.decode()}")

    decrypted_text = decrypt_aes(key, ciphertext)
    print(f"Decrypted message: {decrypted_text.decode()}")

import pyperclip

# ... (previous code)

if __name__ == "__main__":
    # ... (previous code)

    # Instead of printing, save the output to a variable
    output = f"Ciphertext: {ciphertext.decode()}\nDecrypted message: {decrypted_text.decode()}"

    # Copy the output to the clipboard
    pyperclip.copy(output)
def decrypt_aes(key, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    data = urlsafe_b64decode(ciphertext)
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return decrypted_data.rstrip(b'\0')  # Remove padding

if __name__ == "__main__":
    key = b'sixteen byte key'
    user_input = input("Enter a message to encrypt: ").encode()

    ciphertext = encrypt_aes(key, user_input)
    print(f"Ciphertext: {ciphertext.decode()}")

    decrypted_text = decrypt_aes(key, ciphertext)
    print(f"Decrypted message: {decrypted_text.decode()}")

    input("Press Enter to exit...")

