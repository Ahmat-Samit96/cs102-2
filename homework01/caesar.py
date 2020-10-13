import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    k1=ord("a")   #65
    k2=ord("z")   #90
    k3=ord("A")   #97
    k4=ord("Z")   #122
    k5=26   #Количество букв в английском языке
    for i in plaintext:
        if i.isalpha():
            if k1<=ord(i)<=k2:
                a=chr((((ord(i)-k1)+shift)%k5)+k1)
                ciphertext += a
            elif k3<=ord(i)<=k4:
                a=chr((((ord(i)-k3)+shift)%k5)+k3)
                ciphertext += a
        else:
            ciphertext += i
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    k1=ord("a")   #65
    k2=ord("z")   #90
    k3=ord("A")   #97
    k4=ord("Z")   #122
    k5=26   #Количество букв в английском языке
    for i in ciphertext:
        if i.isalpha():
            if k1<=ord(i)<=k2:
                a=chr((((ord(i)-k1)-shift)%k5)+k1)
                plaintext += a
            elif k3<=ord(i)<=k4:
                a=chr((((ord(i)-k3)-shift)%k5)+k3)
                plaintext += a
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
