import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

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
# on utilise un modele de regression de ridge 
modele_ridge= Ridge()
modele_ridge.fit(x_train,y_train)
#afficher les coefficients du modele 
modele_ridge.coef_
y_predict=modele_ridge.predict(x_test)
# on utilise l'algorithme de k plus proche voisin

modele_rf=RandomForestClassifier()
modele_knn= KNeighborsClassifier()

modele_rf.fit(x_train,y_train)
modele_knn.fit(x_train,y_train)

y_predict_rf=modele_rf.predict(x_test)
y_predict_knn= modele_knn.predict(x_test)
print(y_predict,y_predict_rf, y_predict_knn)