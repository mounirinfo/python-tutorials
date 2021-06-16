'''
import psycopg2
import pandas as pd
conn = psycopg2.connect(
            user = "postgres",
            password = "postgres",
            host = "localhost",
            port = "5432",
            database = "test"
)
sql= "select * from ventes"
cur.execute(sql)

'''

import psycopg2
import pandas as pd

try:
    conn = psycopg2.connect(
          user = "postgres",
          password = "postgres",
          host = "localhost",
          port = "5432",
          database = "test"
    )
    
    cur = conn.cursor()

    # Afficher la version de PostgreSQL 
    cur.execute("select * from ventes")
    version = cur.fetchall()
    column_names = ["id_client", "quantite", "prix_unitaire", "identifiant_prod"]
    df = pd.DataFrame(version,columns=column_names)
    print("la table sql : ","\n", df,"\n")
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
