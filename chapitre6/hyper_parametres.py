import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

fichier= pd.read_csv("../traitement_donnees/melb_data.csv")

donnes_sans_vide=fichier.dropna()
# transferer les donnes object aux donnees numeriques avec la fonction label encoder 
dict_label_encode={}
for col in donnes_sans_vide.columns:
    if donnes_sans_vide[col].dtype==object:
        dict_label_encode[col]= LabelEncoder()
        donnes_sans_vide[col]=dict_label_encode[col].fit_transform(donnes_sans_vide[col])

x=donnes_sans_vide.drop("Price",axis=1)
y=donnes_sans_vide["Price"]
# on sépare les échantillons d'apprentissage 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# on utilise l'algorithme de k plus proche voisin

modele_rf=RandomForestClassifier()


modele_rf.fit(x_train,y_train)
y_predict_rf=modele_rf.predict(x_test)

print(y_predict_rf)
#dic_param={"n_estimator":[10,100,1000], "max":[5,7,9]}
#modele_grid_rf= GridSearchCV(modele_rf,dic_param,scoring="roc_auc", cv=5)