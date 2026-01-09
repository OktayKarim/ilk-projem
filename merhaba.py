# Bu benim GitHub'daki ilk kodum!
import datetime

def karsilama_mesaji(isim):
    zaman = datetime.datetime.now()
    print(f"Merhaba {isim}!")
    print(f"GitHub'a hoş geldin. Bugün tarih: {zaman.strftime('%d-%m-%Y')}")
    print("Kodlama yolculuğunda başarılar dilerim!")

# Fonksiyonu çalıştırıyoruz
karsilama_mesaji("Ziyaretçi")
