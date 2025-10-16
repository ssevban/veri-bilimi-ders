"""
sorular2.py
"""

# temel sınıf
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"{self.ad} diyor ki: Merhaba, ben bir insanım.")


# alt sınıf – hoca
class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    # metodu override ediyoruz
    def konus(self):
        print(f"Hoca {self.ad}: Öğrenciler, derse hoş geldiniz!")

    def ders_ver(self):
        print(f"Hoca {self.ad} (sicil: {self.sicil_no}) şu anda ders veriyor.")


# alt sınıf – sekreter
class Sekreter(Insan):
    def __init__(self, ad, yas, ofis_no):
        super().__init__(ad, yas)
        self.ofis_no = ofis_no

    def konus(self):
        print(f"Sekreter {self.ad}: Merhaba, nasıl yardımcı olabilirim?")

    def toplantiyi_duzenle(self):
        print(f"Sekreter {self.ad} ofis {self.ofis_no}'da toplantıyı düzenliyor.")


# alt sınıf – öğrenci
class Ogrenci(Insan):
    def __init__(self, ad, yas, ogr_no, bolum):
        super().__init__(ad, yas)
        self.ogr_no = ogr_no
        self.bolum = bolum

    def konus(self):
        print(f"Öğrenci {self.ad}: Merhaba hocam, ben {self.bolum} bölümündeyim.")

    def ders_calıs(self):
        print(f"Öğrenci {self.ad} ({self.ogr_no}) ders çalışıyor.")


# örnek kullanım
if __name__ == "__main__":
    insan = Insan("Ahmet", 30)
    insan.konus()

    hoca = Hoca("Mehmet", 45, "H123")
    hoca.konus()
    hoca.ders_ver()

    sekreter = Sekreter("Ayşe", 35, "B-204")
    sekreter.konus()
    sekreter.toplantiyi_duzenle()

    ogrenci = Ogrenci("Zeynep", 20, "O567", "Bilgisayar Mühendisliği")
    ogrenci.konus()
    ogrenci.ders_calıs()
