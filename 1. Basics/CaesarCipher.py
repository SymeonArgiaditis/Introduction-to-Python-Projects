#CAESAR CIPHER

def caesar(text, shift, encrypt = True) -> str:
    if not isinstance(shift, int):
        return "Shift must be an integer value!"
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25!"
    if not encrypt:
        shift = -shift
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translate_table = str.maketrans(alphabet+alphabet.upper(),shifted_alphabet+shifted_alphabet.upper())

    caesar_message = text.translate(translate_table)
    print(caesar_message)
    return caesar_message

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)

text: str = input("Give text: ")
shift: int = int(input("Give shift: "))

response = input("Do you want to encrypt(1) or decrypt(2)?\n")
if response == '1':
    encrypt(text, shift)
elif response == '2':
    decrypt(text, shift)
else:
    print("Invalid value!")
