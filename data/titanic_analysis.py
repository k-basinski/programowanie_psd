# %%
import pandas as pd

df = pd.read_csv('titanic.csv')

df.info()

# %%
df
# %%
df.Pclass.value_counts()
# %%
df['survived_r'] = df['Survived'].replace({0: 'no', 1: 'yes'})
df.groupby('survived_r').Age.mean()
# %%
import pingouin as png

survived = df[df.survived_r == 'yes'].Age
not_survived = df[df.survived_r == 'no'].Age
png.ttest(survived, not_survived)
# %%

# chisq
expected, observed, stats = png.chi2_independence(df, x='survived_r', y='Sex')
print(expected)
print(observed)
print(stats.round(3))
# %%
png.corr(df.Fare, df.Age)
# %%


import seaborn as sns
sns.relplot(x = 'Age', y='Fare', data=df)
# %%
sns.catplot(x='Survived', y='Age', kind='violin', data=df)
# %%

sns.catplot(x='Pclass', y='Fare', hue='Sex', data=df, kind='box')

# %%
