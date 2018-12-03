import random


n = random.randint(1, 99)
GUESS_PHRASE = "Enter an integer from 1 to 99 (0 to quit): "
ATTEMPTS = 0

guess = int(raw_input(GUESS_PHRASE))

while guess != 0:
    print
    ATTEMPTS += 1
    if guess != n:
        if guess >=1 and guess <= 99:
            print "guess is low" if guess < n else "guess is high"
        guess = int(raw_input(GUESS_PHRASE))
    else:
        print "you guessed {} in {} attempts".format(n, ATTEMPTS)
        break
print "bye"
