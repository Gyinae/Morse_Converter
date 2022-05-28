morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())


# parse a morse code string positionInString is the starting point for decoding
def decodeMorse(code, positionInString=0):
    if positionInString < len(code):
        morseLetter = ""
        for key, char in enumerate(code[positionInString:]):
            if char == " ":
                positionInString = key + positionInString + 1
                letter = inverseMorseAlphabet[morseLetter]
                return letter + decodeMorse(code, positionInString)

            else:
                morseLetter += char
    else:
        return ""


# encode a message in morse code, spaces between words are represented by '/'
def encodeToMorse(message):
    encodedMessage = ""
    for char in message[:]:
        encodedMessage += morseAlphabet[char.upper()] + " "

    return encodedMessage

#User inputs

cipher_direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
message = input("Please enter your message:\n")

#user response
if cipher_direction == "decode":
    plain_text = decodeMorse(message)
    print(f"Your plain text for '{message}' is {plain_text}")
elif cipher_direction == "encode":
    morse_code = encodeToMorse(message)
    print(f" Your morse code for '{message}' is {morse_code}")
else:
    print("Enter a valid cipher direction and message")