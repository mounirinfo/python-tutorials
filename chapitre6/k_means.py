import pandas as pd

import datetime

def calcul_distance_deux_points (ligne1, ligne2):
    print('je calcule la distance ')
    return 1

actuel_year = datetime.datetime.now().year

df_donnees_vente= pd.read_csv("../traitement_donnees/melb_data.csv")
#df_donnees_vente.info()

#traitement de donnees
df_donnees_essentielle=df_donnees_vente[['Price','Landsize','YearBuilt']]

# calcul du nombre de valeur null dans le dataframe 
df_donnees_essentielle.isna().sum()

df_sans_donnees_vide= df_donnees_essentielle.dropna()

# le choix du k
k= input ('entrer le nombre k qui correspond axu clusters ')
 
df_sans_donnees_vide['AgeMaison']=actuel_year-df_sans_donnees_vide['YearBuilt']

# la normalisation des données
df_sans_donnees_vide['Price_normalise']=(df_sans_donnees_vide['Price']-df_sans_donnees_vide['Price'].min())/(df_sans_donnees_vide['Price'].max()-df_sans_donnees_vide['Price'].min())
df_sans_donnees_vide['Landsize_normalise']=(df_sans_donnees_vide['Landsize']-df_sans_donnees_vide['Landsize'].min())/(df_sans_donnees_vide['Landsize'].max()-df_sans_donnees_vide['Landsize'].min())
df_sans_donnees_vide['YearBuilt_normalise']=(df_sans_donnees_vide['YearBuilt']-df_sans_donnees_vide['YearBuilt'].min())/(df_sans_donnees_vide['YearBuilt'].max()-df_sans_donnees_vide['YearBuilt'].min())


# 1 choisir aléatoirement les k lignes dans le dataframe
df_k_donnees_aleatoire = df_sans_donnees_vide.sample(int(k))

# 2 distance entre chaque centre et le tablea précédent
# pour chaque ligne de dataframe des donnees aléatoire 
# pour chaque ligne de dataframe des donnees 
#on calcule la distance entre les deux point 
for index,row in df_k_donnees_aleatoire.iterrows():
    for index2,row2 in df_sans_donnees_vide.iterrows():
        calcul_distance_deux_points(row,row2)
#3 affecter chaque point au cluster où la ditance est proche
#4 calculer le centre de gravité de chaque cluster
#5 vérifier si au moins un centre bouge
# indexer les centres :
df_k_donnees_aleatoire.reset_index(inplace=True)
centres_k = df_k_donnees_aleatoire[['Price_normalise','Landsize_normalise','YearBuilt_normalise']]
dict_centres_k=centres_k.T







