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
pencere_basligi = "@KekikAkademi GUI Taslak"                    # Pencere Başlığımız                    #
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
        baslik = QLabel("")
        sistem = QLabel("")
        logo = QLabel()
        self.donenYazi = QTextEdit()
        self.girilenYazi = QLineEdit("Yazı Girin")
        buton_1 = QPushButton()
        buton_2 = QPushButton()

        # Başlık
        baslik.setText(f'<h1><font color="green">{pencere_basligi}</font></h1>')
        baslik.setFont(QFont("Helvatica",15,QFont.Bold))
        baslik.setAlignment(Qt.AlignCenter)

        # Sistem
        sistem.setText(ust_bilgi)
        sistem.setFont(QFont("Courier",12,QFont.Bold))
        sistem.setAlignment(Qt.AlignCenter)

        # Logo
        logo.setPixmap(QPixmap(r"img/KekikAkademiQt5Logo.png").scaled(700,250))
        logo.setAlignment(Qt.AlignCenter)

        # buton_1
        buton_1.setIcon(QIcon(r"img/buton_1.png"))
        buton_1.setText("buton_1")

        # buton_2
        buton_2.setIcon(QIcon(r"img/buton_2.png"))
        buton_2.setText("buton_2")

        # Horizontal Box
        h_box = QHBoxLayout()
        h_box.addWidget(self.girilenYazi)
        #h_box.addStretch()                              # Dikey dinamik uzaklığı koru
        h_box.addWidget(buton_1)
        #h_box.addStretch()                              # Dikey dinamik uzaklığı koru
        h_box.addWidget(buton_2)

        # Vertical Box
        v_box = QVBoxLayout()
        v_box.addWidget(baslik)
        v_box.addWidget(sistem)
        v_box.addWidget(logo)
        v_box.addWidget(self.donenYazi)
        v_box.addLayout(h_box)

        buton_1.clicked.connect(self.Buton_1_Tiklandi)
        buton_2.clicked.connect(self.Buton_2_Tiklandi)

        self.setLayout(v_box)
#########################################################
        self.show()                                     # Pencereyi göster
        self.setWindowTitle(f"{pencere_basligi}")       # Pencere Başlığımızı Belirledik
        self.setWindowIcon(QIcon("img/kekik.png"))      # Pencere İkonumuzu Belirledik
        self.setMinimumSize(QSize(750, 500))            # Pencere Min. Ebat Tanımladık
        self.setMaximumSize(QSize(750, 750))            # Pencere Max. Ebat Tanımladık
        #pencere.setGeometry(700,300,500,500)            # 700x300 kordinatında başlayarak / 500x500 ebatında aç

    def Buton_1_Tiklandi(self):
        gelen = self.girilenYazi.text()
        self.donenYazi.setText(f"Bunu Yazdın : {gelen}")

    def Buton_2_Tiklandi(self):
        gelen = self.girilenYazi.text()
        self.donenYazi.setText(f"Bunu Yazdın : {gelen}")

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = Pencere()                         # Pencereyi göster
    sys.exit(uygulama.exec())                   # çıkış yapıldığı zaman, uygulamayı kapat