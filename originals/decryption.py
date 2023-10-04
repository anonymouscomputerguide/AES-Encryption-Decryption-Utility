from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64decode

def decrypt_aes(key, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    data = urlsafe_b64decode(ciphertext)
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return decrypted_data.rstrip(b'\0')  # Remove padding

if __name__ == "__main__":
    key = b'sixteen byte key'
    ciphertext = input("Enter the ciphertext to decrypt: ")

    decrypted_text = decrypt_aes(key, ciphertext)
    print(f"Decrypted message: {decrypted_text.decode()}")

    input("Press Enter to exit...")
