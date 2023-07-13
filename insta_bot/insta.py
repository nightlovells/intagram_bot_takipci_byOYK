from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import smtplib
import os
import colorama
from colorama import Fore

print(Fore.RED + """
  ____                _           _   _              _____   ___  __
  / ___|_ __ ___  __ _| |_ ___  __| | | |__  _   _   / _ \ \ / / |/ /
 | |   | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | | | | | \ V /| ' / 
 | |___| | |  __/ (_| | ||  __/ (_| | | |_) | |_| | | |_| || | | . \ 
  \____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |  \___/ |_| |_|\_\
                                              |___/                                    

\n""")

print("""Bu program unlu kisileri takip eder/takipten cikar. Boylece saatte yaklasik 15 takipci getirir. Bu program
calisirken lütfen instagram hesabinizdan herhangi bir islem yapmayiniz. @omryk.to8\n""")

path = '/insta_bot/geckodriver.exe'
binary_path = '/Mozilla Firefox/firefox.exe'
service = Service(path)
options = Options()
options.binary_location = binary_path

options.add_argument('--headless')

browser = webdriver.Firefox(service=service, options=options)
browser.maximize_window()

browser.get('https://www.instagram.com')

time.sleep(6)

print("\n Hesabinizda iki faktorlu dogrulama varsa calismayacaktir\n")
kullanici_adi = input(Fore.LIGHTYELLOW_EX+"Kullanıcı adınızı giriniz: ")
sifre = input(Fore.LIGHTYELLOW_EX+"Şifrenizi giriniz: ")
islem = 1
sayac = 0
unfsayac = 0

try:
    kullanici = browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
    kullanici.send_keys(kullanici_adi)
    sifre_input = browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/label[1]/input[1]")
    sifre_input.send_keys(sifre)
    browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[3]/button[1]/div[1]").click()
    print(Fore.GREEN+"Giris Yapiliyor")
    time.sleep(10)
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    time.sleep(5)

    while True:
#------------------------------------------------------------------------------------------------------------------------------------------------------
        if islem == 1 and sayac==0:
                print("Takip etme islemi basliyor bu sure icinde instagramdan islem yapmayiniz...")
                time.sleep(7)
                #!Unlunun sayfasına gitme
                print("Dualipa takip edilmeye calisiliyor...")
                browser.get("https://www.instagram.com/dualipa/")
                time.sleep(15)
                #!Unlu takip etme
                browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                print(str(sayac)+" Dualipa takip edildi :)")
                print("\n")
                sayac = 1
                time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac == 1:
                        #!Unlunun sayfasına gitme
                        print("Selena Gomez takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/selenagomez/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" Selena Gomez takip edildi :)")
                        print("\n")
                        sayac = 2
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------ 
                if sayac == 2:
                        #!Unlunun sayfasına gitme
                        print("Messi takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/leomessi/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+ " Messi takip edildi :)")
                        print("\n")
                        sayac = 3
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------ 
                if sayac == 3:
                        #!Unlunun sayfasına gitme
                        print("taylorswift takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/taylorswift/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" taylorswift takip edildi :)")
                        print("\n")
                        sayac = 4
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------ 
                if sayac == 4:
                        #!Unlunun sayfasına gitme
                        print("instagram takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/instagram/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" Instagram takip edildi :)")
                        print("\n")
                        sayac = 5
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac ==5:
                        #!Unlunun sayfasına gitme
                        print("ladygaga takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/ladygaga/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" Ladygaga takip edildi :)")
                        print("\n")
                        sayac = 6
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac == 6:
                        #!Unlunun sayfasına gitme
                        print("madonna takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/madonna/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" Madonna takip edildi :)")
                        print("\n")
                        sayac = 7
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac == 7:
                        #!Unlunun sayfasına gitme
                        print("leonardodicaprio takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/leonardodicaprio/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" leonardodicaprio takip edildi :)")
                        print("\n")
                        sayac = 8
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac == 8:
                        #!Unlunun sayfasına gitme
                        print("mileycyrus takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/mileycyrus/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" mileycyrus takip edildi :)")
                        print("\n")
                        sayac = 9
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac == 9:
                        #!Unlunun sayfasına gitme
                        print("cristiano takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/cristiano/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" critsiano takip edildi :)")
                        print("\n")
                        sayac = 10
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac == 10:
                        #!Unlunun sayfasına gitme
                        print("neymar takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/neymarjrsiteoficial/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" neymar takip edildi :)")
                        print("\n")
                        sayac = 11
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if sayac == 11:
                        #!Unlunun sayfasına gitme
                        print("kimkardashian takip edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/kimkardashian/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        print(str(sayac)+" kimkardashian takip edildi :)")
                        print("\n")
                        sayac = 0
                        time.sleep(5)
                        islem = 0
