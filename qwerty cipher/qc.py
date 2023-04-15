def encryption():
    plain = input("Enter plain text: ")
    substitutions = {'a': '€','b': '/','c': '+','d': '$','e': '<',
        'f': '&','g': '*','h': ']','i': '8','j': '}','k': "'",'l': '≠','m': '¢','n': '@','o': '∂','p': 'ƒ',
        'q': '∫','r': 'å','s': 'œ','t': '4','u': '9','v': ':','w': '~','x': 'π','y': 'ø','z': '¥'}
    enc = ''.join(substitutions.get(c, c) for c in plain)
    print("Encrypted text: " + enc)
def decrypt():
    encrypted = input("Enter encrypted text: ")
    redo={'€': 'a', '/': 'b', '+': 'c', '$': 'd', '<': 'e','&': 'f', '*': 'g', ']': 'h', '8': 'i', '}': 'j',"'": 'k', '≠': 'l', '¢': 'm', '@': 'n', '∂': 'o',
         'ƒ': 'p', '∫': 'q', 'å': 'r', 'œ': 's', '4': 't','9': 'u', ':': 'v', '~': 'w', 'π': 'x', 'ø': 'y','¥': 'z'}
    dec = ''.join(redo.get(c, c) for c in encrypted)
    print("Decrypted text: " + dec)
choose = input("1 for encryption and 2 for decryption: ")
while choose not in ["1", "2"]:
    print("Please select a valid input.")
    choose = input("1 for encryption and 2 for decryption: ")
if choose == "1":
    encryption()
elif choose == "2":
    decrypt()
