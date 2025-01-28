import random
random_num = random.randrange(1, 10)

while True:
    num = int(input("Enter a number from 1 to 10: "))
    if num == random_num:
        print("Congratulations, you guessed correctly!")
        break  # To stop the loop once the correct guess is made
    else:
        print("Sorry, please try again.")
