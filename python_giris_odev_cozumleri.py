"""
python giriş – ödev çözümleri
kaynak pdf: "python giriş.pdf"
bu dosya, pdf içindeki "sorular" bölümlerinin tümüne net cevapları içerir
ve bazı sorular için kısa doğrulama/demonstrasyon kodları da ekler.

"""

from dataclasses import dataclass

# ---------------------------------------------------------
# bölüm 1: sayfa ~17 civarı çoktan seçmeli sorular
# ---------------------------------------------------------

@dataclass(frozen=True)
class Answer:
    secenek: str
    aciklama: str

bolum1_cevaplar = {
    1: Answer("B", "python'da sınıf tanımlamak için 'class' anahtar kelimesi kullanılır."),
    2: Answer("E", "chromepy bir editör/ide değildir; diğer seçeneklerle python kodu yazılabilir."),
    3: Answer("C", "aynı sınıftan birden çok nesne türetilebilir; 'türetilmez' ifadesi yanlıştır."),
    4: Answer("B", "python dosya uzantısı .py'dir."),
    5: Answer("B", "fonksiyon 'def fonksiyon_adi()' ile oluşturulur."),
    6: Answer("C", "oop bağlamında benzersiz örnek üretimi 'constructor' (yapıcı) ile ilişkilidir."),
}

# ---------------------------------------------------------
# bölüm 2: sayfa ~27 civarı sorular
# ---------------------------------------------------------

bolum2_cevaplar = {
    "encapsulation_tanimi": Answer(
        "C",
        "encapsulation; veriyi/metotları dış müdahaleden saklayıp kontrollü erişim sağlamaktır."
    ),
    "miras_iliskisi_A_B": Answer(
        "B",
        "class B(A): ifadesinde B, A'dan miras alır."
    ),
    "abstract_tanim": Answer(
        "B",
        "soyut sınıf; nesnesi oluşturmaya kapalı, kalıtım için şablon sağlayan sınıftır."
    ),
    "cikti_sesVer": Answer(
        "—",
        "a.sesVer() -> 'ses çıkarırlar' ;  k.sesVer() -> 'miyav' (override)"
    ),
}

# ---------------------------------------------------------
# demonstrasyon: encapsulation, inheritance, override, abstract
# (sorulardaki kavramları kısa kodlarla doğruluyoruz)
# ---------------------------------------------------------
# 1) encapsulation (özel alan + getter/setter)
class Banka2:
    def __init__(self, isim: str, para: int, adres: str):
        self.__isim = isim
        self.__para = para
        self.__adres = adres

    def get_para(self) -> int:
        return self.__para

    def set_para(self, miktar: int) -> None:
        self.__para = int(miktar)

# 2) inheritance + override
class Animal:
    def ses_ver(self):
        print("ses çıkarırlar")

class Kedi(Animal):
    def ses_ver(self):
        print("miyav")

# 3) abstract class örneği
from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def yuru(self) -> None: ...
    @abstractmethod
    def kos(self) -> None: ...

class Kus(AbstractAnimal):
    def yuru(self) -> None:
        # Kuşlar tipik olarak az yürür; sadece örnek çıktı
        print("kuslar pek yürümez")
    def kos(self) -> None:
        # Kuşlar genelde koşmaz; sadece örnek çıktı
        print("kuslar pek koşmaz")

def yazdir_baslik(metin: str):
    print("\n" + "-"*60)
    print(metin)
    print("-"*60)

def yazdir_bolum1():
    yazdir_baslik("bölüm 1 – çoktan seçmeli cevaplar")
    for k in sorted(bolum1_cevaplar.keys()):
        a = bolum1_cevaplar[k]
        print(f"soru {k}: seçenek = {a.secenek} | açıklama: {a.aciklama}")

def yazdir_bolum2():
    yazdir_baslik("bölüm 2 – kavramsal ve kod soruları")
    for k, a in bolum2_cevaplar.items():
        print(f"{k}: {a.secenek} | {a.aciklama}")

def demo():
    yazdir_baslik("demo – encapsulation")
    h = Banka2("sinan", 1000, "istanbul")
    print("başlangıç bakiye:", h.get_para())
    h.set_para(750)
    print("güncel bakiye:", h.get_para())

    yazdir_baslik("demo – inheritance + override")
    a = Animal()
    a.ses_ver()   # beklenen: ses çıkarırlar
    k = Kedi()
    k.ses_ver()   # beklenen: miyav

    yazdir_baslik("demo – abstract class")
    b = Kus()
    b.yuru()
    b.kos()

if __name__ == "__main__":
    yazdir_bolum1()
    yazdir_bolum2()
    demo()
