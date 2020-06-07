print("Hello!")
name = input("What´s you name?")
print("Let´s play a game, " + name + "!")
secret = 13
guess = input("Guess the secret number:")
if guess == "13":
    print("Congratulations!!! " + name + ", you are a winner!")
elif guess == "12":
    print("Sorry, that´s wrong. But you are very close!")
elif guess == "14":
    print("Sorry, that´s wrong. But you are very close!")
else:
    print("Sorry, that´s wrong. Try again, " + name + "!")
