#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
# @raifpy > Ömer Rai'ye Sonsuz Teşekkürler..

#################################
from PyQt5.QtCore import *      #
from PyQt5.QtGui import *       #
from PyQt5.QtWidgets import *   #
import sys                      #
#################################
from bs4 import BeautifulSoup       # HTML veya XML dosyalarını okuyan arkadaş
import html5lib                     # HTML dosyalarını işleyen arkadaş
import re                           # Ayrıştırıcı Arkadaş
#########################################################################################################
import os                           # Dizinler ve dosyalarla çalışmak için                              #
import platform                     # Çalışılan makine bilgisi sağlayacak arkadaş                       #
import time, datetime, pytz         # Zaman/Tarih Bilgisi sağlayacak arkadaşlar                         #
import requests                     # Websitelerine istek atmamızı sağlayacak arkadaş                   #
#-------------------------------------------------------------------------------------------------------#
try:                                                                                                    #
    kullanici_adi = os.getlogin()                               # Kullanıcı Adı                         #
except:                                                                                                 #
    import pwd                                                                                          #
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]               # Kullanıcı Adı                         #
                                                                                                        #
bilgisayar_adi = platform.node()                                # Bilgisayar Adı                        #
oturum = kullanici_adi + "@" + bilgisayar_adi                   # Örn.: "kekik@Administrator"           #
                                                                                                        #
isletim_sistemi = platform.system()                     # İşletim Sistemi                               #
bellenim_surumu = platform.release()                    # Sistem Bellenim Sürümü                        #
cihaz = isletim_sistemi + " | " + bellenim_surumu       # Örn.: "Windows | 10"                          #
                                                                                                        #
tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")     # Bugünün Tarihi        #
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")         # Bugünün Saati         #
zaman = tarih + " | " + saat                                                    # 18-03-2020 | 02:30    #
                                                                                                        #
ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz    #
ip = ip_req.text                                # ip Adresi                                             #
                                                                                                        #
ust_bilgi = f"{kullanici_adi} | {cihaz} | {ip} \n\t{zaman}"     # Üst Bilgimiz                          #
pencere_basligi = "KekikUdemy Kupon Botu GUI | @KekikAkademi"   # Pencere Başlığımız                    #
#-------------------------------------------------------------------------------------------------------#####
def WindowsTerminaliGizle():                        # WindowsTerminaliGizle adında bir fonksiyon oluşturduk #
    if isletim_sistemi == "Windows":                # Eğer İşletim Sistemi "Windows" ise                    #
        import win32console, win32gui               # Gerekli Modüller                                      #
        terminal = win32console.GetConsoleWindow()  # Terminal adlı değişken                                #
        win32gui.ShowWindow(terminal, 0)            # Görünmez yap                                          #
    else:                                           # Eğer İşletim Sistemi "Windows" değilse                #
        pass                                        # Boşver :)                                             #
WindowsTerminaliGizle()     # Eğer Windows'da Terminalin gizlenmesini istiyosanız aktifleştirin             #
                            # -- pyinstaller -i udemy.ico --onefile --noconsole KekikUdemyGUI.py --         #
#############################################################################################################
#####################################
class Pencere(QWidget):             # Penceremizi Oluşturduk
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # vBox -- Dikey Yerleşim (Vertical Layout)
        vBox = QVBoxLayout()

        # hBox -- Yatay Yerleşim (Horizontal Layout)
        hBox = QHBoxLayout()

        # Başlık
        baslik = QLabel()
        baslik.setText(f'<h1><font color="green">{pencere_basligi}</font></h1>')
        baslik.setFont(QFont("Helvatica",15,QFont.Bold))
        baslik.setAlignment(Qt.AlignCenter)

        # Sistem
        sistem = QLabel()
        sistem.setText(ust_bilgi)
        sistem.setFont(QFont("Courier",12,QFont.Bold))
        sistem.setAlignment(Qt.AlignCenter)

        # Logo
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap(r"img/KekikAkademiQt5Logo.png").scaled(700,250))
        self.logo.setAlignment(Qt.AlignCenter)

        # Alınan Kurslar
        self.alinanKurslar = QTextEdit()

        # Çekilecek Sayfa
        self.cekilecekSayfa = QLineEdit()
        self.cekilecekSayfa.setPlaceholderText("Kaç Sayfa Çekilsin?")

        # discUdemy
        discUdemy = QPushButton()
        discUdemy.setIcon(QIcon(r"img/discUdemy.png"))
        discUdemy.setText("discUdemy")
        discUdemy.clicked.connect(self.DiscUdemy)

        # realDiscount
        realDiscount = QPushButton()
        realDiscount.setIcon(QIcon(r"img/realDiscount.png"))
        realDiscount.setText("realDiscount")
        realDiscount.clicked.connect(self.RealDiscount)

        # Yatay Düzen'e(hBox'a) Yerleştir
        hBox.addWidget(self.cekilecekSayfa)
        #hBox.addStretch()                              # Dikey dinamik uzaklığı koru
        hBox.addWidget(discUdemy)
        #hBox.addStretch()                              # Dikey dinamik uzaklığı koru
        hBox.addWidget(realDiscount)

        # Dikey Düzen'e(vBox'a) Yerleştir
        vBox.addWidget(baslik)
        vBox.addWidget(sistem)
        vBox.addWidget(self.logo)
        vBox.addWidget(self.alinanKurslar)
        vBox.addLayout(hBox)

        self.setLayout(vBox)
