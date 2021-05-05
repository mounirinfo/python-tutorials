import xlrd

import pandas as pd 



nom_fichier= input('entrez le nom du fichier: ')
liste=nom_fichier.split('.')
print('chaine',liste)
format_fichier=liste[-1]

if (format_fichier) =='xlsx' :
    
    data = pd.read_excel(nom_fichier, sheet_name='Feuil1')
    print(data)
    
    
    # wb = xlrd.open_workbook(nom_fichier)
    # sheet = wb.sheet_by_index(0)
    
    # print(sheet.cell_value(0, 0))
    
    
    #afficher le nombre de ligne dans le fichier 
    # n_ligne=sheet.nrows
    # for i in range(sheet.nrows):
    #     somme= (sheet.cell_value(i, 3))
    #     print("la moyenne d'age est: ",somme)
    
else:
    print ("le format du ficheir est erronne ou le fichier n'existe pas")
   