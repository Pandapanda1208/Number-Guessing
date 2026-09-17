import random

num = random.randint(1, 10)

run = True

while run:
  guess = int(input('What is your guess? '))
  if guess == num:
    run = False
  if guess > num:
    print('That was too high.')
  if guess < num:
    print('That was too low.')

print('You guessed it correctly')
input()
