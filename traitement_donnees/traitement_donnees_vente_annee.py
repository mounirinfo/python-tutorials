import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data_frame=pd.read_csv("fichier.csv")
data_frame['Date']=pd.to_datetime(data_frame['Date'])
data_frame["annee"]=data_frame['Date'].dt.year

data_frame_stat=data_frame.groupby(["annee"],as_index=False)['Price'].agg({'Price_mean': 'mean'})
print(data_frame_stat)

#plt.plot(data_frame_stat)
#plt.title("Evolution du prix de vente de maison")
#plt.xlabel("annee")
#plt.ylabel("Prix")
sns.boxplot(data_frame["annee"],data_frame["Price"])
plt.title("Evolution du prix de vente de maison")
plt.savefig("boite_a_moustaches.png")