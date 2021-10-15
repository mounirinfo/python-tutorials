import pandas as pd
import torch
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import BatchNormalization, Activation
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

fichier= pd.read_csv("../traitement_donnees/melb_data.csv")
donnes_sans_vide=fichier.dropna()

x=donnes_sans_vide.drop("Price",axis=1)
y=donnes_sans_vide["Price"]

# on sépare les échantillons d'apprentissage 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

# on cree le modele
model= Sequential()

# on ajoute des couches avec des fonctions d'activation 
model.add(Dense(50, input_shape=(28,)))
model.add(Activation('relu'))
# cette couche permet de normaliser les donnees
model.add(BatchNormalization())
# cette couche evite overfitting (surapprentissage)
model.add(Dropout(0.1))

# on ajoute un autre groupe de couche 
model.add(Dense(10))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Dropout(0.1))

# on ajoute la couche de sortie
model.add(Dense(1))
model.add(Activation('sigmoid'))

# on définit la fonction de perte et la fonction d'optimisation 

model.compile(loss='binary_crossentropy', optimizer ='adam', metrics=["accuracy"])

#on ajuste le modele 
#, batch_size=100, epochs=100
model.fit(x_train, y_train, batch_size=100, epochs=100)

# on calcule l AUC pour les donnees de validation 
print (" AUC pour RN :",roc_auc_score(Y_test,model.predict_proba(X_test, verbose=0).reshape(-1),))