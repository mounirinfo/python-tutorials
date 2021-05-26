import pandas as pd
data_frame_melb=pd.read_csv("melb_data.csv")
#print(data_frame_melb)
data_frame_melb.info()

data_frame_sans_case_vide=data_frame_melb.dropna() 
# j'ai opté pour la suppression des lignes des données manquantes, 
#qui sont a peu pres d'une moitié des données brutes
# je ne peux pas appliquer une methode pour prédire la valeur de chaque 
#colonne manquante neanmoins on peut  proceder  a la suppression
# des colonnes qui ont beaucoup de valeurs manquantes.
# le choix de la methode pour le traitmeent des donnees dépond de l'objectif métier  
print (data_frame_sans_case_vide.info())
data_frame_sans_case_vide['Date']=pd.to_datetime(data_frame_sans_case_vide['Date'])

# L'utilisation des prefixes permet de savoir exactement l'origine de la colonne 
#autrement dit la nouvelle colonne ajoutee elle etait reellement la valeur de quelle variable   
data_exp=pd.get_dummies(data_frame_sans_case_vide, prefix = ['Suburb','Address','Type','Method','sellerG','CouncilArea','Regionname'], columns=['Suburb','Address','Type','Method','SellerG','CouncilArea','Regionname'])
print(data_exp)
