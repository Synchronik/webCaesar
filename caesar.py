from sys import argv, exit

def userInputIsValid():
    if not len(argv) > 1:
        print("Please enter an integer for the rotation!")
        exit()

    if argv[1].isdigit() == False:
        print("Please enter an integer for the rotation!")
        exit()

def encrypt(mess, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted = ''
    for char in mess:
        if char not in alphabet and char not in ALPHABET:
            encrypted = encrypted + char
        if char in ALPHABET:
            rotated_index = ALPHABET.index(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + ALPHABET[rotated_index]
            else:
                encrypted = encrypted + ALPHABET[rotated_index % 26]
        if char in alphabet:
            rotated_index = alphabet.index(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted

def main():
    mess = str(input("Please enter a message"))
    userInputIsValid()
    rot = int(argv[1])
    print(encrypt(mess, rot))


if __name__ == "__main__":
    main()