#########################################################
        self.show()                                     # Pencereyi göster
        self.setWindowTitle(f"{pencere_basligi}")       # Pencere Başlığımızı Belirledik
        self.setWindowIcon(QIcon("img/udemy.png"))      # Pencere İkonumuzu Belirledik
        self.setMinimumSize(QSize(750, 500))            # Pencere Min. Ebat Tanımladık
        self.setMaximumSize(QSize(750, 750))            # Pencere Max. Ebat Tanımladık
        #pencere.setGeometry(700,300,500,500)            # 700x300 kordinatında başlayarak / 500x500 ebatında aç

    def DiscUdemy(self):
        #-------------------------------------------------------------------------------------------#
        udemy_baslik = []                                                   # Boş Tablo Oluşturduk  #
        udemy_link = []                                                     # Boş Tablo Oluşturduk  #
        #-------------------------------------------------------------------------------------------#

        for sayfa in range(1, int(self.cekilecekSayfa.text())):             # Sayfa Sayısı | örn:(1, 3) {2 Sayfa Tarar [1-2]}
            #----------------------------------------------------------------------------------------------------------------------------------#
            sayfa = str(sayfa)                                              # int olan değerimizi str yapıyoruz
            link = 'https://www.discudemy.com/language/Turkish/' + sayfa    # sayfalar arasında gezinmek için
            kimlik = {'User-Agent': '@KekikAkademi'}                        # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
            istek = requests.get(link)                                      # link'e istek göderiyoruz ve gelen veriyi kaydediyoruz
            kaynak = BeautifulSoup(istek.text, 'html5lib')                  # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
            #####self.logo.setText(link)                                         # Ekrana Yaz
            #sleep(1)                                                        # Bekleme Ver
            #----------------------------------------------------------------------------------------------------------------------------------#

            #---------------------------------------------------------------------------------------------------------------------#
            for heading in kaynak.findAll('a', {'class': 'card-header'}):   # kaynak'tan | <a class'ı = card-header olanları tut
                heading = heading.text                                      # Yazı Formatına Çevir
                udemy_baslik.append(heading)                                # Tablomuza Yerleştir
                ######self.logo.setText(heading)                                 # Ekrana Yaz
            #sleep(1)                                                        # Bekleme Ver
            #---------------------------------------------------------------------------------------------------------------------#

            #-----------------------------------------------------------------------------------------------------------------------#
            for discudemy_linkler in kaynak.findAll('a', attrs={                        # kaynak'tan | <a olanları _ ve
                'href': re.compile("^https://www.discudemy.com/Turkish/")}):            # href="../Turkish/' olan linkleri tut
                gelen_discudemy = discudemy_linkler['href']                             # dönen verideki linkleri tut
                discudemy_go_html = requests.get(gelen_discudemy)                       # onlara istek gönder
                discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'html5lib') # kaynağını al
                #####self.logo.setText(gelen_discudemy)                            # Ekrana Yaz
                #sleep(1)                                                                # Bekleme Ver
                
                #-------------------------------------------------------------------------------------------------------------------#
                for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={    # aldığın kaynaktan | <a olanları _ ve
                    'href': re.compile("^https://www.discudemy.com/go/")}):             # href="../go/kurs-adi" olan linkleri tut
                    gelen_discudemy_go = discudemy_go_linkler['href']                   # dönen verideki linkleri tut
                    udemy_html = requests.get(gelen_discudemy_go)                       # onlara istek gönder
                    udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')           # kaynağını al
                    ####self.logo.setText(gelen_discudemy_go)                     # Ekrana Yaz
                    #sleep(1)                                                            # Bekleme Ver
                    
                    #---------------------------------------------------------------------------------------------------------------#
                    for udemy_linkler in udemy_kaynak.findAll('a', attrs={              # aldığın kaynaktan | <a olanları _ ve
                        'href': re.compile("^https://www.udemy.com/")}):                # href="../www.udemy.com/" olan linkleri tut
                        gelen_udemy = udemy_linkler['href']                             # dönen verideki linkleri tut
                        udemy_link.append(gelen_udemy)                                  # Tablomuza Yerleştir
                        ####self.logo.setText(gelen_udemy)                        # Ekrana Yaz
                        #sleep(1)                                                        # Bekleme Ver
            #-----------------------------------------------------------------------------------------------------------------------#

        #-------------------------------------------------------------------------------------------------------------------------#
        for adet in range(0, len(udemy_baslik)):                    # 0'dan Başlayarak, Dönen "başlık" sayısı kadar "adet" oluştur
            gelen_udemy_kaydet = open("DiscUdemy.txt", "a+")        # .txt oluştur
            gelen_udemy_kaydet.write(f"{udemy_baslik[adet]}\n")     # Başlık[adet] yaz satır atla
            gelen_udemy_kaydet.write(f"{udemy_link[adet]}\n\n")     # Link[adet] Yaz satır atla, satır atla
            gelen_udemy_kaydet.close()                              # dosyayı kapat
        #-------------------------------------------------------------------------------------------------------------------------#

        #---------------------------------------------------------------------------#
        icerik = open("DiscUdemy.txt", "r+").read()                 # Dosyayı oku   #
        self.alinanKurslar.setText(icerik)                          # Ekrana Yaz    #
        #---------------------------------------------------------------------------#
        
        #---------------------------------------------------------------------------------------------#
        satir_say = open("DiscUdemy.txt")
        satir = 0
        for line in satir_say:
            satir = satir+1
        satir_bilgi = "\n\t Bulunup, Yazılan Link Sayısı >>" + f"{int(satir/3)}"
        #####self.alinanKurslar.textChanged(satir_bilgi) #setText(satir_bilgi)     # Ekrana Yaz
        satir_say.close()
        os.remove("DiscUdemy.txt")                                  # Dosyayı Sil   
        #---------------------------------------------------------------------------------------------#

    def RealDiscount(self):
        for sayfa in range(1, int(self.cekilecekSayfa.text())):
            sayfa = str(sayfa)                                  # int olan değerimizi str yapıyoruz
            link = 'https://www.real.discount/new/' + sayfa     # sayfalar arasında gezinmek için
            kimlik = {'User-Agent': '@KekikAkademi'}            # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
            html = requests.get(link, headers=kimlik)           # link'in içerisindeki bütün html dosyasını indiriyoruz.
            kaynak = BeautifulSoup(html.text, "html5lib")       # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
            for discount_linkler in kaynak.findAll('a', attrs={'href': re.compile("^https://www.real.discount/offer/")}):
                gelen_discount = discount_linkler['href']

                udemy_html = requests.get(gelen_discount, headers=kimlik)
                udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')
                for udemy_linkler in udemy_kaynak.findAll('a', attrs={
                    'href': re.compile("^https://www.udemy.com/")}):  # o sayfanın içindeki udemy linki
                    gelen_udemy = udemy_linkler['href']

                    ######################################################
                    gelen_udemy_kaydet = open("UdemyeGiderken.txt", "a")
                    gelen_udemy_kaydet.write(gelen_udemy + "\n")
                    gelen_udemy_kaydet.close()
                    ######################################################
        ###########################################################################
        lines_seen = set()              # holds lines already seen
        outfile = open("RealDiscount.txt", "a")
        for line in open("UdemyeGiderken.txt", "r"):
            if line not in lines_seen:  # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()
        os.remove("UdemyeGiderken.txt")
        ###########################################################################
        icerik = open("RealDiscount.txt", "r").read()
        self.alinanKurslar.setText(icerik)
        os.remove("RealDiscount.txt")

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = Pencere()                         # Pencereyi göster
    sys.exit(uygulama.exec())                   # çıkış yapıldığı zaman, uygulamayı kapat