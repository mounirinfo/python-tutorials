import pandas as pd
data = pd.read_excel('test_vente.xlsx', sheet_name='Feuil1')
print(" le menu des informations disponibles ")
print("++++++++++++++++++++++++++++++++++++++++++")

menu = {}
menu['1']="le medicament le plus vendu" 
menu['2']="le medicament le moins vendu"
menu['3']="le nombre total des produits vendus"
menu['4']="le nombre total des références produit vendus"
menu['5']="le nombre de clients"
menu['6']="le chiffre d’affaire"
menu['7']="le médicament ayant généré le plus de chiffre d’affaires"
menu['8']="le médicament ayant généré le moins de chiffre d’affaires"
menu['9']="le client ayant généré le plus chiffre d’affairs"
menu['10']="le client ayant acheté le plus de produits"
menu['0']="Exit"   
options=menu.keys()
for entry in options: 
    print (entry, menu[entry])
print("++++++++++++++++++++++++++++++++++++++++++")
selection=input("Please Select:")
if selection =='1':
    maxe=data["quantite"].argmax()
    print("Le medicament le plus vendu: ", data.loc[maxe,:])
elif selection =='2':
    mine=data["quantite"].argmin()
    print("Le medicament le moins  vendu: ", data.loc[mine,:])
elif selection =='3':
    somme=data["quantite"].sum()
    print("le nombre total des produits vendus", somme)
elif selection =='4':
    nombre_produit=data.shape[0]
    print("le nombre de references de produits vendus", nombre_produit)
elif selection =='5':
    tabl=data[['id_client','quantite']].groupby(['id_client']).sum('quantite')
    print("produits vendus par client",tabl)
    nombre_client= len (pd.unique(data['id_client']))
    print("le nombre de client est: " , nombre_client)
elif selection =='6':
    print("ok")
elif selection =='7':
    print("ok")
elif selection =='8':
    print("ok")
elif selection =='9':
    print("ok")
elif selection =='10':
    print("ok")
elif selection == '0':
    print("ok")
