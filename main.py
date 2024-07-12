from game_data import data
import os
import random

is_playing = True
score = 0

print("Welcome to US States: Higher or Lower Game.")

state_one = data[random.randint(0, len(data) - 1)]

while(is_playing == True):
  state_two = data[random.randint(0, len(data) - 1)]

  while(state_one == state_two):
    state_two = data[random.randint(0, len(data) - 1)]

  print(f"Compare A. {state_one['state']} vs B. {state_two['state']}.")
  guess = input("Which state has a higher population? Choose 'A' or 'B': ").upper()

  if(state_one['population'] > state_two['population'] and guess == 'A'):
    os.system('clear')
    print(f'{state_one["state"]} population: {state_one["population"]}')
    print(f'{state_two["state"]} population: {state_two["population"]}')
    score += 1
    print(f'Correct! Your current score is {score}.')
  elif(state_one['population'] < state_two['population'] and guess == 'B'):
    os.system('clear')
    print(f'{state_one["state"]} population: {state_one["population"]}')
    print(f'{state_two["state"]} population: {state_two["population"]}')
    score += 1
    state_one = state_two
    print(f'Correct! Your current score is {score}.')
  elif(state_one['population'] < state_two['population'] and guess == 'A'):
    os.system('clear')
    print(f'{state_one["state"]} population: {state_one["population"]}')
    print(f'{state_two["state"]} population: {state_two["population"]}')
    print(f'Incorrect! Your final score is {score}.')
    is_playing = False
  elif(state_one['population'] < state_two['population'] and guess == 'A'):
    os.system('clear')
    print(f'{state_one["state"]} population: {state_one["population"]}')
    print(f'{state_two["state"]} population: {state_two["population"]}')
    print(f'Incorrect! Your final score is {score}.')
    is_playing = False
  else:
    os.system('clear')
    print(f'{state_one["state"]} population: {state_one["population"]}')
    print(f'{state_two["state"]} population: {state_two["population"]}')
    print(f'Incorrect input. Your final score is {score}.')
    is_playing = False