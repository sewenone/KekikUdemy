#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
# @raifpy > Ömer Rai'ye Sonsuz Teşekkürler..

########################################################################################################################
## ModulYukle
# https://github.com/raif-py/pentester/blob/master/PentesterBeta.py
try:                                        # Dene
    import os                       # Dizinler ve dosyalarla çalışmak için
    import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
    import time,datetime,pytz       # Zaman/Tarih Bilgisi sağlayacak arkadaşlar
    import ctypes                   # C dili veri tipleri kullanmamızı sağlayacak arkadaş (.DLL / .SO)
    import colorama                 # Ortalığın renklenmesini sağlayacak arkadaş
    from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
    colorama.init(autoreset=True)   # Renklerin ilgili satırdan başka satıra devam etmemesi için
    import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
    from bs4 import BeautifulSoup   # HTML veya XML dosyalarını işleyen arkadaş
    import re                       # Ayrıştırıcı Arkadaş
except ModuleNotFoundError:                 # Modül bulunamadıysa
    try:                                    # Dene
        os.system("pip3 install platform")  # pip3 ile Yüklemeyi
        os.system("pip3 install datetime")  # pip3 ile Yüklemeyi
        os.system("pip3 install pytz")      # pip3 ile Yüklemeyi
        os.system("pip3 install ctypes")    # pip3 ile Yüklemeyi
        os.system("pip3 install colorama")  # pip3 ile Yüklemeyi
        os.system("pip3 install requests")  # pip3 ile Yüklemeyi
        os.system("pip3 install bs4")       # pip3 ile Yüklemeyi
        os.system("pip3 install re")        # pip3 ile Yüklemeyi
    except:                                 # pip3 yüklemediyse
        os.system("pip install platform")   # pip ile Yüklemeyi
        os.system("pip install datetime")   # pip ile Yüklemeyi
        os.system("pip install pytz")       # pip ile Yüklemeyi
        os.system("pip install ctypes")     # pip ile Yüklemeyi
        os.system("pip install colorama")   # pip ile Yüklemeyi
        os.system("pip install requests")   # pip ile Yüklemeyi
        os.system("pip install bs4")        # pip ile Yüklemeyi
        os.system("pip install re")         # pip ile Yüklemeyi
    try:                                    # Tekrar dene
        import os                       # Dizinler ve dosyalarla çalışmak için
        import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
        import time,datetime,pytz       # Zaman/Tarih Bilgisi sağlayacak arkadaşlar
        import ctypes                   # C dili veri tipleri kullanmamızı sağlayacak arkadaş (.DLL / .SO)
        import colorama                 # Ortalığın renklenmesini sağlayacak arkadaş
        from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
        colorama.init(autoreset=True)   # Renklerin ilgili satırdan başka satıra devam etmemesi için
        import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
        from bs4 import BeautifulSoup   # HTML veya XML dosyalarını işleyen arkadaş
        import re                       # Ayrıştırıcı Arkadaş
    except Exception as hata:               # Hala hata var ise
        sys.exit(f"{Fore.RED}Modüller yüklenemedi !\n\n{Fore.CYAN}Log : {Fore.LIGHTBLACK_EX}{hata}") # Kapat(yazdır)
########################################################################################################################

########################################################################################################################
## GenelDegiskenler
pencere_basligi = "@KekikAkademi UDEMY Kupon Çekme Aracı"                        # Pencere Başlığımız
logo = '''
   _    _      _     _ _        _     _     _                   
  | |  / )    | |   (_) |      | |   | |   | |                  
  | | / / ____| |  _ _| |  _   | |   | | _ | | ____ ____  _   _ 
  | |< < / _  ) | / ) | | / )  | |   | |/ || |/ _  )    \| | | |
  | | \ ( (/ /| |< (| | |< (   | |___| ( (_| ( (/ /| | | | |_| |
  |_|  \_)____)_| \_)_|_| \_)   \______|\____|\____)_|_|_|\__  |
                                                         (____/   
'''                                                                   # Logomuz
        # logo = http://patorjk.com/software/taag/#p=display&f=Doom&t=kopya%20Kagidi
