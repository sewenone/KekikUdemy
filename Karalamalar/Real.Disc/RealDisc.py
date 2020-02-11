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
print(Fore.CYAN + '\t[1] RealDisc ALL Link Çek\n\t[2] Udemy Linki Al\n' + Fore.WHITE, end='')
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
        URL = 'https://www.real.discount/new/{}'.format(SayfaNumarasi)
        response = requests.get(URL)
        whole_source = response.text
        soup = BeautifulSoup(whole_source, 'lxml') ## https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning
        for DiscudemyLinkler in soup.findAll('a', attrs={'href': re.compile("^https://www.real.discount/offer/")}): ## https://stackoverflow.com/questions/26274724/filtering-urls-obtained-using-beautifulsoup
            GelenDiscount = DiscudemyLinkler['href']
            print(GelenDiscount)
            #####################
            print(Fore.RED + "\tLinkler İşleniyor.." + Fore.WHITE)
            GelenDiscountKaydet = open("RealDisc.txt", "a")
            GelenDiscountKaydet.write(GelenDiscount + "\n")
            GelenDiscountKaydet.close()
    print("\n\t\t" + Fore.GREEN + "Linkler Kaydedildi.." + Fore.WHITE)
    time.sleep(1)
###########################################################################
    print("\n\t\t" + Fore.YELLOW + "Çift Linkler Siliniyor.." + Fore.WHITE)
    lines_seen = set() # holds lines already seen
    outfile = open("RealDiscTemiz.txt", "w")
    for line in open("RealDisc.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    print("\n\t\t" + Fore.YELLOW + "Çift Linkler Silindi.." + Fore.WHITE)
    time.sleep(1)
    os.system("python RealDisc.py")
###########################################################################

##################################################################
if option == '2':
##################################################################
    import requests, bs4, lxml, re

    RealUdemy = open("RealDiscTemiz.txt").readlines() # RealUdemy bir liste oldu [ ]
    for RealUdemyVer in RealUdemy:
    #   print(RealUdemyVer)  # RealUdemy'daki listenin her birini for döngüsü ile çıkardık ve yazdırdık
        RealUdemyURL = RealUdemyVer
        RealUdemyURL = RealUdemyURL.replace("\n","") ## Çekilen Satır Boşluklarını Yok Et
        RealUdemyResponse = requests.get(RealUdemyURL)
        RealUdemyWhole = RealUdemyResponse.text
        RealUdemySoup = bs4.BeautifulSoup(RealUdemyResponse.text, 'lxml') ## https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning
        for RealUdemyLinkler in RealUdemySoup.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/course/")}): ## https://stackoverflow.com/questions/26274724/filtering-urls-obtained-using-beautifulsoup
            GelenDiscountGo = RealUdemyLinkler['href']
            print(GelenDiscountGo)
            #####################
            print(Fore.RED + "\tLinkler İşleniyor.." + Fore.WHITE)
            GelenDiscountGoKaydet = open("RealUdemy.txt", "a")
            GelenDiscountGoKaydet.write(GelenDiscountGo + "\n")
            GelenDiscountGoKaydet.close()
    print("\n\t\t" + Fore.GREEN + "Linkler Kaydedildi.." + Fore.WHITE)
    time.sleep(1)
########################################################################### ## https://blog.georgechalhoub.com/2015/09/remove-duplicate-lines-from-file-using.html
    print("\n\t\t" + Fore.YELLOW + "Çift Linkler Siliniyor.." + Fore.WHITE)
    lines_seen = set() # holds lines already seen
    outfile = open("RealUdemyTemiz.txt", "w")
    for line in open("RealUdemy.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    print("\n\t\t" + Fore.YELLOW + "Çift Linkler Silindi.." + Fore.WHITE)
    time.sleep(1)
    os.system("python RealDisc.py")
###########################################################################