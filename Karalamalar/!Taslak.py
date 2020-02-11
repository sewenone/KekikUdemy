#!/usr/bin python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os, sys, time, random, platform
import ctypes   #Ctypes yabancı(dışarıdan) olan fonksiyonların kullanılmasını sağlar.
                #C dilinin veri tiplerini destekler(içinde barındırır).
                #Windows platformunda dynamic link libraries (DLL) dediğimiz,
                #Linux’da ise shared objects (SO) dediğimiz derlenmiş binary kütüphanelerden fonksiyon çağırmaya yarar.

#########################################################################################
isim = os.getlogin()
platform = platform.system()
renk = random.choice(["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"])
#########################################################################################

##############################
def temizle():
    if platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")
##############################

temizle()

####################################################################################################################
try:
    from colorama import init, Fore, Back, Style
except ImportError:
    print(f"\t\t\033[32mHoşgeldin {renk}{isim}\033[32m Lütfen Bekle ...\033[0m")
    print(f"\tGörünüşe göre colorama yüklü değil :/ . \n\t\tEndişelenme Python'u doğru kurduysan yükleyebilirim ")
    os.system("pip install colorama")
    print(f"\t\t {renk} Colorama Başarıyla Kuruldu!\n\033[0m")
    time.sleep(3)
    temizle()
    ############################################
    from colorama import init, Fore, Back, Style
    ################################################################################################################

init()

###########################################################################
if platform == "Windows":
    ctypes.windll.kernel32.SetConsoleTitleW("@KekikAkademi Python Taslağı")
elif platform == "Android":
    clear
else:
    os.system('title @KekikAkademi Python Taslağı')
############################################################################

text = '''
   _    _      _     _ _        ______            _
  | |  / )    | |   (_) |      (_____ \      _   | |
  | | / / ____| |  _ _| |  _    _____) )   _| |_ | |
  | |< < / _  ) | / ) | | / )  |  ____/ | | |  _)| || \ / _ \|  _ \
  | | \ ( (/ /| |< (| | |< (   | |    | |_| | |__| | | | |_| | | | |
  |_|  \_)____)_| \_)_|_| \_)  |_|     \__  |\___)_| |_|\___/|_| |_|
                                      (____/
'''
print(Fore.GREEN + text)
print("\t\t{}| {} |".format(renk,isim) + Fore.YELLOW + ' Oturumundayız..\n')
print(Fore.CYAN + '\t[1] Seçim 1\n\t[2] Seçim 2\n' + Fore.WHITE, end='')
option = str(input("\n>> "))

#################
if option == '1':
#################

    print("[+] 1 Seçildi")
    print(Fore.RED + "5 Saniye İçinde Çıkılıyor.." + Fore.WHITE)
    time.sleep(5)

#################
if option == '2':
#################

    print("[+] 2 Seçildi")
    print(Fore.RED + "5 Saniye İçinde Çıkılıyor.." + Fore.WHITE)
    time.sleep(5)