import os
nom_fichier= input('entrez le nom du fichier: ')
if nom_fichier.endswith(".xlsx") !=True :
    manip=open(nom_fichier,'r')
    ext = '.'+ os.path.realpath(manip).split('.')[-1:][0]
    filefinal = manip.replace(ext,'.pdf')
    os.rename(manip ,filefinal)
    sheet = manip.sheet_by_index(0)
    n_column= input('entrez le numero de colonne' )
    
    
else:
    print("format eronnee")
