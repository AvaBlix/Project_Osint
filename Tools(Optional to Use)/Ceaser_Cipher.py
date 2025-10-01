import string


def caesar_cipher(text, shift):
    UPPERCASE = string.ascii_uppercase
    LOWERCASE = string.ascii_lowercase

    shift %= 26

    result_chars = []

    for char in text:
        if char in UPPERCASE:
            current_index = UPPERCASE.index(char)
            new_index = (current_index + shift) % 26
            result_chars.append(UPPERCASE[new_index])

        elif char in LOWERCASE:
            current_index = LOWERCASE.index(char)
            new_index = (current_index + shift) % 26
            result_chars.append(LOWERCASE[new_index])

        else:
            result_chars.append(char)

    return "".join(result_chars)


input_word = input("Enter the Word:")
input_shift = int(input("Enter the Shift:"))

cipher_output = caesar_cipher(input_word, input_shift)

print(f"Original Word: {input_word}")
print(f"Shift Key:     {input_shift}")
print(f"Cipher Output: {cipher_output}")
