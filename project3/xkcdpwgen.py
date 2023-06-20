#!/usr/bin/env python3

import argparse
import random
import string

def generate_password(words, caps, numbers, symbols):
    # Load the word list
    with open("words.txt") as f:
        wordlist = [word.strip() for word in f.readlines()]

    # Select the words
    password_words = random.sample(wordlist, words)

    # Capitalize random words
    for _ in range(caps):
        word_to_capitalize = random.choice(password_words)
        password_words = [word.capitalize() if word == word_to_capitalize else word for word in password_words]

    # Convert the list of words to a list of characters
    password = password_words

    # Add random numbers
    for _ in range(numbers):
        position = random.randint(1, len(password))  # Positions start from 1 to insert between words
        password.insert(position, str(random.randint(0,9)))

    # Add random symbols
    for _ in range(symbols):
        position = random.randint(1, len(password))  # Positions start from 1 to insert between words
        password.insert(position, random.choice(string.punctuation))

    # Convert the list of characters back into a string
    return "".join(password)

def main():
    parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method')
    parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password (default=4)')
    parser.add_argument('-c', '--caps', type=int, default=0, help='capitalize the first letter of CAPS random words (default=0)')
    parser.add_argument('-n', '--numbers', type=int, default=0, help='insert NUMBERS random numbers in the password (default=0)')
    parser.add_argument('-s', '--symbols', type=int, default=0, help='insert SYMBOLS random symbols in the password (default=0)')
    
    args = parser.parse_args()
    
    password = generate_password(args.words, args.caps, args.numbers, args.symbols)
    print(password)

if __name__ == "__main__":
    main()