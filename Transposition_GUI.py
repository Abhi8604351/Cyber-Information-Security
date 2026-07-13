import tkinter as tk

def encrypt():
    result.set(message.get()[::-1])

def decrypt():
    result.set(message.get()[::-1])

root = tk.Tk()
root.title("Transposition Cipher")

tk.Label(root, text="Message").pack()

message = tk.Entry(root, width=40)
message.pack()

result = tk.StringVar()

tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

tk.Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
