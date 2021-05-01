nom_fichier= input('entrez le nom du fichier: ')
manip=open(nom_fichier,'r')
somme=0
for ligne in manip:
    mot_separe=ligne.split()
    print(len(mot_separe))

    somme=somme+int(len(mot_separe))
print('la somme est: ', somme)