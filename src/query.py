import sqlite3
import pandas as pd
from build_db import get_conn

def prenoms(prenom) :
    conn = get_conn()
    df = pd.read_sql( 
        " SELECT periode, SUM(valeur) FROM prenom" \
        " WHERE prenom = ?" \
        "GROUP BY periode ORDER BY periode", conn, params=(prenom))
    conn.close
    return df

def tous_prenoms():
    conn = get_conn()
    tuples = conn.execute( " SELECT DISTINCT prenom from prenom ORDER BY prenom" ).fetchall()
    conn.close()
    prenoms = []
    for r in tuples :
        prenom.append(r[0])
    return prenoms
