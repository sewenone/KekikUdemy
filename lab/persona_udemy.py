from bs4 import BeautifulSoup as bs
import requests
import os,time,random
import telebot
#from urllib3.exceptions import InsecureRequestWarning # bazı ağlarda ssl hatası almamak için :)
###
bot = telebot.TeleBot("TelegramToken'iniz :)")
@bot.message_handler(["start"])

def basla(mesaj):
	print(f"Start alındı ! --> {mesaj.chat.id} | {mesaj.chat.username} | {mesaj.chat.first_name} || Grup Türü : {mesaj.chat.type}")
	bot.reply_to(mesaj,"Merhaba :\n/kurs ile ücretsiz udemy kurslarını sohbete çağırabilir\n/txt ile kursların txtlerini alabilirsin\n")

@bot.message_handler(["kurs"])
def kurs(mesaj):
	sayi = str(random.choice(range(1,16)))
	print(f"Kurs alındı ! --> {mesaj.chat.id} | {mesaj.chat.username} | {mesaj.chat.first_name} || Grup Türü : {mesaj.chat.type}")
	def_ici = "@depo_kurs_bot |\ndiscudemy Türkçe katagorisi 15 ile sınırlı\n/all ile tüm dillerden kurs çekin :)\n\n"
	link = "http://www.discudemy.com/language/turkish/"+sayi # sayfalar arasında gezinmek için
	html=requests.post(url=link) #Fatih ssl hatasi vermemesi icin
	##
	kaynak = bs(html.text,"html.parser") #bitifulsup ile html'i işlememiz gerekiyor . html.parser'i kullandık
	linkler = kaynak.find_all("a",attrs={"class":"card-header"}) # sınıf'ı kart-header olan tüm linkleri çekiyoruz bununla
	for i in linkler: # linkler listesini i olarak ayırdık
		i = i["href"] # i'nin hreflerini aldık (linkleri)
		i = i.split("/") # discudemy.com/katagori olan linki udemy.com olarak değiştirmemiz gerekiyor . Bunun için / 'ları bulduktan sonra buralardan bölüyoruz
		i = i[0] + "//www.udemy.com/course/"+i[4] 
		def_ici = def_ici+i+"\n"
	def_ici=def_ici+"\n---------"
	bot.reply_to(mesaj,def_ici)

@bot.message_handler(["all"])
def all(mesaj):
	sayi = str(random.choice(range(1,300)))
	print(f"ALL alındı ! --> {mesaj.chat.id} | {mesaj.chat.username} | {mesaj.chat.first_name} || Grup Türü : {mesaj.chat.type}")
	def_ici = "@depo_kurs_bot |\nTüm dillerin kursları listeleniyor\n/kurs ile Türkçe kursları çekin :)\n\n"
	link = "http://www.discudemy.com/all/"+sayi # sayfalar arasında gezinmek için
	html=requests.post(url=link) #Fatih ssl hatasi vermemesi icin
	##
	kaynak = bs(html.text,"html.parser") #bitifulsup ile html'i işlememiz gerekiyor . html.parser'i kullandık
	linkler = kaynak.find_all("a",attrs={"class":"card-header"}) # sınıf'ı kart-header olan tüm linkleri çekiyoruz bununla
	for i in linkler: # linkler listesini i olarak ayırdık
		i = i["href"] # i'nin hreflerini aldık (linkleri)
		i = i.split("/") # discudemy.com/katagori olan linki udemy.com olarak değiştirmemiz gerekiyor . Bunun için / 'ları bulduktan sonra buralardan bölüyoruz
		i = i[0] + "//www.udemy.com/course/"+i[4] 
		def_ici = def_ici+i+"\n"
	def_ici=def_ici+"\n---------"
	bot.reply_to(mesaj,def_ici)

@bot.message_handler(["txt"])
def txt(mesaj):
	sayi = str(random.choice(range(1,16)))
	print(f"txt alındı ! --> {mesaj.chat.id} | {mesaj.chat.username} | {mesaj.chat.first_name} || Grup Türü : {mesaj.chat.type}")
	bot.reply_to(mesaj,f"@depo_kurs_bot discudemy [sayfa:{sayi}]\nDil : TR\n\nTüm diller için :/txtall")
	def_ici = "@depo_kurs_bot |\n"
	link = "http://www.discudemy.com/language/turkish/"+sayi # sayfalar arasında gezinmek için
	html=requests.post(url=link)
	kaynak = bs(html.text,"html.parser") #bitifulsup ile html'i işlememiz gerekiyor . html.parser'i kullandık
	linkler = kaynak.find_all("a",attrs={"class":"card-header"}) # sınıf'ı kart-header olan tüm linkleri çekiyoruz bununla
	for i in linkler: # linkler listesini i olarak ayırdık
		i = i["href"] # i'nin hreflerini aldık (linkleri)
		i = i.split("/") # discudemy.com/katagori olan linki udemy.com olarak değiştirmemiz gerekiyor . Bunun için / 'ları bulduktan sonra buralardan bölüyoruz
		i = i[0] + "//www.udemy.com/course/"+i[4] 
		def_ici = def_ici+i+"\n"
	def_ici=def_ici+"\n---------"
	dosya = f"udemytrkurs[{sayi}]_{mesaj.chat.username}.txt"
	with open(dosya,"w") as yaz:yaz.write(def_ici)
	bot.send_document(mesaj.chat.id,open(dosya))

@bot.message_handler(["txtall"])
def txt(mesaj):
	sayi = str(random.choice(range(1,300)))
	print(f"txtall alındı ! --> {mesaj.chat.id} | {mesaj.chat.username} | {mesaj.chat.first_name} || Grup Türü : {mesaj.chat.type}")
	bot.reply_to(mesaj,f"@depo_kurs_bot discudemy [sayfa:{sayi}]\nDil : ALL\n\nSadece Türkçe için :/txt")
	def_ici = "@depo_kurs_bot |\n"
	link = "http://www.discudemy.com/all/"+sayi # sayfalar arasında gezinmek için
	html=requests.post(url=link)
	kaynak = bs(html.text,"html.parser") #bitifulsup ile html'i işlememiz gerekiyor . html.parser'i kullandık
	linkler = kaynak.find_all("a",attrs={"class":"card-header"}) # sınıf'ı kart-header olan tüm linkleri çekiyoruz bununla
	for i in linkler: # linkler listesini i olarak ayırdık
		i = i["href"] # i'nin hreflerini aldık (linkleri)
		i = i.split("/") # discudemy.com/katagori olan linki udemy.com olarak değiştirmemiz gerekiyor . Bunun için / 'ları bulduktan sonra buralardan bölüyoruz
		i = i[0] + "//www.udemy.com/course/"+i[4] 
		def_ici = def_ici+i+"\n"
	def_ici=def_ici+"\n---------"
	dosya = f"udemyallkurs[{sayi}]_{mesaj.chat.username}.txt"
	with open(dosya,"w") as yaz:yaz.write(def_ici)
	bot.send_document(mesaj.chat.id,open(dosya))

bot.polling()