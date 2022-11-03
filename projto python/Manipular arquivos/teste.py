from turtle import color, title
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

planilha = input("Digite o nome da plailha ")
arquivo = planilha+".xlsx"

print(arquivo)

df = pd.read_excel(arquivo)
print(arquivo)
gf = df.loc[:,"LojaID":"Qtde"]
print(gf)

# gf.plot(kind ='bar')
# plt.show()

print(gf)

nc = df["LojaID"].value_counts(ascending=False).sum
print(nc)

# nc.plot(kind = 'bar')
# plt.show


pi = df.groupby(df["Data"].dt.year)["Qtde"].sum().plot.pie();
plt.legend()
plt.show()

print(df)

# marco = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# print(marco)



