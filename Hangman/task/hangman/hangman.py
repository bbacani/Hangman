# Write your code here
import random

listOfWords = ['python', 'java', 'kotlin', 'javascript']
usedLetters = []
lives = 8

print("H A N G M A N")

menu = ''
while menu != "exit":
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu != "play":
        continue

    word = random.choice(listOfWords)
    hint = '-' * len(word)

    while lives > 0:
        print('\n' + hint)

        if hint == word:
            print("You guessed the word!")
            print("You survived!\n")
            break

        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if letter.isupper() or not letter.isalpha():
            print("Please enter a lowercase English letter")
            continue
        if letter in usedLetters:
            print("You've already guessed this letter")
            continue

        usedLetters.append(letter)

        counter = 0
        appeared = False
        for char in word:
            if char == letter:
                hint = hint[:counter] + hint[counter:].replace('-', char, 1)
                appeared = True
            counter += 1

        if appeared:
            continue

        print("That letter doesn't appear in the word")
        lives -= 1
    else:
        print("You lost!\n")
