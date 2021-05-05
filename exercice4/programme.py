
import pandas as pd 



nom_fichier= input('entrez le nom du fichier: ')
liste=nom_fichier.split('.')
print('chaine',liste)
format_fichier=liste[-1]

if format_fichier =='xlsx' :
    
    data = pd.read_excel(nom_fichier, sheet_name='Feuil1')
    print (' Menu des actions a faire :')
    print('+++++++++++++++++++++++++++++')
    print ( '1- Afficher les colonnes du fichier')
    print ( '2- Le nombre de lignes de fichier')
    print(' 3- Exporter les 10 premieres lignes dans un autre fichier excel')
    print (' 4- exporter un fichier avec les colonnes et la moyenne de chaque colonne si elle est numérique')
    print('++++++++++++++++++++++')
    numero= input ('choisir le numero de laction que vous voulez faire ' )
    if numero =='1':
        print('les colonnes du fichier', data.columns)
    elif numero=='2':
        num_rows=data.shape[0]
        print('le nombre de lignes de fichier',num_rows)
    elif numero=='3':
        print('lexportation des 10 premeires lignes' )
        resultat=data.head(10)
        resultat.to_excel(excel_writer = "array.xlsx")
    elif numero=='4':
        
        print('la moyenne de lage', data["age"].mean())
        
    else:
        print('resaissez le bon numero')

else:
    print ("le format du fichier est erroné ou le fichier n'existe pas")
   