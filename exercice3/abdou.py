file_name = input('plz give the file name : ')
file_to_open = open(file_name,'r')
nbr_total=0 
i=0
for line in file_to_open:
    nbr_of_words= 0
    i=i+1    
    nbr_of_words=len(line.split())
    print('number in line ',i, 'is ',nbr_of_words)
    nbr_total= nbr_total+nbr_of_words

print('the nmbr of words totale is : ',nbr_total)    
