import os, sys, time, random, platform
from colorama import init, Fore, Back, Style

init()


##########################################################
try:
    import requests, bs4, lxml, re
except ImportError:
    print(f"\t\t\033[32mHoşgeldin {renk}{isim}\033[32m Lütfen Bekle ...\033[0m")
    print(f"\tGörünüşe göre requests, bs4, lxml, re yüklü değil :/ . \n\t\tEndişelenme Python'u doğru kurduysan yükleyebilirim ")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip install lxml")
    os.system("pip install re")
    print(f"\t\t {renk} requests, bs4, lxml, re Başarıyla Kuruldu!\n\033[0m")
    time.sleep(3)
    temizle()
    ###############################\\Burdan Başlıyor
    import requests, bs4, lxml, re



##################################################################
URL = 'https://www.discudemy.com/language/Turkish/'
res = requests.get(URL)
soup = bs4.BeautifulSoup(res.text, 'lxml') ## https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning


"""
for Link in soup.find_all('a', href=True): ## https://youtu.be/Vv_FX3FSvGo
    print(Link['href']) ##Komutuyla gelen linklere bak!
"""

for Link in soup.find_all('a', attrs={'href': re.compile("^https://www.discudemy.com/Turkish/")}): ## https://stackoverflow.com/questions/26274724/filtering-urls-obtained-using-beautifulsoup
    GelenDiscudemy = Link['href']
    print(GelenDiscudemy)
    #####################
    ######################################################
    print(Fore.RED + "\tLinkler İşleniyor.." + Fore.WHITE)
    ######################################################
    GelenDiscudemyKaydet = open("GelenDiscudemy.txt", "a")
    GelenDiscudemyKaydet.write(GelenDiscudemy + "\n")
    GelenDiscudemyKaydet.close()


print("\n\t\t" + Fore.GREEN + "Linkler Kaydedildi.." + Fore.WHITE)
time.sleep(1)