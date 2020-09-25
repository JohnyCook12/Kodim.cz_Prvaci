
"""Program PRVACI:
    1) nacte data z studenti.txt jako tabulku seznamu - kazdy radek = vnoreny seznam.
    2) pridame sloupec udavajici vek
    3) pridame sloupec s pohlavim
    4) pridame sloupec email (=5pismen prijmeni + 3pismena jmena @hybrid.eu

"""
import unidecode



def nejaka_fce():                           # dílčí fce
    vstup = open('studenti.txt',"r" , encoding='utf-8')
    radky = [radek.split("\t") for radek in vstup]
    vstup.close()
    jmena = [[radek[0], radek[1], radek[2][0:-1], (100-int(radek[2][0:2])+20), pohlavi(radek[2][2]) , unidecode.unidecode(radek[0][:5])+unidecode.unidecode(radek[1][:3])+"@hybrid.eu" , "\n"] for radek in radky[1:len(radky)]]
    print(jmena)
    
def pohlavi(udaj):
    if int(udaj)>1:
        return "žena"
    else:
        return "muž"

def main():                                # hlavní fce.  (v C a Java se používá jako hlavní fce. V Pythonu ne, ale je to dobrý zvyk. +lze zavolat z importovaného modulu)
    nejaka_fce()

if __name__ == "__main__":                 # zde odpálím můj script     (abych ho mohl i importovat, ne jen spouštět přímo)
    main()