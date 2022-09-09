#DIGITAL ROOT CALCULATOR
"""
This code is based on the Digital Root
from the video game "Zero Escape."

When a number is given, it'll generate a digital root.

RULES:
    - If the number has 1 digit, it'll return that number.
    - If the number has more than 1 digit,
      the following should happen:
         > add each digit to each to create new number
         > repeat step until you get 1 digit
"""

def add_digits(N):
    """(string) -> string

    Given a number, return the sum of each digit.
    """
    total = 0
    for digit in N:
        total = total + int(digit)
    return str(total)
    

def found_dr(N):
    """(string) -> boolean

    Return True if N only has 1 digit.
    """
    return len(N)==1


def calculate_dr(N):
    """(string) -> string

    Uses add_digit method to find digital root.
    """
    while found_dr(N)==False:
        ans = add_digits(N)
        N = ans
        print(ans)
    return ans
    

if __name__=="__main__":
    #number = input("Enter a number: ")
    while True:
        number = input("Enter a number: ")
        ans = calculate_dr(number)
        print("Digital Root:", ans)
        redo = input("Do you want to find another digital root? [Y]/[N]")
        if redo=="n" or redo=="N":
            break
    print("Closing...")

