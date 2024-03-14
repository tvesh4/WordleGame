import colorama
from colorama import Fore, Style
import random
colorama.init()

def read_words_from_file(file_name):
    words = []
    with open(file_name, "r") as file:
        for line in file:
            words.append(line.strip())
    return words

def print_output(guess, answer):
    output = ""
    for i in range(5):
        guess_letter = guess[i]
        answer_letter = answer[i]

        if guess_letter == answer_letter:
            output += Fore.GREEN + guess_letter
        elif guess_letter in answer:
            output += Fore.YELLOW + guess_letter
        else:
            output += Fore.WHITE + guess_letter

    print(output + Style.RESET_ALL)
    print()

def main():
    answers = read_words_from_file("answers.txt")
    validGuesses = read_words_from_file("validGuesses.txt")
    validGuesses.extend(answers)
    answer = random.choice(answers)
    guess = ""
    while guess != answer:
        guess = input("Guess the word: ")
        if guess not in validGuesses:
            print("Invalid guess. Try again.")
        else:
            print_output(guess, answer)
    print("Congratulations! You guessed the word correctly.")

if __name__ == "__main__":
    main()