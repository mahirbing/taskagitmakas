import random

def tas_kagit_makas():
    while True:
        # Kullanıcı adı al
        kullanici_adi = input("Kullanıcı adınızı girin: ")
        
        # Skorları başlat
        kullanici_skor = 0
        bilgisayar_skor = 0
        
        # Olası seçimler
        secimler = ["taş", "kağıt", "makas"]
        
        print("Oyun başladı! 'puan durumu' yazarak puanınızı görebilir, 'çıkış' yazarak oyunu bitirebilirsiniz.")
        
        while True:
            # Kullanıcı seçimi
            kullanici_secimi = input("Taş, kağıt, makas seçin (veya komut girin): ").lower()
            
            if kullanici_secimi == "puan durumu":
                print(f"Skor: {kullanici_adi} {kullanici_skor} - {bilgisayar_skor} Bilgisayar")
                continue
            
            if kullanici_secimi == "çıkış":
                print("\nOyun Bitti!")
                print(f"Son Skor: {kullanici_adi} {kullanici_skor} - {bilgisayar_skor} Bilgisayar")
                print(f"İyi oyundu, eline sağlık {kullanici_adi}!")
                return

            if kullanici_secimi not in secimler:
                print("Geçersiz giriş! Lütfen 'taş', 'kağıt' veya 'makas' seçin ya da komut girin.")
                continue
            
            # Bilgisayarın rastgele seçimi
            bilgisayar_secimi = random.choice(secimler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
            
            # Kazananı belirleme
            if kullanici_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (
                (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or
                (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or
                (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt")
            ):
                print(f"{kullanici_adi}, kazandınız!")
                kullanici_skor += 1
            else:
                print(f"{kullanici_adi}, kaybettiniz!")
                bilgisayar_skor += 1

# Oyunu başlat
if __name__ == "__main__":
    tas_kagit_makas()

