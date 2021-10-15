import urllib.request

url= urllib.request.urlopen("https://gist.githubusercontent.com/calvinmetcalf/084ab003b295ee70c8fc/raw/314abfdc74b50f45f3dbbfa169892eff08f940f2/wordlist.txt")
txt = url.read()

type(txt)
x=txt.split()



liste1=['chien','chine','niche','race','poire','proie']
  
for i in range(len(liste1)):
    for j in range(len(liste1)-i):
        if sorted(liste1[i]) == sorted(liste1[j+i]):
            print(liste1[i], ';', liste1[j+i])
            
            
    
  
