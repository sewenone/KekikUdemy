###############################
import requests, bs4, lxml, re
###############################

###################################################
URL = 'https://www.real.discount/new/'
SayfaAl = requests.get(URL)
SayfaOku = bs4.BeautifulSoup(SayfaAl.text, 'lxml')
###################################################
###############################################
##!!!Önce Gelen Linklere bak!!!##
#################################
"""
for Link in SayfaOku.find_all('a', href=True):
    print(Link['href'])
"""
###############################################
##########################################################################
##Sonra istediğin filtreyi ayıkla##
###################################
"""
for Link in SayfaOku.find_all(
    'a', attrs={'href': re.compile("^https://www.real.discount/offer/")}
    ):
    
    GelenDiscudemy = Link['href']
    print(GelenDiscudemy)
"""
##########################################################################



###############################
##Döngü İstersen;##
###################
from bs4 import BeautifulSoup
import requests, bs4, lxml, re
###############################
##########################################################################################################
taranacakSayfa = 3
for SayfaNumarasi in range(1, taranacakSayfa+1):
    URL = 'https://www.real.discount/new/{}'.format(SayfaNumarasi)
    SayfaAl = requests.get(URL)
    SayfaKaynak = SayfaAl.text
    SayfaOku = BeautifulSoup(SayfaKaynak, 'lxml')
    for Link in SayfaOku.findAll('a', attrs={'href': re.compile("^https://www.real.discount/offer/")}):
        Linkler = Link['href']
        print(Linkler)
##########################################################################################################
#################################################
        ##Hemen Burda Dönen Linkleri Kaydet######
        #########################################
        print("\tLinkler İşleniyor..")
        LinklerKaydet = open("Linkler.txt", "a")
        LinklerKaydet.write(Linkler + "\n")
        LinklerKaydet.close()
print("\n\t\tLinkler.txt Kaydedildi..\n")
##################################################


##########################################################################################################
###İkinci Aşama;###
###################################
from bs4 import BeautifulSoup
import requests, bs4, lxml, re, os
###################################
Udemy = open("Linkler.txt").readlines() # Udemy bir liste oldu [ ]
for UdemyVer in Udemy:
#   print(UdemyVer)  # Udemy'deki listenin her birini for döngüsü ile çıkardık ve yazdırdık
    UdemyURL = UdemyVer
    UdemyURL = UdemyURL.replace("\n","") ## Çekilen Satır Boşluklarını Yok Et
    UdemyResponse = requests.get(UdemyURL)
    UdemyWhole = UdemyResponse.text
    UdemySoup = bs4.BeautifulSoup(UdemyResponse.text, 'lxml')
    for UdemyLinkler in UdemySoup.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}):
        GelenUdemy = UdemyLinkler['href']
        print(GelenUdemy)
##########################################################################################################
##########################################################################################
        ##Hemen Burda Dönen Linkleri Kaydet######
        #########################################
        print("\tUdemy Linkler İşleniyor..")
        GelenUdemyKaydet = open("Udemylerce.txt", "a") ## Belki Eş Gelen Linkler Vardır.
        GelenUdemyKaydet.write(GelenUdemy + "\n")
        GelenUdemyKaydet.close()
print("\n\t\tUdemylerce.txt Kaydedildi..\n")
os.remove("Linkler.txt")
print("\n\t\tLinkler.txt Silindi\n") ## Birinci Aşamada Çektiğimiz Gereksiz Linkler
##########################################################################################
############################################################
        ##Eş Gelen Linkleri Silelim###############
##################################################
print("\n\t\tÇift Linkler Siliniyor..\n")
BenzerLink = set() # Bütün Satırları Tut
SilBenzerLink = open("KekikUdemy.txt", "a")
for line in open("Udemylerce.txt", "r"):
    if line not in BenzerLink: # Eş çıkmayana kadar döndür
        SilBenzerLink.write(line)
        BenzerLink.add(line)
SilBenzerLink.close()
print("\n\t\tÇift Linkler Silindi..\n")
os.remove("Udemylerce.txt")
print("\n\t\tUdemylerce.txt Silindi\n") ## Eşli Linkler
print("\n\t\tKekikUdemy.txt Kaydedildi!!!\n") ## Son Hali
############################################################