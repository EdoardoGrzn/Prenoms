import sqlite3 
import pandas as pd #type: ignore

df = pd.read_csv("data/prenoms-2025-nat.csv", sep=";")
#df = df[["periode" != "XXXX"]]
df["periode"] = df["periode"].astype(int)
df = df[["prenom", "periode", "valeur"]]

def get_conn():
    return sqlite3.connect("data/prenom.db")

conn = get_conn()
df.to_sql("prenom", conn, if_exists="replace", index=False)
conn.close()



