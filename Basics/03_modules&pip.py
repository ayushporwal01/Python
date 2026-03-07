#A module is a python file containing reusable code.
#pip is a package manager for Python used to install Libraries.
#Libraries are collection of modules.

import pandas as pd

df = pd.read_csv("products-100.csv")
print(df)