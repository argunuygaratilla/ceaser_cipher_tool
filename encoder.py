import pyperclip  # pyperclip modülünü import ediyoruz

# İngilizce harflerle Sezar şifrelemesi fonksiyonu
def sezar_sifrele(metin, kaydirma):
    sifreli_metin = ""
    
    for karakter in metin:
        # Büyük harfler için işlem
        if karakter.isupper():
            yeni_karakter = chr(((ord(karakter) - ord('A') + kaydirma) % 26) + ord('A'))
            sifreli_metin += yeni_karakter
        # Küçük harfler için işlem
        elif karakter.islower():
            yeni_karakter = chr(((ord(karakter) - ord('a') + kaydirma) % 26) + ord('a'))
            sifreli_metin += yeni_karakter
        # Diğer karakterleri olduğu gibi ekleyelim (boşluklar, noktalama işaretleri vs.)
        else:
            sifreli_metin += karakter

    return sifreli_metin

# Kullanıcıdan metin ve kaydırma miktarını al
metin = input("Şifrelenecek metni girin: ")

# Kaydırma miktarını al (0-25 arasında)
while True:
    try:
        kaydirma = int(input("Kaydırma miktarını (0-25) arasında bir değer olarak girin: "))
        if 0 <= kaydirma <= 25:
            break
        else:
            print("Lütfen 0 ile 25 arasında bir değer girin.")
    except ValueError:
        print("Geçersiz bir sayı girdiniz. Lütfen 0 ile 25 arasında bir değer girin.")

# Şifreli metni al
sifreli_metin = sezar_sifrele(metin, kaydirma)

# Şifreli metni panoya kopyala
pyperclip.copy(sifreli_metin)

# Kullanıcıya şifreli metnin kopyalandığını bildir
print(f"Şifreli metin: {sifreli_metin}")
print("Şifreli metin panoya kopyalandı! Şimdi Ctrl+V ile yapıştırabilirsiniz.")
