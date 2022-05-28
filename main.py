Morse_Alphabets = {
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

inverse = dict((a, b) for (b, a) in Morse_Alphabets.items())


# parse a morse code string string_Position is the starting point for decoding
def Decode_Morse(code, string_Position=0):
    if string_Position < len(code):
        Morse_Letter = ""
        for key, char in enumerate(code[string_Position:]):
            if char == " ":
                string_Position = key + string_Position + 1
                letter = inverse[Morse_Letter]
                return letter + Decode_Morse(code, string_Position)

            else:
                Morse_Letter += char
    else:
        return ""


# encode a message in morse code, spaces between words are represented by '/'
def To_Morse(message):
    encodedMessage = ""
    for char in message[:]:
        encodedMessage += Morse_Alphabets[char.upper()] + " "

    return encodedMessage

#User inputs

cipher_direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
message = input("Please enter your message:\n")

#user response
if cipher_direction == "decode":
    plain_text = Decode_Morse(message)
    print(f"Your plain text for '{message}' is '{plain_text}'")
elif cipher_direction == "encode":
    morse_code = To_Morse(message)
    print(f" Your morse code for '{message}' is '{morse_code}'")
else:
    print("Enter a valid cipher direction and message")