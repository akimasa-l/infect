import pandas
df=pandas.read_csv("data.csv")
df.T.to_csv("data_t.csv")