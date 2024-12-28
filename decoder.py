import pyperclip  # pyperclip modülünü import ediyoruz

# Sezar şifre çözme fonksiyonu
def sezar_coz(metin, kaydirma):
    orijinal_metin = ""
    
    for karakter in metin:
        # Büyük harfler için işlem
        if karakter.isupper():
            yeni_karakter = chr(((ord(karakter) - ord('A') - kaydirma) % 26) + ord('A'))
            orijinal_metin += yeni_karakter
        # Küçük harfler için işlem
        elif karakter.islower():
            yeni_karakter = chr(((ord(karakter) - ord('a') - kaydirma) % 26) + ord('a'))
            orijinal_metin += yeni_karakter
        # Diğer karakterleri olduğu gibi ekleyelim (boşluklar, noktalama işaretleri vs.)
        else:
            orijinal_metin += karakter

    return orijinal_metin

# Komut satırından şifreli metin ve kaydırma miktarını al
if __name__ == "__main__":
    metin = input("Çözülecek şifreli metni girin: ")
    
    # Kaydırma miktarını al (0-25 arasında)
    while True:
        try:
            kaydirma = int(input("Kaydırma miktarını (0-25) arasında bir değer girin: "))
            if 0 <= kaydirma <= 25:
                break
            else:
                print("Lütfen 0 ile 25 arasında bir değer girin.")
        except ValueError:
            print("Geçersiz bir sayı girdiniz. Lütfen 0 ile 25 arasında bir değer girin.")

    # Şifreli metni çöz
    orijinal_metin = sezar_coz(metin, kaydirma)

    # Çözülmüş metni panoya kopyala
    pyperclip.copy(orijinal_metin)

    # Kullanıcıya çözülmüş metnin kopyalandığını bildir
    print(f"Çözülmüş metin: {orijinal_metin}")
    print("Çözülmüş metin panoya kopyalandı! Şimdi Ctrl+V ile yapıştırabilirsiniz.")
