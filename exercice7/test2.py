import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import io

try:
    
     # connexion a la base de donnée
     
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/test')
    connexion=engine.connect();
    

    df = pd.read_sql(" select * from ventes", connexion);
    print (df)
    
   
    #calculer la moyenne des prix unitaire 
    moyenne_prix_unitaire=df["prix_unitaire"].mean()
    print("la moyenne des prix unitaire est : ", moyenne_prix_unitaire)
    #calculer le chiffre d'affaire
    df['chiffre_daffaires']=df.quantite*df.prix_unitaire
    ca_global=df['chiffre_daffaires'].sum()
    print("Le chiffre daffaires realise est: ", ca_global)
    #fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    print("La connexion PostgreSQL est fermée")
    
except (Exception, psycopg2.Error) as error :
    print ("Erreur lors de la connexion à PostgreSQL", error)
    
