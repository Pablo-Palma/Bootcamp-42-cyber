import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")

secret_number = random.randint(1, 99)
attempts = 0

while True:
    guess = input("What's your guess between 1 and 99?\n")
    if guess == "exit":
        print("Goodbye!")
        break
    try:
        guess = int(guess)
        if guess < 1 or guess > 99:
            raise ValueError
    except ValueError:
        print("The number should be between 1 and 99.")
        continue
    attempts += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        if secret_number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if attempts == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print(f"You won in {attempts} attempts!")
        break

