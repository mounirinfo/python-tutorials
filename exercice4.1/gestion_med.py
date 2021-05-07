import pandas as pd
data = pd.read_excel('test_vente.xlsx', sheet_name='Feuil1')
data['chiffre_daffaires']=data.quantite*data.prix_unit
condition = True

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
options=list(menu.keys())


while condition:
    for entry in options: 
        print (entry, menu[entry])
    print("++++++++++++++++++++++++++++++++++++++++++")
    
    selection=input("Please Select the number of the menu:")
    if selection in options:
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
            ca_global=data['chiffre_daffaires'].sum()
            print("Le chiffre daffaires realise est: ", ca_global)
        elif selection =='7':
           med_vendu_max=data['chiffre_daffaires'].argmax()
           print("Le medicament qui a realise le plus grand chiffre daffaires est: ", data.loc[med_vendu_max,:])
        elif selection =='8':
            med_vendu_min=data['chiffre_daffaires'].argmin()
            print("Le medicament qui a realise le plus moins chiffre daffaires est: ", data.loc[med_vendu_min,:])
        elif selection =='9':
             client_vendu_max=data['chiffre_daffaires'].argmax()
             print("le client ayant genere plus grand chiffre daffaires", data.iloc[client_vendu_max]['id_client'])
        elif selection =='10':
            client_acheter_max_produits=data['quantite'].argmax()
            print("le client ayant achete le plus de produits", data.iloc[client_acheter_max_produits]['id_client'])
        elif selection == '0':
            print("Exit")
            condition = False
        afficher_menu= input("voulez vous reafficher le menu? saisir:  \n 0--> Oui \n 1--> Non : \n")
        if afficher_menu == '1':
            condition = False
            print("vous avez choisi de quitter le menu, au revoir!!!")    
    
    else:
        print("Votre choix n'est pas dans la liste, veuillez choisir une option de la liste suivante :\n")
    
    
        
