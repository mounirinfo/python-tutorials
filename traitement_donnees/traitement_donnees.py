import pandas as pd
data_frame_melb=pd.read_csv("melb_data.csv")
data_frame_sans_case_vide=data_frame_melb.dropna() # pourquoi tu as supprimé les na  ? il y a combien de na qui sont supprimés après cette ligne
print (data_frame_sans_case_vide.info())
#print(data_frame_sans_case_vide["Suburb"].value_counts())
#frame_suburb=pd.get_dummies(data_frame_sans_case_vide["Suburb"])
# print(frame_suburb)
#print(data_frame_sans_case_vide["Type"].value_counts())
#frame_type=pd.get_dummies(data_frame_sans_case_vide["Type"])
#print(frame_type)
#frame_methode=pd.get_dummies(data_frame_sans_case_vide["Method"])
#frame_sellerg=pd.get_dummies(data_frame_sans_case_vide["SellerG"])
data_frame_sans_case_vide['Date']=pd.to_datetime(data_frame_sans_case_vide['Date'])
#pourquoi tu as utilisé les prefixes? et c'est quoi le résultat du get_dummies
data_exp=pd.get_dummies(data_frame_sans_case_vide, prefix = ['Suburb','Address','Type','Method','sellerG','CouncilArea','Regionname'], columns=['Suburb','Address','Type','Method','SellerG','CouncilArea','Regionname'])
print(data_exp)