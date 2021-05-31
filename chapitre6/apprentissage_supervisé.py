import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
churn= pd.read_csv("telecom.csv")

churn.describe(include="object").transpose()
# verifier si les cases sont vides 
#print (churn.isnull().any())
#print(churn["Area Code"].value_counts())
dict_label_encode={}
for col in churn.columns:
    if churn[col].dtype==object:
        dict_label_encode[col]= LabelEncoder()
        churn[col]=dict_label_encode[col].fit_transform(churn[col])

print(dict_label_encode)