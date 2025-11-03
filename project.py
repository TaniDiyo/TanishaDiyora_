from cryptography.fernet import Fernet
import hashlib, base64

# Convert password to a valid key
def get_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Encrypt file
def encrypt_file(filename, password):
    key = get_key(password)
    fernet = Fernet(key)

    with open(filename, 'rb') as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open("encrypted_" + filename, 'wb') as file:
        file.write(encrypted_data)

    print("✅ File Encrypted: encrypted_" + filename)

# Decrypt file
def decrypt_file(filename, password):
    key = get_key(password)
    fernet = Fernet(key)

    with open(filename, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open("decrypted_" + filename, 'wb') as file:
        file.write(decrypted_data)

    print("✅ File Decrypted: decrypted_" + filename)

# Main Program
choice = input("Encrypt or Decrypt (e/d): ")

if choice == "e":
    filename = input("Enter file name: ")
    password = input("Enter password: ")
    encrypt_file(filename, password)

elif choice == "d":
    filename = input("Enter encrypted file name: ")
    password = input("Enter password: ")
    decrypt_file(filename, password)

else:
    print("❌ Invalid choice!")
