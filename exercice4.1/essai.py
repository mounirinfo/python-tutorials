import pandas as pd
data = pd.read_excel('test_vente.xlsx', sheet_name='Feuil1')
print(" le menu des informations disponibles ")
print("++++++++++++++++++++++++++++++++++++++++++")
print("1- le medicament le plus vendu")
print("2- le medicament le moins vendu")
print("3- le nombre total des produits vendus")
print("4- le nombre total des références produit vendus")
print("5- le nombre de clients")
print("6- le chiffre d’affaire")
print("7-le médicament ayant généré le plus de chiffre d’affaires ")
print("8- le médicament ayant généré le moins de chiffre d’affaires")
print("9- le client ayant généré le plus chiffre d’affairs")
print("10- le client ayant acheté le plus de produits")
print("++++++++++++++++++++++++++++++++++++++++++")
numero=input ("entrer le numero correspond a linformation que vous voulez savoir")
if numero =='1':
    print("ok")
elif numero =='2':
    print("ok")
elif numero =='3':
    print("ok")
elif numero =='4':
    print("ok")
elif numero =='5':
    print("ok")
elif numero =='6':
    print("ok")
elif numero =='7':
    print("ok")
elif numero =='8':
    print("ok")
elif numero =='9':
    print("ok")
elif numero =='10':
    print("ok")

