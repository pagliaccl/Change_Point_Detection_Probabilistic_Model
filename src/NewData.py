import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('/Users/Pagliacci/Desktop/ECE 443/finalProject/data/ImportValues')['Value']
# data.hist()
firstDiff=data.values[1:]-data.values[:-1]

outdata=pd.DataFrame({'Value':firstDiff})
outdata.plot(kind='line')
outdata.hist()

outdata.to_csv('/Users/Pagliacci/Desktop/ECE 443/finalProject/data/ImportValuesFD.csv')
plt.show()