import requests
from bs4 import BeautifulSoup
import re


udemy_baslik = []
udemy_link = []

print("Sabır, En Büyük Erdemdir..")

for sayfa in range(1, 4): # ilk döngü /language/Turkish için
    ######################################################################################################
    sayfa = str(sayfa)                                              # int olan değerimizi str yapıyoruz
    link = 'https://www.discudemy.com/language/Turkish/' + sayfa    # sayfalar arasında gezinmek için
    reqs = requests.get(link)
    soup = BeautifulSoup(reqs.text, 'html5lib')
    ######################################################################################################
        
    for heading in soup.findAll('a', {'class': 'card-header'}):
        heading = heading.text
        udemy_baslik.append(heading)
        
    for discudemy_linkler in soup.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/Turkish/")}): # Turkish/kurs-adi
        gelen_discudemy = discudemy_linkler['href']
        discudemy_go_html = requests.get(gelen_discudemy)
        discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'html5lib')

        for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/go/")}): # go/kurs-adi
            gelen_discudemy_go = discudemy_go_linkler['href']
            udemy_html = requests.get(gelen_discudemy_go)
            udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')
            
            for udemy_linkler in udemy_kaynak.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}): # o sayfanın içindeki udemy linki
                gelen_udemy = udemy_linkler['href']
                udemy_link.append(gelen_udemy)

for adet in range(0, len(udemy_baslik)):
    ############################################################
    gelen_udemy_kaydet = open("UdemyBaslik.txt", "a+")
    
    gelen_udemy_kaydet.write("="*100 + f"\n{udemy_baslik[adet]}\n")
    print("="*100 + f"\n{udemy_baslik[adet]}\n")
    
    gelen_udemy_kaydet.write(f"\t{udemy_link[adet]}\n" + "="*100)
    print(f"\t{udemy_link[adet]}\n" + "="*100)
    
    gelen_udemy_kaydet.close()
    ############################################################