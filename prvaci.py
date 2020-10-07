
"""Program PRVACI:
    1) nacte data z studenti.txt jako tabulku seznamu - kazdy radek = vnoreny seznam.
    2) pridame sloupec udavajici vek
    3) pridame sloupec s pohlavim
    4) pridame sloupec email (=5pismen prijmeni + 3pismena jmena @hybrid.eu

"""
import unidecode



def nejaka_fce():                           # dílčí fce
    with open(r'studenti2.txt',"r" , encoding='utf-8') as vstup, open('studenti_vystup.txt',"w" , encoding='utf-8') as vystup, open('studenti_vystup.json',"w" , encoding='utf-8') as vystup_json:          # studenti.txt je puvodni soubor, studenti2.txt ma navic 1 novy radek na konci
        radky = [radek.split("\t") for radek in vstup]
        jmena = [[radek[0], radek[1], radek[2][0:-1], (100-int(radek[2][0:2])+20), pohlavi(radek[2][2]) , unidecode.unidecode(radek[0][:5])+unidecode.unidecode(radek[1][:3])+"@hybrid.eu" , "\n"] for radek in radky[1:len(radky)]]

        jmena_list_of_dicts = [{'krestni_jmeno': [radek[0]], 'prijmeni': [radek[1]]} for radek in radky[1:len(radky)]]
        prijmeni_list = [jmena_list_of_dicts[i]['prijmeni'] for i in range(0, len(jmena_list_of_dicts))]
        print(prijmeni_list)

        #for i in range(0, len(jmena_list_of_dicts)):
        #   print(jmena_list_of_dicts[i]['prijmeni'])

        for jmeno in jmena:
            for udaj in jmeno:
                vystup.write(str(udaj)+"\t")
                vystup_json.write(str(udaj))



def pohlavi(udaj):
    if int(udaj)>1:
        return "žena"
    else:
        return "muž"

def main():                                # hlavní fce.  (v C a Java se používá jako hlavní fce. V Pythonu ne, ale je to dobrý zvyk. +lze zavolat z importovaného modulu)
    nejaka_fce()

if __name__ == "__main__":                 # zde odpálím můj script     (abych ho mohl i importovat, ne jen spouštět přímo)
    main()