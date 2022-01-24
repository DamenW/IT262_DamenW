import seaborn as sns
import pandas as pd
import numpy as np

#create a dataframe (data table)
df = pd.DataFrame(columns = ['risk', 'likelihood', 'impact', 'score'])

#identify list of uncertainties
df['risk'] = ['users', 'team', 'budget', 'security']

#estimate the likelihood of happening
df['likelihood'] = [0.2, 0.3, 0.1, 0.5]

#assess the severity of impact if the uncertainty happens (pick a scale)
df['score'] = df['impact']*df['likelihood']
df['impact'] = [1, 2, 7, 10]

#calculate scores
df['score'] = df['impact']*df['likelihood']

#create the heatmap
scoresPivot = df.pivot('impact', 'likelihood', 'score')
print(scoresPivot)

#use when using array, replaces Na values with empty strings
#labelsPivot = df.pivot('impact', 'likelihood', 'risk')
#print(labelsPivot)
#test replacement
#print(labelsPivot)

#replaces no labels with empty strings
labelsPivot.fillna('', inplace=True)

#simple heatmap
p1 = sns.heatmap(scoresPivot, cmap="Spectral", annot=labelsPivot, fmt='')