#######################################################################################
try:
    kullanici_adi = os.getlogin()                                     # Kullanıcı Adı
except:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]                     # Kullanıcı Adı
bilgisayar_adi = platform.node()                                      # Bilgisayar Adı
oturum = kullanici_adi + "@" + bilgisayar_adi                         # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()                                             # İşletim Sistemi
bellenim_surumu = platform.release()                                            # Sistem Bellenim Sürümü
cihaz = isletim_sistemi + " | " + bellenim_surumu                               # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")     # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")         # Bugünün Saati
zaman = tarih + " | " + saat

ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz
ip = ip_req.text                                # ip Adresi

ust_bilgi = f"""
    {Fore.LIGHTBLACK_EX}{kullanici_adi} | {cihaz} | {Fore.LIGHTGREEN_EX}{ip} 
          {Fore.YELLOW}{zaman}
    """                                                               # Üst Bilgimiz
########################################################################################################################

########################################################################################################################
def Temizle():                          # Temizle adında bir fonksiyon oluşturduk
    if isletim_sistemi == "Windows":    # Eğer İşletim Sistemi "Windows" ise
        os.system("cls")                # Sisteme "cls" komutu gönder
    else:                               # Sistem Windows değil ise
        os.system("clear")              # Sisteme "clear" komutu gönder
Temizle()                               # Temizle fonksiyonumuzu çağırdık
########################################################################################################################

########################################################################################################################
def PencereBasligi():                                                               # PencereBasligi fonksiyonu
    if isletim_sistemi == "Windows":                                                # Eğer İşletim Sistemi "Windows" ise
        ctypes.windll.kernel32.SetConsoleTitleW(f"{pencere_basligi}")       # Konsol Başlığını ayarla
    elif isletim_sistemi == "Android":                                              # Eğer İşletim Sistemi "Android" ise
        os.system("clear")                                                          # Sisteme "clear" komutu gönder
    elif isletim_sistemi == "Linux":                                                # Eğer İşletim Sistemi "Linux" ise
        os.system(f'echo "\033]0;{pencere_basligi}\007"')                   # Başlık Ayarla
    else:                                                                           # Hiçbiri değil ise
        os.system(f'title {pencere_basligi}')                               # Başlık Ayarla
PencereBasligi()                                                                    # PencereBasligi çağır
########################################################################################################################

########################################################################################################################
def WindowsBildirimi(): # WindowsBildirimi adında bir metod oluşturduk
    if isletim_sistemi == "Windows":
        from win10toast import ToastNotifier         # Windows'a bildirim göndermek için
        bildirim = ToastNotifier()
        bildirim.show_toast(f"{pencere_basligi}", "Başlıyoruz :)", icon_path=None, duration=10, threaded=True)
    else:
        pass
WindowsBildirimi()
########################################################################################################################

