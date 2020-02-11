###############################
import requests, bs4, lxml, re
###############################

###################################################
URL = 'https://www.discudemy.com/language/Turkish/'
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
    'a', attrs={'href': re.compile("^https://www.discudemy.com/Turkish/")}
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
taranacakSayfa = 10
for SayfaNumarasi in range(1, taranacakSayfa+1):
    URL = 'https://www.discudemy.com/language/Turkish/{}'.format(SayfaNumarasi)
    SayfaAl = requests.get(URL)
    SayfaKaynak = SayfaAl.text
    SayfaOku = BeautifulSoup(SayfaKaynak, 'lxml')
    for Link in SayfaOku.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/Turkish/")}):
        Linkler = Link['href']
        print(Linkler)
##########################################################################################################