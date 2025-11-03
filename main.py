import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import hashlib, base64

# Convert password to key
def get_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Select File
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    file_label.config(text=filename)

# Encrypt Function
def encrypt_gui():
    try:
        password = password_entry.get()
        key = get_key(password)
        f = Fernet(key)

        with open(filename, 'rb') as file:
            data = file.read()

        encrypted_data = f.encrypt(data)

        with open("encrypted_" + filename.split("/")[-1], 'wb') as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", "✅ File Encrypted Successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# Decrypt Function
def decrypt_gui():
    try:
        password = password_entry.get()
        key = get_key(password)
        f = Fernet(key)

        with open(filename, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        with open("decrypted_" + filename.split("/")[-1], 'wb') as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", "✅ File Decrypted Successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# GUI Window
window = tk.Tk()
window.title("File Encryption/Decryption")
window.geometry("400x250")

# Widgets
tk.Button(window, text="Select File", command=browse_file).pack(pady=10)
file_label = tk.Label(window, text="No file selected")
file_label.pack()

tk.Label(window, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Button(window, text="Encrypt", command=encrypt_gui, bg="lightgreen").pack(pady=10)
tk.Button(window, text="Decrypt", command=decrypt_gui, bg="lightblue").pack()

window.mainloop()
