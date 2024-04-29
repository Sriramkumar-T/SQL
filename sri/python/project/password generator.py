import random
import string

def password_gen(min_length,numbers=True,special_charc=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    character= letters
    if numbers:
        character += digits
    if special_charc:
        character += special
    pwd=""
    meet_criteria=False
    has_number=False
    has_special=False

    while not meet_criteria or len(pwd)<min_length:
        new_char=random.choice(character)
        pwd+=new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True

        meet_criteria=True
        if numbers:
            meet_criteria=has_number
        if special_charc:
            meet_criteria=meet_criteria and has_special
    return pwd
min_length=int(input("enter the minimum length:"))
has_number=input("do you want have numbers? (y/n):").lower()=="y"
has_special=input("do you want have special characters? (y/n):").lower()=="y"
pwd=password_gen(min_length,has_number,has_special)
print("the generated password is:",pwd)
