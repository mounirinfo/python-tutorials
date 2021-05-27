'''

'''
import pandas as pd
data_frame_melb=pd.read_csv("melb_data.csv")
data_frame_new=data_frame_melb[["Regionname","Landsize","Price"]]
data_frame_price_region=data_frame_new.dropna()
#remove rows when we don't know landsize


data_frame_price_region["price_mettre"]=data_frame_price_region["Price"]/data_frame_price_region["Landsize"]
price_max=data_frame_price_region["price_mettre"].argmax()
price_min=data_frame_price_region["price_mettre"].argmin()
#print("la ville la plus chere est: ", data_frame_price_region["Regionname"].loc[price_max])
#print("la ville la moins chere est: ", data_frame_price_region["Regionname"].loc[price_min])

data_frame_prix_annee=data_frame_melb[["YearBuilt","Price","Landsize"]]
data_frame_prix_annee_construction=data_frame_prix_annee.dropna()
data_frame_prix_annee_construction_traite = data_frame_prix_annee_construction[data_frame_prix_annee_construction['Landsize'] != 0]
data_frame_prix_annee_construction_traite["prix_mettre"]=data_frame_prix_annee_construction_traite["Price"]/data_frame_prix_annee_construction_traite["Landsize"]

neuf = data_frame_prix_annee_construction_traite[data_frame_prix_annee_construction_traite['YearBuilt'] > 2010]
ancien = data_frame_prix_annee_construction_traite[data_frame_prix_annee_construction_traite['YearBuilt']<2000]
#print([neuf["prix_mettre"]])


print(neuf["prix_mettre"].mean())
print(ancien["prix_mettre"].mean())
#neuf.info()
