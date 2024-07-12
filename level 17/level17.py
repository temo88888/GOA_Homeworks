import random

def guess_number():
    correct_number = random.randint(1, 1000)
    user_input = int(input("შემოიტანეთ რიცხვი 1-დან 1000-მდე: "))

    if user_input == correct_number:
        print("სწორია!")
    else:
        print("არასწორია!")

guess_number()