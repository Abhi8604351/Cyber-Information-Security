def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter Choice: ")

message = input("Enter Message: ")
shift = int(input("Enter Shift Value: "))

if choice == "1":
    print("Encrypted Message:", encrypt(message, shift))
elif choice == "2":
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid Choice")
