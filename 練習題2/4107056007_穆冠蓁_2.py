import pandas as pd
df = pd.read_csv("Titanic.csv")
df = df.replace({"Sex" :    {"male":1, "female":0} })
print(df.corr())
corr_matrix = df.corr()
corr_matrix.style.background_gradient(cmap = 'coolwarm')
