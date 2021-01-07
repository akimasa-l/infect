import pandas
df=pandas.read_csv("data.csv")
df.cumsum().T.to_csv("d.csv")