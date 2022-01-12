from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import math

dataT = pd.read_csv("/content/drive/MyDrive/Copy of 262-CBA.csv")
print(dataT)

# set your own discount rate
discountRate = 0.05

#calculate the compund discount over the years
#initialize a list of 4 elements - one for each year, 0 to 3
discountFactor = [0,0,0,0]

for year in dataT['years']:
  discountFactor[year] = 1/math.pow(1 + discountRate, year)

dataT['discountFactor'] = [round(num, 2) for num in discountFactor]
print(dataT)

#calculate Net benefit/cost for each year
#sum of all benefits and cost for each year : op cost + dev cost + benefit
#initlize list of 4 items
NetBC = [0,0,0,0]
for year in dataT['years']: 
  NetBC[year] = dataT['developmentCost'][year] + dataT['operationalCost'][year] + dataT['valueOfBenefits'][year]

dataT['NetBC'] = NetBC
print(dataT)

#calculate net present value

NPV = [0,0,0,0]

for year in dataT['years']:
  NPV[year] = dataT['NetBC'][year] * dataT['discountFactor'][year]

dataT['NPV'] = [round(num, 2) for num in NPV]
print(dataT)