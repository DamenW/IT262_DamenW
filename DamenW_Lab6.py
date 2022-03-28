import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive/')

%cd /content/drive/My Drive/

myData = pd.read_csv('/content/drive/MyDrive/BDU.csv')

myData.shape
myData.head(2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 2))

ax1.set_xlabel('Days')
ax2.set_xlabel('Days')

ax1.plot(myData.Cideal, color = 'blue', label = 'Work Completed - Ideal')
ax3 = ax1.twinx()
ax3.plot(myData.Cactual, color = 'green', label = 'Work Completed - Actual')

ax2.plot(myData.Lideal, color = 'blue', label = 'Work to be Done - Ideal')
ax4 = ax2.twinx()
ax4.plot(myData.Lactual, color = 'green', label = 'Work to be Done - Actual')
ax1.set_title('Burn Up')
ax2.set_title('Burn Down')

h1, l1 = ax1.get_legend_handles_labels()
h3, l3 = ax3.get_legend_handles_labels()
ax3.legend(h1+h3, l1+l3, loc=2)
h2, l2 = ax2.get_legend_handles_labels()
h4, l4 = ax4.get_legend_handles_labels()
ax4.legend(h1+h3, l1+l3, loc=2)

plt.show()
