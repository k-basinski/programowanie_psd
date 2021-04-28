# %%
import pandas as pd

df = pd.read_csv('titanic.csv')

df.info()

# %%
df.Pclass.value_counts()
# %%
