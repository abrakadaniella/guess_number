import random
import pyinputplus as pyip


def further_action():
    again = pyip.inputMenu(choices=['Yes', 'No'], numbered=True)
    if again == 'Yes':
        game()
    else:
        print("Bye!")


def game():
    number = random.randint(0, 100)
    print("I have generated some integer between 0 and 100. Can you guess it?")
    guess = pyip.inputInt(prompt="Your guess is:\n", min=0, max=100)
    counter = 1
    while counter != 3:
        if guess == number:
            break
        elif number > guess:
            guess = pyip.inputInt(prompt="Your number is lower than my number. What is your new guess?\n", min=0,
                                  max=100)
            counter += 1
        else:
            guess = pyip.inputInt("Your number is higher than my number. What is your new guess?\n", min=0, max=100)
            counter += 1
    if guess != number:
        print("You are out of attempts! My number was {}. Do you want to play again?".format(number))
    else:
        print("You are right! This is {}. Do you want to play again?".format(number))
    further_action()


game()
