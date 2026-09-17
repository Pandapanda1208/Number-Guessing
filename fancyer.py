import os
import random

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

green = '\033[32m'
yellow = '\033[33m'
reset = '\033[0m'

guesses = []
g = 0

num = random.randint(1, 100)

run = True

input('Guess the number 1 through 100, when it shows your guesses, if the number is green, it is too high, if it is yellow, it is too low.')

while run:
  clear()
  print('Guesses: ', end='')
  print(', '.join(guesses))
  guess = int(input('What is your guess? '))
  g += 1
  if guess == num:
    break
  elif guess > num:
    input('Your Guess was to high!')
    guesses.append(f'{green}{guess}{reset}')
  elif guess < num:
    input('Your Guess was too low!')
    guesses.append(f'{yellow}{guess}{reset}')

clear()
input(f'You succesfully guesses the number {num}, in {g} tries!')
