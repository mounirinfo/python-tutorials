# 1- first you need to define a separate function that has array of string as parameter
#2- no need to split by -, because you already have an array of string splitted 
#3- you can add tests separatedly from the function

ligne_commande= input ("Entrez votre ligne de commande")


ligne_arguments= ligne_commande.split("-")
print(ligne_arguments)
if ligne_arguments[0]== "":
    ligne_arguments.pop(0)
    
    
for i in range(len(ligne_arguments)):
    
    if ligne_arguments[i][0]=="p":
        port= (ligne_arguments[i]).split()
        numero_port=port[1]
        if numero_port.isdigit():
            
            print("true")
    elif ligne_arguments[i][0]=="l" and ligne_arguments[i][1]==" ":
        
        print("juste")
    elif ligne_arguments[i][0]=="d" and type([ligne_arguments[i]][1:])=="str":
        print("correct")
    else:
        print("rreecrivez votre ligne de commande")
    
            
        # if type(port[1])=="int" :
        #     print("correct")
    
    
    # and type([ligne_arguments[i]][1:])== "int" :
    #     print("votre argument est juste")
    # else:
    #     print(" réécrivez la ligne de commande juste")
    
    
    
    #"-l -p 8080 -d /usr/logs