#------------------------------------------------------------------------------------------------------------------------------------------------------
        elif islem == 0:
                os.system("cls")
                print("TAKIP ISLEMLERI BASARIYLA TAMAMLANDI")
                print("2 DAKIKA SONRA TAKIPTEN CIKMA ISLEMLERI BASLAYACAKTIR 120sny")
                print("\n")
                time.sleep(120)
                unfsayac = 1
#------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac == 1:
                        print("TAKIPTEN CIKMA ISLEMLERI BASLADI...")
                        time.sleep(7)
                        #!Unlunun sayfasına gitme
                        print("Dualipa unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/dualipa/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" Dualipa unfollow edildi :)")
                        print("\n")
                        unfsayac = 2
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac== 2:
                        #!Unlunun sayfasına gitme
                        print("Selena Gomez unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/selenagomez/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" Selena Gomez unfollow edildi :)")
                        print("\n")
                        unfsayac = 3
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------ 
                if unfsayac == 3:
                        #!Unlunun sayfasına gitme
                        print("Messi unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/leomessi/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" Messi unfollow edildi :)")
                        print("\n")
                        unfsayac = 4
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------ 
                if unfsayac == 4:
                        #!Unlunun sayfasına gitme
                        print("taylorswift unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/taylorswift/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" taylorswift unfollow edildi :)")
                        print("\n")
                        unfsayac = 5
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------ 
                if  unfsayac == 5:
                        #!Unlunun sayfasına gitme
                        print("instagram unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/instagram/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" Instagram unfollow edildi :)")
                        unfsayac = 6
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac == 6:
                        #!Unlunun sayfasına gitme
                        print("ladygaga unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/ladygaga/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" Ladygaga unfollow edildi :)")
                        print("\n")
                        unfsayac = 7
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac == 7:
                        #!Unlunun sayfasına gitme
                        print("madonna unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/madonna/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" Madonna unfollow edildi :)")
                        print("\n")
                        unfsayac = 8
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac == 8:
                        #!Unlunun sayfasına gitme
                        print("leonardodicaprio unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/leonardodicaprio/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" leonardodicaprio unfollow edildi :)")
                        print("\n")
                        unfsayac = 9
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac == 9:
                        #!Unlunun sayfasına gitme
                        print("mileycyrus unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/mileycyrus/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" mileycyrus unfollow edildi :)")
                        print("\n")
                        unfsayac = 10
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac == 10: 
                        #!Unlunun sayfasına gitme
                        print("cristiano unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/cristiano/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" critsiano unfollow edildi :)")
                        print("\n")
                        unfsayac = 11
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac == 11:
                        #!Unlunun sayfasına gitme
                        print("neymar unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/neymarjrsiteoficial/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" neymar unfollow edildi :)")
                        print("\n")
                        unfsayac = 12
                        time.sleep(5)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
                if unfsayac== 12:
                        #!Unlunun sayfasına gitme
                        print("kardashian unfollow edilmeye calisiliyor...")
                        browser.get("https://www.instagram.com/kimkardashian/")
                        time.sleep(15)
                        #!Unlu takip etme
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
                        time.sleep(8)
                        browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        print(str(unfsayac)+" kimkardashian unfollow edildi :)")
                        unfsayac = 1
                        time.sleep(5)
                print("TAKIPTEN CIKMA ISLEMI TAMAMLANDI 120 SANIYE SONRA TAKIP ETME ISLEMI BASLAYACAKTIR 120sny")
                time.sleep(120)
                print("\n")
                islem = 1
        #------------------------------------------------------------------------------------------------------------------------------------------------------
except Exception as e:
    onarildi = 0
    print("Program bir hata ile karsilasti onarilmaya calisiliyor...")
    browser.close()
    time.sleep(10)
    browser.get('https://www.instagram.com')
    time.sleep(15)
    kullanici = browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
    kullanici.send_keys(kullanici_adi)
    sifre_input = browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/label[1]/input[1]")
    sifre_input.send_keys(sifre)
    browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[3]/button[1]/div[1]").click()
    print(Fore.GREEN+"Giris Yapiliyor")
    time.sleep(10)
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    time.sleep(5)
    onarildi = 1

    if onarildi == 1:
            print("Program basariyla onarildi islemleriniz birazdan devam edecektir...")
            time.sleep(8)

    elif onarildi == 0:
        print("Program onarilamadi internet baglantinizi ve sifrenizi kontrol edip tekrar deneyiniz...")

    islem = islem    
    sayac = sayac
    unfsayac = unfsayac

