#Making Blackjack
import random

print("Would you like to be dealt?")
game_start_input = input("'y' or 'n'")

game_start = False
if game_start_input == 'y':
  game_start = True
while game_start:
  print("Game runs")
  game_start = False
