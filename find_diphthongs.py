"""
File:         find_diphthongs.py
Author:       Vu Nguyen
Date:         10/9/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs extract two vowels that composite
              within an inputted string and displayed it in
              the terminal.
"""
if __name__ == "__main__":
    diphthong_string = input("Enter a string with a lot of diphthongs: ").strip()
    vowel_list = ['a', 'e', 'i', 'u', 'o', 'y']

    diphthong_word_list = diphthong_string.split()
    first_vowel = ''
    second_vowel = ''
    diphthong_vowels = ''
    diphthong_vowels_list = []

    # This loop add vowel into diphthong_vowel
    for word in diphthong_word_list:
        for char in word:

            # Check if the letter is a vowel
            if char in vowel_list:

                # If there is already a vowel in the first vowel add it to the second vowel
                if first_vowel:
                    second_vowel += char
                else:
                    first_vowel += char

            # Check for consonants
            else:
                if first_vowel:
                    first_vowel = ''

            # Check if there is already something in the first/second vowel
            if first_vowel and second_vowel:
                diphthong_vowels += first_vowel + second_vowel
                first_vowel = ''
                second_vowel = ''

            # Adding the diphthong vowels into a list for easier count.
            if diphthong_vowels:
                diphthong_vowels_list.append(diphthong_vowels)
                diphthong_vowels = ''

    # This condition check for any d_vowels within the list.
    diphthong_count = 0
    if not diphthong_vowels_list:
        print("The diphthong count is", diphthong_count)
    else:

        # This loop print out the d_vowels and display the number of count.
        for vowels in diphthong_vowels_list:
            diphthong_count += 1
            print(vowels)
        print("The diphthong count is", diphthong_count)








