"""
sorular1.py
"""

# 1) kod yorumlama
# class Araba bir şablondur (sınıf).
# __init__ metodu nesne oluşturulduğunda marka ve model bilgisini alır.
# bilgileri_yazdir() metodu ise bu bilgileri ekrana bastırır.
# örnek: Araba("Toyota", "Corolla") → araba1.marka="Toyota", araba1.model="Corolla"
# araba1.bilgileri_yazdir() çıktısı: Marka: Toyota, Model: Corolla

class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_yazdir(self):
        print(f"Marka: {self.marka}, Model: {self.model}")

araba1 = Araba("Toyota", "Corolla")
araba1.bilgileri_yazdir()

# 2) Dikdörtgen sınıfı – alan hesaplama
class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return self.genislik * self.yukseklik

dikdortgen1 = Dikdortgen(5, 10)
alan = dikdortgen1.alan_hesapla()
print(f"Dikdörtgenin alanı: {alan}")

# 3) Kare sınıfı – ekrana kare çizimi
class Kare:
    def __init__(self, kenar_uzunlugu):
        self.kenar_uzunlugu = kenar_uzunlugu

    def kareyi_yazdir(self):
        for _ in range(self.kenar_uzunlugu):
            print("* " * self.kenar_uzunlugu)

kare1 = Kare(5)
kare1.kareyi_yazdir()

# 4) HesapMakinesi – iki veya üç sayıyı toplama
class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        return sayi1 + sayi2

hesap = HesapMakinesi()
print("İki sayının toplamı:", hesap.topla(10, 20))
print("Üç sayının toplamı:", hesap.topla(10, 20, 30))

# 5) Merhaba sınıfı – "Merhaba Dünya"
class Merhaba:
    def merhaba_yazdir(self):
        print("Merhaba Dünya")

m = Merhaba()
m.merhaba_yazdir()
