import tkinter as tk

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt():
    result.set(encrypt(message.get(), -int(shift.get())))

def encrypt_message():
    result.set(encrypt(message.get(), int(shift.get())))

root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Message").pack()
message = tk.Entry(root, width=40)
message.pack()

tk.Label(root, text="Shift").pack()
shift = tk.Entry(root)
shift.pack()

result = tk.StringVar()

tk.Button(root, text="Encrypt", command=encrypt_message).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

tk.Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
