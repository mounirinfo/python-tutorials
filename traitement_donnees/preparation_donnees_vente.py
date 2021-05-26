import pandas as pd
data_frame_melb=pd.read_csv("melb_data.csv")
data_frame_new=data_frame_melb[["Date","Price"]]
data_frame_new_sans_case_vide=data_frame_new.dropna()
print(data_frame_new_sans_case_vide)
data_frame_new_sans_case_vide['Date']=pd.to_datetime(data_frame_new_sans_case_vide['Date'])
data_frame_new_sans_case_vide.to_csv("fichier.csv")
