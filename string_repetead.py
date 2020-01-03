# Vamos a construir un programa que nos permita encontrar el primer carácter que no se repite en un string.
# Por ejemplo si tenemos el string mimamameama el primer carácter que no se repite es la i.


# "abacabad"   C
# "abcabababababac" _


def first_no_repeating_character(sequence):
    seen_letters = {}
    for idx, letter in enumerate(sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (
                seen_letters[letter][0],
                seen_letters[letter][1] + 1,
            )
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])
    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return "_"


if __name__ == "__main__":
    char_sequence = str(input("write a sequence of chars: "))
    result = first_no_repeating_character(char_sequence)
    print(result)
