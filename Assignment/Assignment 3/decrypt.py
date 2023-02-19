"""
FINDING THE KEY
"""

from typing import TextIO  # Specific annotations


def decrypt(input_file: TextIO, wordlist_filename: str) -> str:
    """
    Using wordlist_filename, decrypt input_file according to the handout
    instructions, and return the plaintext.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word_tail = ['ed', 's', 'es', 'ing', 'ment', 'ments', 'ful', 'fully', 'fulness']
    lead_word_max_count = 0
    lead_word_count = 0
    lead_word = ''
    is_first_read = True

    if wordlist_filename != '':
        f = open(wordlist_filename, 'r')
        while True:
            line = f.readline()
            if not line:
                break
            read_word = line.strip()

            if is_first_read:
                lead_word = read_word
                is_first_read = False
                continue

            if read_word.startswith(lead_word):
                for i in range(0, len(word_tail)):
                    word = lead_word + word_tail[i]
                    if read_word == word:
                        lead_word_count += 1
                if lead_word_count == 0:
                    lead_word = read_word
            else:
                if lead_word_count >= lead_word_max_count:
                    lead_word_max_count = lead_word_count
                lead_word_count = 0
                lead_word = read_word
        f.close()
    else:
        lead_word_max_count = 1

    decrypt_words = ''
    while True:
        read_line = input_file.readline()
        if not read_line:
            break
        for i in range(0, len(read_line)):
            if read_line[i].isalpha():
                idx = alphabet.index(read_line[i].lower())
                decrypt_words += alphabet[idx - lead_word_max_count]
            else:
                decrypt_words += read_line[i]
    input_file.close()
    return decrypt_words


if __name__ == "__main__":
    # Sample input from the handout -- you can tweak this if you like
    print(decrypt(open("book1.txt"), "wordlist.txt"))
    print(decrypt(open("book2.txt"), "wordlist.txt"))
    print(decrypt(open("book3.txt"), ""))
