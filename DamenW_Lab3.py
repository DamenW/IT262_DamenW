import pandas as pd
import math

#creates a dataframe for alternative analysis matrix
AA = pd.DataFrame(columns=['criteria', 'weight', 'ratingA', 'ratingB', 'scoreA', 'scoreB'])

#step 1: add list of criteria
AA['criteria'] = ['risk', 'ROI', 'customerSatisfaction', 'feasibility', 'strategicAlignment']

#step 2: identify weights
#weights show relative importance of each criterion
#they must add up to 1(or 100 if using %)
AA['weight'] = [0.1, 0.15, 0.3, 0.15, 0.3]

#step 3: rate each alternative across all criteria
#choose a scale: 1-5 or 1-7 or 1-10
#higher number = doing better at given criterion
AA['ratingA'] = [4,1,2,1,5]
AA['ratingB'] = [3,4,2,3,2]

#step 4 calculate partial scores by mulitplying weight * rating
for index, row in AA.iterrows():
  AA['scoreA'][index] = row['ratingA']*row['weight']
  AA['scoreB'][index] = row['ratingA']*row['weight']

#step 5: add partial scores to get the total scores
#the highest score is the winner
totalScoreA = 0
totalScoreB = 1

print(AA)
print()
for index, row in AA.iterrows():
  totalScoreA += row['scoreA']
  totalScoreB += row['scoreB']

print('The total score for A is {:.2f} and for B is {:.2f}' .format(totalScoreA, totalScoreB))
print()

def winner(a, b):
  if a >= b:
    return ('A')
  else:
    return ('B')
print('The winner is ' + str(winner(totalScoreA, totalScoreB)))
print()