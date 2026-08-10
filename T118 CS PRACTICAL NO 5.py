import tkinter as tk
from tkinter import messagebox


# ---------------- DIFFIE-HELLMAN FUNCTION ----------------

def calculate_keys(p, g, person_a_private, person_b_private):

    person_a_public = pow(g, person_a_private, p)
    person_b_public = pow(g, person_b_private, p)

    person_a_secret = pow(
        person_b_public,
        person_a_private,
        p
    )

    person_b_secret = pow(
        person_a_public,
        person_b_private,
        p
    )

    return (
        person_a_public,
        person_b_public,
        person_a_secret,
        person_b_secret
    )


# ---------------- CLI MODE ----------------

def cli_mode():

    while True:

        print("\n===================================")
        print("       DIFFIE-HELLMAN KEY EXCHANGE")
        print("===================================")
        print("1. Perform Key Exchange")
        print("2. Show Explanation")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            try:
                p = int(input("\nEnter prime number (p): "))
                g = int(input("Enter primitive root (g): "))

                person_a_private = int(
                    input("Enter Person A private key: ")
                )

                person_b_private = int(
                    input("Enter Person B private key: ")
                )

                (
                    person_a_public,
                    person_b_public,
                    person_a_secret,
                    person_b_secret
                ) = calculate_keys(
                    p,
                    g,
                    person_a_private,
                    person_b_private
                )

                print("\n---------- RESULTS ----------")

                print(
                    "Person A public key :",
                    person_a_public
                )

                print(
                    "Person B public key :",
                    person_b_public
                )

                print(
                    "Person A shared key :",
                    person_a_secret
                )

                print(
                    "Person B shared key :",
                    person_b_secret
                )

                if person_a_secret == person_b_secret:
                    print("\nKey exchange successful!")
                    print(
                        "Both persons have the same shared secret."
                    )
                else:
                    print("\nKey exchange failed.")

            except ValueError:
                print("\nPlease enter numbers only.")

        elif choice == "2":

            print("\nDiffie-Hellman allows two persons to")
            print("create a common secret key over")
            print("an insecure network.")

            print("\nPrivate keys are never exchanged.")
            print("Only public keys are shared.")

        elif choice == "3":

            print("\nExiting program...")
            break

        else:

            print("\nInvalid choice. Try again.")


# ---------------- GUI FUNCTIONS ----------------

def gui_exchange():

    try:

        p = int(p_entry.get())
        g = int(g_entry.get())

        person_a_private = int(
            person_a_entry.get()
        )

        person_b_private = int(
            person_b_entry.get()
        )

        (
            person_a_public,
            person_b_public,
            person_a_secret,
            person_b_secret
        ) = calculate_keys(
            p,
            g,
            person_a_private,
            person_b_private
        )

        person_a_public_entry.delete(0, tk.END)
        person_a_public_entry.insert(
            0,
            str(person_a_public)
        )

        person_b_public_entry.delete(0, tk.END)
        person_b_public_entry.insert(
            0,
            str(person_b_public)
        )

        person_a_secret_entry.delete(0, tk.END)
        person_a_secret_entry.insert(
            0,
            str(person_a_secret)
        )

        person_b_secret_entry.delete(0, tk.END)
        person_b_secret_entry.insert(
            0,
            str(person_b_secret)
        )

        if person_a_secret == person_b_secret:

            result_label.config(
                text="✓ Key Exchange Successful\n"
                     "Both persons have the same shared secret."
            )

        else:

            result_label.config(
                text="✗ Key Exchange Failed"
            )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )


# ---------------- CLEAR GUI ----------------

def clear_gui():

    entries = [
        p_entry,
        g_entry,
        person_a_entry,
        person_b_entry,
        person_a_public_entry,
        person_b_public_entry,
        person_a_secret_entry,
        person_b_secret_entry
    ]

    for entry in entries:
        entry.delete(0, tk.END)

    result_label.config(text="")


# ---------------- GUI MODE ----------------

def gui_mode():

    global p_entry
    global g_entry
    global person_a_entry
    global person_b_entry
    global person_a_public_entry
    global person_b_public_entry
    global person_a_secret_entry
    global person_b_secret_entry
    global result_label

    root = tk.Tk()

    root.title("Diffie-Hellman Key Exchange")
    root.geometry("600x600")

    tk.Label(
        root,
        text="DIFFIE-HELLMAN KEY EXCHANGE",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tk.Label(
        root,
        text="Public Values",
        font=("Arial", 12, "bold")
    ).pack()

    tk.Label(
        root,
        text="Prime Number (p)"
    ).pack()

    p_entry = tk.Entry(root, width=35)
    p_entry.pack(pady=5)

    tk.Label(
        root,
        text="Primitive Root (g)"
    ).pack()

    g_entry = tk.Entry(root, width=35)
    g_entry.pack(pady=5)

    tk.Label(
        root,
        text="Private Keys",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    tk.Label(
        root,
        text="Person A Private Key"
    ).pack()

    person_a_entry = tk.Entry(root, width=35)
    person_a_entry.pack(pady=5)

    tk.Label(
        root,
        text="Person B Private Key"
    ).pack()

    person_b_entry = tk.Entry(root, width=35)
    person_b_entry.pack(pady=5)

    tk.Button(
        root,
        text="Perform Key Exchange",
        command=gui_exchange,
        width=30
    ).pack(pady=15)

    tk.Label(
        root,
        text="Person A Public Key"
    ).pack()

    person_a_public_entry = tk.Entry(
        root,
        width=35
    )
    person_a_public_entry.pack(pady=5)

    tk.Label(
        root,
        text="Person B Public Key"
    ).pack()

    person_b_public_entry = tk.Entry(
        root,
        width=35
    )
    person_b_public_entry.pack(pady=5)

    tk.Label(
        root,
        text="Person A Shared Key"
    ).pack()

    person_a_secret_entry = tk.Entry(
        root,
        width=35
    )
    person_a_secret_entry.pack(pady=5)

    tk.Label(
        root,
        text="Person B Shared Key"
    ).pack()

    person_b_secret_entry = tk.Entry(
        root,
        width=35
    )
    person_b_secret_entry.pack(pady=5)

    tk.Button(
        root,
        text="Clear",
        command=clear_gui,
        width=15
    ).pack(pady=10)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 11, "bold")
    )
    result_label.pack(pady=10)

    root.mainloop()


# ---------------- MAIN MENU ----------------

while True:

    print("\n===================================")
    print("     DIFFIE-HELLMAN KEY EXCHANGE")
    print("===================================")
    print("1. CLI Mode")
    print("2. GUI Mode")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        cli_mode()

    elif choice == "2":

        gui_mode()

    elif choice == "3":

        print("\nProgram terminated.")
        break

    else:

        print("\nInvalid choice. Please try again.")
