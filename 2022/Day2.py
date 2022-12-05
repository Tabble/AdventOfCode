# Enemy
# A = Rock
# B = Paper
# C = Scissors

# Me
# X = Rock
# Y = Paper
# Z = Scissors

# Rock > Scissors
# Scissors > Paper
# Paper > Rock

# total score is the sum of your scores for each round
# score for the round is the score for the shape you selected
# Rock = 1
# Paper = 2
# Scissor = 3
# plus the outcome of the round
# Lost = 0
# Draw = 3
# Win = 6
from enum import Enum

class Score_Round(Enum):
    Lost = 0
    Draw = 3
    Win = 6

class Shape(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

enemy_guide = {"A" : Shape.Rock, "B" : Shape.Paper, "C" : Shape.Scissor}
player_guide = {"X" : Shape.Rock, "Y" : Shape.Paper, "Z" : Shape.Scissor}
player_outcome = {"X" : Score_Round.Lost, "Y" : Score_Round.Draw, "Z" : Score_Round.Win}

def calculate_outcome_player(enemyShape, playerShape):
    if(enemyShape == Shape.Rock):
        if(playerShape == Shape.Rock):
            return Score_Round.Draw
        if(playerShape == Shape.Paper):
            return Score_Round.Win
        if(playerShape == Shape.Scissor):
            return Score_Round.Lost
    elif(enemyShape == Shape.Paper):
        if(playerShape == Shape.Rock):
            return Score_Round.Lost
        if(playerShape == Shape.Paper):
            return Score_Round.Draw
        if(playerShape == Shape.Scissor):
            return Score_Round.Win
    elif(enemyShape == Shape.Scissor):
        if(playerShape == Shape.Rock):
            return Score_Round.Win
        if(playerShape == Shape.Paper):
            return Score_Round.Lost
        if(playerShape == Shape.Scissor):
            return Score_Round.Draw

def calculate_shape_player(enemyShape, predictedOutcome):
    if(enemyShape == Shape.Rock):
        if(predictedOutcome == Score_Round.Win):
            return Shape.Paper
        if(predictedOutcome == Score_Round.Lost):
            return Shape.Scissor
        if(predictedOutcome == Score_Round.Draw):
            return Shape.Rock
    elif(enemyShape == Shape.Paper):
        if(predictedOutcome == Score_Round.Win):
            return Shape.Scissor
        if(predictedOutcome == Score_Round.Lost):
            return Shape.Rock
        if(predictedOutcome == Score_Round.Draw):
            return Shape.Paper
    elif(enemyShape == Shape.Scissor):
        if(predictedOutcome == Score_Round.Win):
            return Shape.Rock
        if(predictedOutcome == Score_Round.Lost):
            return Shape.Paper
        if(predictedOutcome == Score_Round.Draw):
            return Shape.Scissor

raw_data = []
with open("Day2Encripted.txt", mode="r") as file:
    raw_data = file.readlines()

# part one calculate score
sum = 0
round = 0
for item in raw_data:
    enemy = item[0]
    player = item[2]
    enemyshape = enemy_guide[enemy]
    playershape = player_guide[player]

    outcome = calculate_outcome_player(enemyshape, playershape)
    round = outcome.value + playershape.value
    sum += round

print("total sum:" + str(sum))

sum_outcome = 0
for item in raw_data:
    enemy = item[0]
    player = item[2]
    enemyshape = enemy_guide[enemy]
    pred_outcome = player_outcome[player]
    playershape = calculate_shape_player(enemyshape, pred_outcome)

    round = pred_outcome.value + playershape.value
    sum_outcome += round

print("total with predicted outcome:" + str(sum_outcome))