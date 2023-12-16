def shift_character(character: str, shift_distance: int) -> str:
    """
    Shift letters from the english alphabet around the clock. 

    params:
     - character: must be a lower case letter [a-z]
     - shift_distance: by how much the character is to be shifted.

    examples:
     - character: 'a', shift_distance: 3 -> 'd'
     - character: 'z', shift_distance: 1 -> 'a'
    """
    A_ORD = 97
    COUNT_LETTERS_IN_ALPHABET = 26
    ret = chr(((ord(character) - A_ORD) + shift_distance) % COUNT_LETTERS_IN_ALPHABET + A_ORD) 
    return ret

def ceaser_shift(word, shift_distance: int):
    output = ""
    for character in word:
        if character == " ":
            output += " " 
        else:
            output += shift_character(character, shift_distance)
    return output

def decoder(input_str: str) -> str:
    input_without_space = input_str.lower()
    if not input_without_space.replace(" ", "").isalpha():
        return decoder(input("Das waren nicht nur Buchstaben. Noch einmal: "))

    for i in range(26):
        print (ceaser_shift(input_without_space, i))

if __name__ == "__main__":
    code = input("Bitte gib mir den input: ")
    decoder(code)

