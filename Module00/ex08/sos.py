import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def encode_string(string):
    morse_code_string = ''
    for char in string:
        if char == ' ':
            morse_code_string += '/'
        else:
            morse_code_string += MORSE_CODE_DICT.get(char.upper(), 'ERROR') + ' '
    return morse_code_string

if __name__ == '__main__':
    args = ' '.join(sys.argv[1:])
    if args:
        encoded_string = encode_string(args)
        if 'ERROR' in encoded_string:
            print('ERROR')
        else:
            print(encoded_string)

