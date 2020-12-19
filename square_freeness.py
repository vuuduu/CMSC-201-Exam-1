"""
File:         square_freeness.py
Author:       Vu Nguyen
Date:         10/9/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs figure out a useless attribute
              of a given number. That useless attribute is
              finding a first factor that can be square.

"""

if __name__ == "__main__":
    number_x = int(input("Tell me a number x: ").strip())
    divisor = 2
    is_Square_Freeness = True

    # This condition check for 0 and negative number
    if number_x <= 0:
        print('You cannot calculate the square freeness of', number_x)
    else:

        while is_Square_Freeness and (divisor < number_x):

            # This condition check for the factor of number_x
            if number_x % divisor == 0:

                # This condition checks to see if the factor can be square root.
                if (divisor ** .5) % 1 == 0:
                    is_Square_Freeness = False
                else:
                    divisor += 1
            else:
                divisor += 1

        # This condition checks for factor divisor and square freeness
        if is_Square_Freeness:
            print(number_x, "is square free")
        else:
            print(number_x, "is not square free because", int(divisor ** .5), "squared divides it")


