import random
word_list = ['apple', 'strawberry', 'peach', 'orange', 'watermelon']
print(word_list)

word = random.choice(word_list)
print(word)

guess = (input("Please input a guess: "))

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
