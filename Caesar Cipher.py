def encrypt(s, shift):
    enc = ""
    if shift == 0:
        shift = 3
    
    for i in s:
        if i.islower():
            x = ord(i)
            new_pos = (x - 97 + shift) % 26 + 97
            enc += chr(new_pos)

        elif i.isupper():
            x = ord(i)
            new_pos = (x - 65 + shift) % 26 + 65
            enc += chr(new_pos)

        else:
            enc += i

    return enc

def decrypt(s, shift):
    dec = ""
    if shift == 0:
        shift = 3

    for i in s:
        if i.islower():
            x = ord(i)
            new_pos = (x - 97 - shift) % 26 + 97
            dec += chr(new_pos)

        elif i.isupper():
            x = ord(i)
            new_pos = (x - 65 - shift) % 26 + 65
            dec += chr(new_pos)
            
        else:
            dec += i

    return dec

def main():
    while True:
        choice = input(" Enter '1' to encrypt\n Enter '2' to decrypt\n Enter exit to terminate: ")

        if choice == '1':
            s = input(" Enter a string to encrypt: ")
            shift = int(input(" Enter a shift: "))

            result = encrypt(s, shift)
            print(" Encrypted string:", result)
            print(' ------------------------------------')

        elif choice == '2':
            s = input(" Enter a string to decrypt: ")
            shift = int(input(" Enter a shift: "))

            result = decrypt(s, shift)
            print(" Decrypted string:", result)
            print(' ------------------------------------')

        elif choice == 'exit':
            break

        else:
            print(" Invalid choice!")
    print(' Thank you ')
    

if __name__ == "__main__":
    main()