########################################################################################################################
def DiscUdemy():
    def DiscUdemyCrawl(sayi):
        sayi = str(sayi)                                        # int olan değerimizi str yapıyoruz
        link = "http://www.discudemy.com/language/Turkish/" + sayi # sayfalar arasında gezinmek için
        kimlik = {'User-Agent': '@KekikAkademi'}                # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
        html = requests.get(link, headers=kimlik)               # Url'nin içerisindeki bütün html dosyasını indiriyoruz.
        kaynak = BeautifulSoup(html.text, "html.parser")        # bitifulsup ile html'i işlememiz gerekiyor / html.parser'i kullandık

        #######################################################################################
        linkler = kaynak.find_all("a", attrs={
            "class": "card-header"})  # sınıf'ı kart-header olan tüm linkleri çekiyoruz bununla
        #######################################################################################
        
        ##############################################################################################################
        for i in linkler:       # linkler listesini i olarak ayırdık
            i = i["href"]       # i'nin hreflerini aldık (linkleri)
            i = i.split("/")    # discudemy.com/katagori olan linki udemy.com olarak değiştirmemiz gerekiyor.
                                # Bunun için / 'ları bulduktan sonra buralardan bölüyoruz
            i = i[0] + "//www.udemy.com/course/" + i[4]  # i[0] = https: i[4] = udemy linki'miz
            print(f"{Fore.LIGHTBLACK_EX}{i} {Fore.CYAN}| {Fore.GREEN} Yazıldı !") # i değerimizi (linkimizi) yazdık
            link_kaydet = open("UdemyeGiderken.txt", "a")
            link_kaydet.write(i + "\n")
            link_kaydet.close()
        ##############################################################################################################
    
    ##################################################################################################################
    for ii in range(1, 4):      # Neden : discumdey.com sitesi site.com/all/1 ,2 ,4 ,200 şeklinde kursları yayınlıyor.
                                # Bu sepeten döngüne aldık . Elbette geliştirilebilir
        DiscUdemyCrawl(ii)      # DiscUdemyCrawl dediğimiz eleman herşeyi başlatan
    ##################################################################################################################
    
    ######################################
    satir_say = open("UdemyeGiderken.txt")
    satir = 0
    for line in satir_say:
        satir = satir+1
    print(f"\n\t{Fore.GREEN} Yazılan Link Sayısı{Fore.YELLOW} >> {Fore.RED}{satir} ")
    satir_say.close()
    ######################################
########################################################################################################################

########################################################################################################################
def AcilisSayfasi():
    print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)                # Üst Bilgimizi yazdırdık
    print(f"""
    {Fore.GREEN}[{Fore.YELLOW} 1 {Fore.GREEN}] {Fore.CYAN}Discudemy TR Linkleri (3 Sayfa Tarar)
    {Fore.GREEN}[{Fore.YELLOW} 2 {Fore.GREEN}] {Fore.CYAN}RealDiscount Linkleri (4 Sayfa Tarar)
    {Fore.GREEN}[{Fore.YELLOW} 3 {Fore.GREEN}] {Fore.CYAN}Çekilenleri Udemy e Çevir
    """) # Seçeneklerimizi ayarladık

    secenek = str(input(f"{Fore.RED}{oturum}{Fore.LIGHTBLUE_EX} >> {Fore.GREEN}")) # Kullanıcı için input oluşturduk
    #########################
    if secenek == '1':      # Eğer 1 i seçerse
        Temizle()           # Temizle fonksiyonunu çalıştır
        print(Fore.LIGHTBLUE_EX + logo)
        print(ust_bilgi)    # Üst Bilgi fonksiyonunu çalıştır
        DiscUdemy()         # DiscUdemy fonksiyonunu çalıştır
    #########################
    elif secenek == '2':    # Eğer 2 yi seçerse
        Temizle()           # Temizle fonksiyonunu çalıştır
        print(Fore.LIGHTBLUE_EX + logo)
        print(ust_bilgi)    # Üst Bilgi fonksiyonunu çalıştır
        print("Bu işlem henüz hazır değil..")
        AcilisSayfasi()
    #########################
    elif secenek == '3':    # Eğer 3 ü seçerse
        Temizle()           # Temizle fonksiyonunu çalıştır
        print(Fore.LIGHTBLUE_EX + logo)
        print(ust_bilgi)    # Üst Bilgi fonksiyonunu çalıştır
        print("Bu işlem henüz hazır değil..")
        AcilisSayfasi()
    #########################
    else:                   # Eğer harici bişey seçerse
        pass                # Aldırış etme (çökme)
        Temizle()           # Temizle fonksiyonunu çalıştır
        AcilisSayfasi()     # AcilisSayfasi fonksiyonunu çalıştır

AcilisSayfasi()
########################################################################################################################