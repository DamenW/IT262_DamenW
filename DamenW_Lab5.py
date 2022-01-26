import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#upload the HelpDesk.csv to your GoogleDrive
df=pd.read_csv("/content/drive/MyDrive/IT262 Project Management/HelpDesk.csv")

#set this column as index to use as plot labels
df.index = df['reason']
#descending sort
df = df.sort_values(by='frequency', ascending = False)

#cumulative percentage column is created using cumum function
df['cumulativePercentage'] = df["frequency"].cumsum()/df["frequency"].sum()*100

#making sure only 2 decimal points are shown
df["cumulativePercentage"] = df["cumulativePercentage"].apply(lambda x: round(x, 2))
print(df)

fig, ax = plt.subplots()
ax.bar(df.index, df["frequency"], color="C5")

#show labels diagonally
ax.set_xticklabels(df['reason'], rotation=45)

#ax2 and ax1 will be shown at the same time with twinx
ax2 = ax.twinx()

ax2.plot(df.index, df["cumulativePercentage"], color="C6", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C2")
ax2.tick_params(axis="y", colors="C3")

plt.show()
