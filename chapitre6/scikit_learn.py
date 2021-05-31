import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
fichier= pd.read_csv("../traitement_donnees/melb_data.csv")

donnes_sans_vide=fichier.dropna()
#donnes_sans_vide.info()
print(donnes_sans_vide[:10])
#print(donnes_sans_vide)
dict_label_encode={}
for col in donnes_sans_vide.columns:
    if donnes_sans_vide[col].dtype==object:
        dict_label_encode[col]= LabelEncoder()
        donnes_sans_vide[col]=dict_label_encode[col].fit_transform(donnes_sans_vide[col])

#◙donnes_sans_vide.info() 
print(donnes_sans_vide[:10])