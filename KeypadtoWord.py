def get_t9_reverse_map():
    t9_letter_to_sequence_map = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
        ' ': '0',
        '_': '_'
    }

    return {sequence: letter for letter, sequence in t9_letter_to_sequence_map.items()}


def run_length_encode_digits(raw_digit_sequence):
    if not raw_digit_sequence:
        return []

    encoded_runs_list = []
    current_index = 0
    sequence_length = len(raw_digit_sequence)

    while current_index < sequence_length:
        current_char = raw_digit_sequence[current_index]

        max_t9_presses = 1
        current_key = current_char

        if current_char.isdigit():
            current_key_val = int(current_char)
            current_key = current_key_val

            if current_key_val in (7, 9):
                max_t9_presses = 4
            elif 2 <= current_key_val <= 6 or current_key_val == 8:
                max_t9_presses = 3

        search_index = current_index
        while search_index < sequence_length and raw_digit_sequence[search_index] == current_char:
            search_index += 1

        consecutive_count = search_index - current_index

        while consecutive_count > 0:
            presses_in_run = min(consecutive_count, max_t9_presses)
            encoded_runs_list.append((current_key, presses_in_run))
            consecutive_count -= presses_in_run

        current_index = search_index

    return encoded_runs_list


def keypad_runs_to_word(encoded_runs):
    reverse_map = get_t9_reverse_map()
    word_parts = []

    for key, count in encoded_runs:

        if isinstance(key, int):
            key_sequence = str(key) * count
        else:
            key_sequence = key * count

        letter = reverse_map.get(key_sequence, f"[{key_sequence}]")
        word_parts.append(letter)

    return "".join(word_parts)


word = input("Enter the Keypad:")
print(f"The word to your Keypad:{word} is {keypad_runs_to_word(run_length_encode_digits(word))}")
