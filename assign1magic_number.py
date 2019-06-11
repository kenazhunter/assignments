import random
rounds = 0
print("Hello, what is your name")
name = input()

number = random.randint(0, 10)
print("{}".format(name), "Take a guess to win.")

while rounds < 6:
    print("Take a guess. ")
    magic = input()
    magic = int(magic)

    rounds = rounds + 1
    if magic == number:
        break
if magic == number:
    rounds = str(rounds)
    print("Well done {}".format(name), "You guessed the number in {}".format(rounds), "rounds.")
if magic != number:
    number = str(number)
    print("Unlucky, the number was {}".format(number))