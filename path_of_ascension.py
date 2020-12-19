"""
File:         path_of_ascension.py
Author:       Vu Nguyen
Date:         10/9/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  Trying to find the longest ascending sequence
              in a random generate list, based on the user
              length, and display the max ascending length

"""
import sys
from random import seed, randint

if len(sys.argv) >= 2:
    seed(sys.argv[1])


if __name__ == "__main__":

    ascension_list = []

    length = int(input("What length of sequence do you want ot input? (0-1000) "))

    if (length >= 0) and (length <= 1000):

        # Adding random num between 0 and 100 into the ascension_list based on the length
        for i in range(length):
            ascension_list.append(randint(0, 100))

        print(ascension_list)

        check_num = -1
        max_length = 1
        check_count = 0
        number_of_sequence = 0

        for ran_num in ascension_list:

            # Compare two number to see if it increasing or decreasing.
            if ran_num > check_num:
                check_num = ran_num
                check_count += 1

            else:
                check_num = ran_num

                # Check to see if the sequence has more than one number.
                if check_count > max_length:
                    max_length = check_count
                    check_count = 1

                # This statements check if the there are other sequence with the same max length
                elif (check_count == max_length) and (max_length > 1):
                    number_of_sequence += 1
                    check_count = 1

        if check_count > max_length:
            print("The max ascending length is", check_count)
        else:
            print("The max ascending length is", max_length)

        """ 
        # This code display the number of sequence that has the same max ascending length
        if number_of_sequence > 0:
            print("The length has", number_of_sequence, "of the same sequence.")
        """

