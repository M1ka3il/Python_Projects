from posixpath import sep
import requests
import openpyxl
import json
import pprint
import os.path
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

# Gets today's date and safes it as a string in the DatumStr as String
heute =datetime.now()
format = "%d_%m_%Y"
Datum = heute.strftime(format)

# If file doesnt exist it creates a new one and jumps in to the first sheet (Seite1) and creates the fitting row headings
if os.path.exists("C:\\Users\\micha\\vsc-workspace\\BenzinScraper\\Benzinpreise.xlsx") == False:
        wb=Workbook()
        Seite1 = wb.active
        Seite1["A1"] = "Datum"
        Seite1["B1"] = "Name Tankstelle"
        Seite1["C1"] = "Adresse Tankstelle"
        Seite1["D1"] = "PLZ"
        Seite1["E1"] = "Preis L/€"
        Seite1["F1"] = "letzte Aktualisierung vor"
        wb.save("C:\\Users\\micha\\vsc-workspace\\BenzinScraper\\Benzinpreise.xlsx")
else : print("File already exists - Check it out:  C:\\Users\\micha\\vsc-workspace\\BenzinScraper\\Benzinpreise.xlsx")

# User-Agent - Pretend to be one of the Browser/Hardware 
#https://deviceatlas.com/blog/list-of-user-agent-strings
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

#Fill in the URL you want to scrap
URL = 'https://www.clever-tanken.de/tankstelle_liste?lat=49.7499815099169&lon=6.63890642129713&ort=54290&spritsorte=7&r=15/'

# Sends a Clientrequests to the URL and saves the response from the server in the object r 
r = requests.get(url=URL, headers=headers) 

# r.text = raw HTML content , html5lib = specified HTML parser
soup = BeautifulSoup(r.text, 'html5lib')


Benzinpreis = { } # creates an empty dictionary
V1 = "Name"
V2 = "Adresse Tankstelle"
V3 = "PLZ Tankstelle"
V4 = "Preis pro Liter in €"
V5 = "Entfernung"
V6 = "Letzte Aktualisierung"

# Finds all the Gasstation Names in the HTML Codesegment soup and saves them in a list, which is later paired with the Key
TName = soup.find_all('span',  class_='fuel-station-location-name')
for TName in TName:
        #print(TName.decode_contents(), sep="\n")
        Benzinpreis[V1] =[TName.decode_contents()]
        print(Benzinpreis[V1])

# Finds all the Gasstation adresses in the HTML Codesegment soup and saves them in a list, which is later paired with the Key
TAdresse = soup.find_all('div', class_='fuel-station-location-street')
for TAdresse in TAdresse:
        #print(TAdresse.decode_contents(), sep="\n")
        Benzinpreis[V2] = [TAdresse.decode_contents()]
        print(Benzinpreis[V2])


# Finds all the Gasstation zipcode in the HTML Codesegment soup and saves them in a list, which is later paired with the Key
TPlz = soup.find_all('div', class_='fuel-station-location-city')
for TPlz in TPlz:
        #print(TPlz.decode_contents(), sep="\n")
        Benzinpreis[V3] = [TPlz.decode_contents()]
        print(Benzinpreis[V3])

# Finds all the Gasstation prices in the HTML Codesegment soup and saves them in a list, which is later paired with the Key
TPreis = soup.find_all('div', class_='price-text price text-color-ct-blue')
for TPreis in TPreis:
        #print(TPreis.decode_contents(), sep="\n")
        Benzinpreis[V4] = [TPreis.decode_contents()]
        print(Benzinpreis[V4])

# Finds all the Gasstation distance from my zipcode in the HTML Codesegment soup and saves them in a list, which is later paired with the Key
TEntfernung = soup.find_all('div', class_='fuel-station-location-distance d-flex justify-content-end')
for TEntfernung in TEntfernung:
        #print (TEntfernung.decode_contents(), sep='\n')
        Benzinpreis[V5] =[TEntfernung.decode_contents()]
        pprint.pprint(Benzinpreis[V5])

#Finds all the refresh timer from the gasstation prices in the HTML Codesegment soup and saves them in a list, which is later paired with the Key
TAktualisierung = soup.find_all('span', class_='price-changed' )
for TAktualisierung in TAktualisierung:
        #print(TAktualisierung.decode_contents(), sep='\n')
        Benzinpreis[V6] = [TAktualisierung.decode_contents()]
        pprint.pprint(Benzinpreis[V6])

# Next up: Filter the strings in my list so the html code disapears 


#Next up: Find a way to add the key:[list] into one row of my excel sheet



#Saves the excel file maybe instantly open it? 
#wb.save("C:\\Users\\micha\\vsc-workspace\\BenzinScraper\\Benzinpreise_.xlsx")
