import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Abhishek\Downloads\Popular_Baby_Names.csv")

df.plot.bar()
plt.show()
