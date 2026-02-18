cipher_dict = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q',
    'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v',
    'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a',
    'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f',
    'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k',
    'z': 'l',

    'A': 'M', 'B': 'N', 'C': 'O', 'D': 'P', 'E': 'Q',
    'F': 'R', 'G': 'S', 'H': 'T', 'I': 'U', 'J': 'V',
    'K': 'W', 'L': 'X', 'M': 'Y', 'N': 'Z', 'O': 'A',
    'P': 'B', 'Q': 'C', 'R': 'D', 'S': 'E', 'T': 'F',
    'U': 'G', 'V': 'H', 'W': 'I', 'X': 'J', 'Y': 'K',
    'Z': 'L',

    '0': '5', '1': '6', '2': '7', '3': '8', '4': '9',
    '5': '0', '6': '1', '7': '2', '8': '3', '9': '4'
}

reverse_cipher_dict = {v: k for k, v in cipher_dict.items()}

def encode(message):
    result = ""
    for c in message:
        if c in cipher_dict:
            result += cipher_dict[c]
        else:
            result += c

    print("\nOriginal:", message)
    print("Cipher:  ", result)
    return result

def decode(cipher):
    original = ""
    for c in cipher:
        if c in reverse_cipher_dict:
            original += reverse_cipher_dict[c]
        else:
            original += c

    print("\nCipher:  ", cipher)
    print("Decoded:", original)
    return original

message = input("Enter your message: ")
cipher_text = ""

while True:
    choice = int(input("\n1 for encoding\n2 for decoding\n3 for exit\nEnter your choice: "))

    if choice == 1:
        cipher_text = encode(message)

    elif choice == 2:
        if cipher_text:
            decode(cipher_text)
        else:
            print("Nothing to decode. Encode first!")

    elif choice == 3:
        print("Exiting...")
        break

    else:

        print("Check your input!!!")
