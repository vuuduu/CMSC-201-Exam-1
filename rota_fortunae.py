"""
File:         rota_fortunae.py
Author:       Vu Nguyen
Date:         10/9/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs take in a mystery texts and user have
              to either guessed the entire text or guess each letter
              of the mystery texts.

"""

if __name__ == "__main__":

    mystery_texts = input("What is the mystery texts you want the players to guess? ").strip()
    missing_list = []

    # This loop append underscore to the missing_list
    for i in mystery_texts:
        if i != " ":
            print("_", end='')
            missing_list.append('_')
        else:
            print(i, end='')
            missing_list.append(i)

    print()
    guess_letter = input('Guess a letter, or "solve": ').strip()

    is_Missing = True
    already_guessed = []

    # While there are still missing letter in the missing_list
    while is_Missing:

        # This condition evaluates for solve input
        if guess_letter.lower() == 'solve':
            entire_puzzle = input("What is the entire puzzle? ").strip()

            # This check to see their solve guess is correct.
            if entire_puzzle.lower() == mystery_texts.lower():
                print("You solved the puzzle!")
                is_Missing = False
            else:
                print("You didn't guessed the correct texts!")
                guess_letter = input('Guess a letter, or "solve": ').strip()
        else:

            # This condition checks for A Letter or Solve.
            if len(guess_letter) != 1:
                print("Please make sure to enter a single letter or type in the word 'solve'!")
                guess_letter = input('Guess a letter, or "solve": ').strip()
            else:

                # This condition checks if the letter has already been entered.
                if guess_letter in already_guessed:
                    print("You've already enter this letter")
                    guess_letter = input('Guess a letter, or "solve": ').strip()
                else:

                    # This loop check if guess_letter is in the mystery_text.
                    for index in range(len(mystery_texts)):
                        mystery_letter = mystery_texts[index]

                        if guess_letter.lower() == mystery_letter.lower():
                            missing_list[index] = mystery_letter

                    if guess_letter.lower() not in mystery_texts.lower():
                        print("There are no " + guess_letter + "'s in the mystery text")

                    # This condition checks for a completed guess.
                    if '_' not in missing_list:
                        for missing_value in missing_list:
                            print(missing_value, end='')
                        print()
                        print("You solved the puzzle!")
                        is_Missing = False
                    else:

                        # This loop print out the guessed letter and the underscore.
                        for missing_value in missing_list:
                            print(missing_value, end='')
                        print()
                        already_guessed.append(guess_letter)
                        guess_letter = input('Guess a letter, or "solve": ').strip()







