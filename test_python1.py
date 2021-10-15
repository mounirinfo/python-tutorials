import urllib.request

# url= urllib.request.urlopen("https://gist.githubusercontent.com/calvinmetcalf/084ab003b295ee70c8fc/raw/314abfdc74b50f45f3dbbfa169892eff08f940f2/wordlist.txt")
# txt = url.read()

# type(txt)
# x=txt.split()

liste1=['chien','chine','niche','race','poire','proie']

def anagramme (liste):
    liste_anagramme=[]
    for i in range(len(liste)):
        for j in range(len(liste)-i):
            if sorted(liste[i]) == sorted(liste[j+i]) and liste[i]!= liste[j+i]:
                #print(liste[i], ';', liste[j+i])
                liste_anagramme.append((liste[i])+(' ')+(liste[j+i]))
    liste_anagramme= sorted(liste_anagramme)
    print(liste_anagramme)
    return liste_anagramme

def test_anagramme():
    
    assert anagramme(liste1)== ['chien chine', 'chien niche', 'chine niche', 'poire proie']
  
