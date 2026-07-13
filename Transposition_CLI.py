def encrypt(text):
    return text[::-1]

def decrypt(text):
    return text[::-1]

print("=== Transposition Cipher ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter Choice: ")

message = input("Enter Message: ")

if choice == "1":
    print("Encrypted Message:", encrypt(message))
elif choice == "2":
    print("Decrypted Message:", decrypt(message))
else:
    print("Invalid Choice")
