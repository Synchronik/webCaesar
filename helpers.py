def alphabetposition(mess):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in mess:
        if char in ALPHABET:
            return ALPHABET.index(char)
    for char in mess:
        if char in alphabet:
            return alphabet.index(char)

def rotatecharacter(mess, rot):
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
            if char in alphabet:
                rotated_index = alphabet.index(char) + rot
                if rotated_index < 26:
                    encrypted = encrypted + alphabet[rotated_index]
                else:
                    encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted
