import hashlib
import tkinter as tk
from tkinter import messagebox


# ---------------- RSA KEY GENERATION ----------------

def generate_keys():
    p = 61
    q = 53

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17
    d = 2753

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


# ---------------- HASH FUNCTION ----------------

def create_hash(message):
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    return int(hash_value, 16)


# ---------------- CREATE DIGITAL SIGNATURE ----------------

def create_signature(message, private_key):
    d, n = private_key

    hash_value = create_hash(message)

    signature = pow(hash_value, d, n)

    return signature


# ---------------- VERIFY SIGNATURE ----------------

def verify_signature(message, signature, public_key):
    e, n = public_key

    hash_value = create_hash(message)

    decrypted_signature = pow(signature, e, n)

    return decrypted_signature == hash_value % n


# ---------------- CLI MODE ----------------

def cli_program():

    public_key, private_key = generate_keys()

    while True:

        print("\n===================================")
        print("       RSA DIGITAL SIGNATURE")
        print("===================================")
        print("1. Generate Digital Signature")
        print("2. Verify Digital Signature")
        print("3. Show RSA Keys")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        # Generate Signature
        if choice == "1":

            message = input("\nEnter message: ")

            signature = create_signature(
                message,
                private_key
            )

            print("\nMessage:", message)
            print("Digital Signature:", signature)

        # Verify Signature
        elif choice == "2":

            message = input("\nEnter message: ")
            signature_input = input("Enter digital signature: ")

            try:
                signature = int(signature_input)

                result = verify_signature(
                    message,
                    signature,
                    public_key
                )

                if result:
                    print("\n✓ Signature Verified")
                    print("✓ Message is authentic and unchanged.")

                else:
                    print("\n✗ Signature Verification Failed")
                    print("✗ Message may have been modified.")

            except ValueError:
                print("\nInvalid signature. Enter numbers only.")

        # Show Keys
        elif choice == "3":

            print("\nPublic Key :", public_key)
            print("Private Key:", private_key)

        # Exit
        elif choice == "4":

            print("\nExiting program...")
            break

        else:

            print("\nInvalid choice. Please try again.")


# ---------------- GUI FUNCTIONS ----------------

def gui_generate():

    message = message_entry.get()

    if message == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a message."
        )
        return

    signature = create_signature(
        message,
        private_key
    )

    signature_entry.delete(0, tk.END)
    signature_entry.insert(0, str(signature))

    result_label.config(
        text="Digital signature generated successfully."
    )


def gui_verify():

    message = message_entry.get()
    signature_text = signature_entry.get()

    if message == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a message."
        )
        return

    if signature_text == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a digital signature."
        )
        return

    try:

        signature = int(signature_text)

        result = verify_signature(
            message,
            signature,
            public_key
        )

        if result:

            result_label.config(
                text="✓ Signature Verified\n"
                     "✓ Message is authentic and unchanged."
            )

        else:

            result_label.config(
                text="✗ Verification Failed\n"
                     "✗ Message has been modified."
            )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Digital signature must contain numbers only."
        )


# ---------------- GUI MODE ----------------

def start_gui():

    global message_entry
    global signature_entry
    global result_label

    root = tk.Tk()

    root.title("RSA Digital Signature")
    root.geometry("550x450")

    title = tk.Label(
        root,
        text="RSA DIGITAL SIGNATURE",
        font=("Arial", 18, "bold")
    )

    title.pack(pady=20)

    tk.Label(
        root,
        text="Enter Message:"
    ).pack()

    message_entry = tk.Entry(
        root,
        width=55
    )

    message_entry.pack(pady=8)

    tk.Button(
        root,
        text="Generate Digital Signature",
        command=gui_generate,
        width=30
    ).pack(pady=10)

    tk.Label(
        root,
        text="Digital Signature:"
    ).pack()

    signature_entry = tk.Entry(
        root,
        width=55
    )

    signature_entry.pack(pady=8)

    tk.Button(
        root,
        text="Verify Signature",
        command=gui_verify,
        width=30
    ).pack(pady=10)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 11, "bold")
    )

    result_label.pack(pady=20)

    tk.Label(
        root,
        text="Public Key: " + str(public_key)
    ).pack()

    root.mainloop()


# ---------------- MAIN PROGRAM ----------------

public_key, private_key = generate_keys()

while True:

    print("\n===================================")
    print("     RSA DIGITAL SIGNATURE SYSTEM")
    print("===================================")
    print("1. CLI Mode")
    print("2. GUI Mode")
    print("3. Show Keys")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        cli_program()

    elif choice == "2":

        start_gui()

    elif choice == "3":

        print("\nPublic Key :", public_key)
        print("Private Key:", private_key)

    elif choice == "4":

        print("\nProgram terminated.")
        break

    else:

        print("\nInvalid choice. Please try again.")
