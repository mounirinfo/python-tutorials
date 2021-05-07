import pandas as pd
data = pd.read_excel('test_vente.xlsx', sheet_name='Feuil1')

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
            afficher_menu= input("voulez vous reafficher le menu? saisir:  \n 0--> Oui \n 1--> Non : \n")
            if afficher_menu == '1':
                condition = False
                print("vous avez choisi de quitter le menu, au revoir!!!")
        elif selection =='2':
            mine=data["quantite"].argmin()
            print("Le medicament le moins  vendu: ", data.loc[mine,:])
            afficher_menu= input("voulez vous reafficher le menu? saisir:  \n 0--> Oui \n 1--> Non : \n")
            if afficher_menu == '1':
                condition = False
                print("vous avez choisi de quitter le menu, au revoir!!!")
        elif selection =='3':
            somme=data["quantite"].sum()
            print("le nombre total des produits vendus", somme)
            afficher_menu= input("voulez vous reafficher le menu? saisir:  \n 0--> Oui \n 1--> Non : \n")
            if afficher_menu == '1':
                condition = False
                print("vous avez choisi de quitter le menu, au revoir!!!")
        elif selection =='4':
            nombre_produit=data.shape[0]
            print("le nombre de references de produits vendus", nombre_produit)
            afficher_menu= input("voulez vous reafficher le menu? saisir:  \n 0--> Oui \n 1--> Non : \n")
            if afficher_menu == '1':
                condition = False
                print("vous avez choisi de quitter le menu, au revoir!!!")
        elif selection =='5':
            tabl=data[['id_client','quantite']].groupby(['id_client']).sum('quantite')
            print("produits vendus par client",tabl)
            nombre_client= len (pd.unique(data['id_client']))
            print("le nombre de client est: " , nombre_client)
            afficher_menu= input("voulez vous reafficher le menu? saisir:  \n 0--> Oui \n 1--> Non : \n")
            if afficher_menu == '1':
                condition = False
                print("vous avez choisi de quitter le menu, au revoir!!!")
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
            print("Exit")
            condition = False
    else:
        print("Votre choix n'est pas dans la liste, veuillez choisir une option de la liste suivante :\n")
        
    
        
