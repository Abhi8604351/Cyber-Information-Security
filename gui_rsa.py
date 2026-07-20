from tkinter import *

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17

while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

def encrypt():
    message = entry.get()

    encrypted = [pow(ord(ch), e, n) for ch in message]

    output.delete(0, END)
    output.insert(0, str(encrypted))

def decrypt():
    data = output.get()

    try:
        data = (data.replace("[", "")
                    .replace("]", "")
                    .replace("(", "")
                    .replace(")", "")
                    .replace(",", " "))

        encrypted = list(map(int, data.split()))

        decrypted = ''.join(chr(pow(num, d, n)) for num in encrypted)

        result.config(text="Decrypted Message: " + decrypted)

    except:
        result.config(text="Invalid Encrypted Data")

def clear():
    entry.delete(0, END)
    output.delete(0, END)
    result.config(text="")

root = Tk()
root.title("RSA Encryption & Decryption")
root.geometry("550x320")
root.resizable(False, False)

Label(root,
      text="RSA Encryption & Decryption",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Enter Message").pack()

entry = Entry(root, width=55, font=("Arial", 11))
entry.pack(pady=5)

Button(root,
       text="Encrypt",
       width=15,
       command=encrypt).pack(pady=5)

Label(root, text="Encrypted Message").pack()

output = Entry(root, width=55, font=("Arial", 11))
output.pack(pady=5)

Button(root,
       text="Decrypt",
       width=15,
       command=decrypt).pack(pady=5)

result = Label(root,
               text="",
               font=("Arial", 12, "bold"))
result.pack(pady=10)

Button(root,
       text="Clear",
       width=10,
       command=clear).pack(side=LEFT, padx=70, pady=20)

Button(root,
       text="Exit",
       width=10,
       command=root.destroy).pack(side=RIGHT, padx=70, pady=20)

root.mainloop()
