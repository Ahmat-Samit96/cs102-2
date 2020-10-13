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
    k1 = ord("a")  # 65
    k2 = ord("z")  # 90
    k3 = ord("A")  # 97
    k4 = ord("Z")  # 122
    k5 = 26  # Количество букв в английском языке
    for i, letter in enumerate(plaintext):
        shift = ord((keyword[i % len(keyword)]).lower()) - k1
        if letter.isalpha() and shift != 0:
            chr_i = ord(letter)
            if k1 <= chr_i <= k2:
                chr_i = chr_i + shift
                if chr_i > k2:
                    chr_i = chr_i - k5
                ciphertext += chr(chr_i)
            elif k3 <= chr_i <= k4:
                chr_i = chr_i + shift
                if chr_i > k4:
                    chr_i = chr_i - k5
                ciphertext += chr(chr_i)
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
    k1 = ord("a")  # 65
    k2 = ord("z")  # 90
    k3 = ord("A")  # 97
    k4 = ord("Z")  # 122
    k5 = 26  # Количество букв в английском языке
    for i, letter in enumerate(ciphertext):
        shift = ord((keyword[i % len(keyword)]).lower()) - k1
        if letter.isalpha() and shift != 0:
            chr_i = ord(letter)
            if k1 <= chr_i <= k2:
                chr_i = chr_i - shift
                if chr_i < k1:
                    chr_i = chr_i + k5
                plaintext += chr(chr_i)
            elif k3 <= chr_i <= k4:
                chr_i = chr_i - shift
                if chr_i < k3:
                    chr_i = chr_i + k5
                plaintext += chr(chr_i)
        else:
            plaintext += letter
    return plaintext
