#!/usr/bin python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os, sys, time, random, platform
import ctypes   #Ctypes yabancı(dışarıdan) olan fonksiyonların kullanılmasını sağlar.
                #C dilinin veri tiplerini destekler(içinde barındırır).
                #Windows platformunda dynamic link libraries (DLL) dediğimiz,
                #Linux’da ise shared objects (SO) dediğimiz derlenmiş binary kütüphanelerden fonksiyon çağırmaya yarar.

##################################################################
isim = os.getlogin()
platform = platform.system()
renk = random.choice(["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"])
##################################################################

##################################################################
def temizle():
    if platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")
##################################################################

##################################################################
temizle()
try:
    from colorama import init, Fore, Back, Style
except ImportError:
    print(f"\t\t\033[32mHoşgeldin {renk}{isim}\033[32m Lütfen Bekle ...\033[0m")
    print(f"\tGörünüşe göre colorama yüklü değil :/ . \n\t\tEndişelenme Python'u doğru kurduysan yükleyebilirim ")
    os.system("pip install colorama")
    print(f"\t\t {renk} Colorama Başarıyla Kuruldu!\n\033[0m")
    time.sleep(3)
    temizle()
    ##############################
    from colorama import init, Fore, Back, Style ## https://stackoverflow.com/questions/9848889/colorama-for-python-not-returning-colored-print-lines-on-windows
    ##############################

##################################################################
init()
##################################################################
if platform == "Windows":
    ctypes.windll.kernel32.SetConsoleTitleW("@KekikAkademi Python Taslağı")
elif platform == "Android":
    clear
else:
    os.system('title @KekikAkademi Python Taslağı')
##################################################################

text = '''
#   _    _      _     _ _        _     _     _                   
#  | |  / )    | |   (_) |      | |   | |   | |                  
#  | | / / ____| |  _ _| |  _   | |   | | _ | | ____ ____  _   _ 
#  | |< < / _  ) | / ) | | / )  | |   | |/ || |/ _  )    \| | | |
#  | | \ ( (/ /| |< (| | |< (   | |___| ( (_| ( (/ /| | | | |_| |
#  |_|  \_)____)_| \_)_|_| \_)   \______|\____|\____)_|_|_|\__  |
#                                                         (____/ 
'''
print(Fore.GREEN + text)
print("\t\t{}| {} |".format(renk,isim) + Fore.YELLOW + ' Oturumundayız..\n')
print(Fore.CYAN + '\t[1] Discudemy Türkçe Link Çek\n\t[2] Türkçe Linklerden Go Linki Çek\n\t[3] Go Linklerden Udemy Linki Al\n' + Fore.WHITE, end='')
option = str(input("\n>> "))

##################################################################
if option == '1':
##################################################################
    temizle()
    try:
        from bs4 import BeautifulSoup
        import requests, bs4, lxml, re
    except ImportError:
        print(f"\t\t\033[32mHoşgeldin {renk}{isim}\033[32m Lütfen Bekle ...\033[0m")
        print(f"\tGörünüşe göre requests, bs4, lxml, re, BeautifulSoup yüklü değil :/ . \n\t\tEndişelenme Python'u doğru kurduysan yükleyebilirim ")
        os.system("pip install BeautifulSoup")
        os.system("pip install requests")
        os.system("pip install bs4")
        os.system("pip install lxml")
        os.system("pip install re")
        print(f"\t\t {renk} requests, bs4, lxml, re, BeautifulSoup Başarıyla Kuruldu!\n\033[0m")
        time.sleep(3)
        temizle()
        ##############################
        from bs4 import BeautifulSoup
        import requests, bs4, lxml, re
    ############################## https://stackoverflow.com/questions/34610162/extract-all-links-from-a-web-page-using-python
    ############################## https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
    taranacakSayfa = 10 ## https://stackoverflow.com/questions/53625255/python-crawling-beautifulsoup-how-to-crawl-several-pages
    for SayfaNumarasi in range(1, taranacakSayfa+1):
        URL = 'https://www.discudemy.com/language/Turkish/{}'.format(SayfaNumarasi)
        response = requests.get(URL)
        whole_source = response.text
        soup = BeautifulSoup(whole_source, 'lxml') ## https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning
        for DiscudemyLinkler in soup.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/Turkish/")}): ## https://stackoverflow.com/questions/26274724/filtering-urls-obtained-using-beautifulsoup
            GelenDiscudemy = DiscudemyLinkler['href']
            print(GelenDiscudemy)
            #####################
            print(Fore.RED + "\tLinkler İşleniyor.." + Fore.WHITE)
            GelenDiscudemyKaydet = open("GelenDiscudemy.txt", "a")
            GelenDiscudemyKaydet.write(GelenDiscudemy + "\n")
            GelenDiscudemyKaydet.close()
    print("\n\t\t" + Fore.GREEN + "Linkler Kaydedildi.." + Fore.WHITE)
    time.sleep(1)
    os.system("python Beta.py")
