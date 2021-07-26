import random

def game():
    num = random.randint(1, 100)
    guess = None
    restart = None

    while guess != num:
            guess = input("Guess number between 1-100: ")
            guess = int(guess)

            if guess > num:
                print("The number is too high")
            elif guess < num:
                print("The number is too low")
            else:
                print("Congratulation! The number is correct!")

    while restart != "Y" and restart != "N":
        restart = input("Play again? Y/N: ")

        if restart == "Y":
            print("Game restart. Good Luck!")
            game()
        elif restart == "N":
            print("Thank you for playing.")

game()