def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i, letter in enumerate(plaintext):
        shift2 = keyword[i % len(keyword)]
        shift = ord((shift2).lower()) - ord("a")
        if letter.isalpha() != 0 and shift != 0:
            chr_i = ord(letter)
            if 65 <= chr_i <= 90:
                chr_i = chr_i + shift
                if chr_i > 90:
                    chr_i = chr_i - 26
                letter_i = chr(chr_i)
                ciphertext += letter_i
            elif 97 <= chr_i <= 122:
                chr_i = chr_i + shift
                if chr_i > 122:
                    chr_i = chr_i - 26
                letter_i = chr(chr_i)
                ciphertext += letter_i
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i, letter in enumerate(ciphertext):
        shift2 = keyword[i % len(keyword)]
        shift = ord((shift2).lower()) - ord("a")
        if letter.isalpha() != 0 and shift != 0:
            chr_i = ord(letter)
            if 65 <= chr_i <= 90:
                chr_i = chr_i - shift
                if chr_i < 65:
                    chr_i = chr_i + 26
                letter_i = chr(chr_i)
                plaintext += letter_i
            elif 97 <= chr_i <= 122:
                chr_i = chr_i - shift
                if chr_i < 97:
                    chr_i = chr_i + 26
                letter_i = chr(chr_i)
                plaintext += letter_i
        else:
            plaintext += letter
    return plaintext