##################################################################

##################################################################
if option == '2':
##################################################################
    import requests, bs4, lxml, re

    DiscUdemyGo = open("GelenDiscudemy.txt").readlines() # DiscUdemyGo bir liste oldu [ ]
    for DiscUdemyGoVer in DiscUdemyGo:
    #   print(DiscUdemyGoVer)  # DiscUdemyGo'daki listenin her birini for döngüsü ile çıkardık ve yazdırdık
        DiscUdemyGoURL = DiscUdemyGoVer
        DiscUdemyGoURL = DiscUdemyGoURL.replace("\n","") ## Çekilen Satır Boşluklarını Yok Et
        DiscUdemyGoResponse = requests.get(DiscUdemyGoURL)
        DiscUdemyGoWhole = DiscUdemyGoResponse.text
        DiscUdemyGoSoup = bs4.BeautifulSoup(DiscUdemyGoResponse.text, 'lxml') ## https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning
        for DiscUdemyGoLinkler in DiscUdemyGoSoup.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/go/")}): ## https://stackoverflow.com/questions/26274724/filtering-urls-obtained-using-beautifulsoup
            GelenDiscUdemyGo = DiscUdemyGoLinkler['href']
            print(GelenDiscUdemyGo)
            #####################
            print(Fore.RED + "\tLinkler İşleniyor.." + Fore.WHITE)
            GelenDiscUdemyGoKaydet = open("GelenDiscUdemyGo.txt", "a")
            GelenDiscUdemyGoKaydet.write(GelenDiscUdemyGo + "\n")
            GelenDiscUdemyGoKaydet.close()
    print("\n\t\t" + Fore.GREEN + "Linkler Kaydedildi.." + Fore.WHITE)
    time.sleep(1)
    os.system("python Beta.py")

##################################################################
if option == '3':
##################################################################
    import requests, bs4, lxml, re

    Udemy = open("GelenDiscUdemyGo.txt").readlines() # Udemy bir liste oldu [ ]
    for UdemyVer in Udemy:
    #   print(UdemyVer)  # Udemy'daki listenin her birini for döngüsü ile çıkardık ve yazdırdık
        UdemyURL = UdemyVer
        UdemyURL = UdemyURL.replace("\n","") ## Çekilen Satır Boşluklarını Yok Et
        UdemyResponse = requests.get(UdemyURL)
        UdemyWhole = UdemyResponse.text
        UdemySoup = bs4.BeautifulSoup(UdemyResponse.text, 'lxml') ## https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning
        for UdemyLinkler in UdemySoup.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}): ## https://stackoverflow.com/questions/26274724/filtering-urls-obtained-using-beautifulsoup
            GelenUdemy = UdemyLinkler['href']
            print(GelenUdemy)
            #####################
            print(Fore.RED + "\tLinkler İşleniyor.." + Fore.WHITE)
            GelenUdemyKaydet = open("GelenUdemy.txt", "a")
            GelenUdemyKaydet.write(GelenUdemy + "\n")
            GelenUdemyKaydet.close()
    print("\n\t\t" + Fore.GREEN + "Linkler Kaydedildi.." + Fore.WHITE)