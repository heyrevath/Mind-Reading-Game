import numpy as np
import random

last_1 = 0
last_2 = 0

inputs = np.zeros((2,2,2), dtype=int)

scores = [0,0]
def update_scores(player_input, predicted):
    if player_input == predicted:
        scores[0] = scores[0]+1
        print("Player score = ",scores[1])
        print("Computer score = ",scores[0]) 
    else:
        scores[1] = scores[1]+1
        print("Computer score = ",scores[0])   
        print("Player score = ",scores[1])

def reset():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                inputs[i][j][k] = 0
    for i in range(len(scores)):
        scores[i] = 0

def prediction():
  if inputs[last_2][last_1][1] == 1: 
    predict = inputs[last_2][last_1][0]    
  else:
    predict = random.randint(0, 1)  
  return predict

def update_inputs(current):
  global last_1,last_2
  
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1 
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0 
    inputs[last_2][last_1][0] = current
 
  last_2 = last_1 
  last_1 = current

def gameplay():
    reset()
    print(inputs,scores, sep= " ")
    valid_entries = ["0","1"]
    while True:
        predict = prediction()
        user_input = input("Enter either 0 or 1: ")
        while user_input not in valid_entries:
            print("Invalid Input")
            user_input = input("Enter either 0 or 1: ")
        user_input = int(user_input)
        update_inputs(user_input)
        update_scores(user_input, predict)
        if scores[0] == 20:
            print("Bad Luck Computer Wins!")
            break
        elif scores[1] == 20:
            print("Congrats You Won!")
            break


gameplay()
