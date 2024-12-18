# Morse code mappings for English letters to Morse
morse_mapping = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", 
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", 
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", 
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char == ' ':
            morse_code.append('/')  # Add a slash for spaces
        else:
            morse_code.append(morse_mapping.get(char, ''))  # Use Morse mapping for other characters
    return ' '.join(morse_code)

if __name__ == "__main__":
    text_input = input("Enter Text: ")
    print("Translated Morse Code:", text_to_morse(text_input))


if __name__ == "__main__":
    text_input = input("Enter Text: ")
    print("Translated Morse Code:", text_to_morse(text_input))
