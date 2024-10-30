# hash_art.py

from letters.uppercase_letters import art_dict_upper as uppercase_letters
from letters.lowercase_letters import art_dict_lower as lowercase_letters
from letters.special_characters import art_dict_special as special_characters

def print_hash_art(letters):
    """Prints the corresponding ASCII art for the given letters."""
    lines = ['' for _ in range(17)]  # As each letter has 17 lines

    for letter in letters:
        if letter in uppercase_letters:
            for i, line in enumerate(uppercase_letters[letter]):
                lines[i] += line + '  '  # Add space between letters
        elif letter in lowercase_letters:
            for i, line in enumerate(lowercase_letters[letter]):
                lines[i] += line + '  '  # Add space between letters
        elif letter in special_characters:
            for i, line in enumerate(special_characters[letter]):
                lines[i] += line + '  '  # Add space between letters
        else:
            print(f"Art not available for the letter: {letter}")


    # Print all lines together
    for line in lines:
        print(line)

if __name__ == "__main__":
    user_input = input("Enter one or more letters (for example, 'PumukyDev'): ")
    print_hash_art(user_input)
