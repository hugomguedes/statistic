#%% 
import pandas as pd

df = pd.read_csv ("data/points_tmw.csv")

minimo = df["qtdPontos"].min()
media = df["qtdPontos"].mean()
quartil_1 = df["qtdPontos"].quantile(0.25)
mediana = df["qtdPontos"].median()
quartil_3= df["qtdPontos"].quantile(0.75)
maximo = df["qtdPontos"].max()
variancia = df["qtdPontos"].var()
desvioPadrao = df["qtdPontos"].std()
amplitude = df["qtdPontos"].max() - df["qtdPontos"].min()
print(f"minimo: {minimo}")
print(f"Média: {media}")
print(f"Primeiro quartil: {quartil_1}")
print(f"Mediana: {mediana}")
print(f"Terceiro quartil: {quartil_3}")
print(f"Maximo: {maximo}")
print(f"Variancia: {variancia:,.2f}")
print(f"Desvio padrao: {desvioPadrao:,.2f}")
print (f"Amplitude: {amplitude}")
df["qtdPontos"].describe()



usuarios = df.groupby(["idUsuario"]).agg({
    "idTransacao": "count",
    "qtdPontos": "sum"
}).reset_index()

usuarios[["idTransacao", "qtdPontos"]].describe()