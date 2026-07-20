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

print("RSA ENCRYPTION & DECRYPTION")
print("Public Key :", (e, n))
print("Private Key:", (d, n))

while True:
    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter message to encrypt: ")

        encrypted = [pow(ord(ch), e, n) for ch in message]

        print("Encrypted Message:")
        print(encrypted)

    elif choice == "2":
        data = input("Enter encrypted numbers: ")

        try:
            data = (data.replace("[", "")
                        .replace("]", "")
                        .replace("(", "")
                        .replace(")", "")
                        .replace(",", " "))

            encrypted = list(map(int, data.split()))

            decrypted = ''.join(chr(pow(num, d, n)) for num in encrypted)

            print("Decrypted Message:")
            print(decrypted)

        except ValueError:
            print("Invalid encrypted data!")

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
