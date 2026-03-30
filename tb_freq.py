#%%
import pandas as pd
import sqlalchemy

df = pd.read_csv ("data/points_tmw.csv")
df.head()

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")
df.to_sql("points", engine, if_exists="replace", index=False)
#%%

freq_produto = df.groupby(by="descProduto")[["idTransacao"]].count()

freq_produto["freq. Abs. Acum."] = freq_produto["idTransacao"].cumsum()
freq_produto["freq. rel"]=freq_produto["idTransacao"] / freq_produto["idTransacao"].sum() 
freq_produto["freq. rel. Acum."]=freq_produto["freq. rel"].cumsum()
freq_produto

# %%

freq_cat = df.groupby(by="descCategoriaProduto")[["idTransacao"]].count().rename(columns={"idTransacao":"Freq. Abs"})
freq_cat["Freq. Abs. Acum"] = freq_cat["Freq. Abs"].cumsum()
freq_cat["Freq. Rel"] = freq_cat["Freq. Abs"] / freq_cat["Freq. Abs"].sum()
freq_cat

freq_cat["Freq. rel. Acum"] = freq_cat["Freq. Rel"].cumsum()
freq_cat