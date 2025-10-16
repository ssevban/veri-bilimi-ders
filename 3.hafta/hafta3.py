# -*- coding: utf-8 -*-
"""
marketsales.py
excel veri seti üzerinde veri analizi işlemleri
her adım fonksiyon olarak tanımlanmıştır.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def yukle_veri(dosya_yolu):
    """excel verisini oku"""
    df = pd.read_excel(dosya_yolu)
    print("veri başarıyla yüklendi.")
    return df


def kopya_olustur(df):
    """orijinal verinin kopyası"""
    kopya = df.copy()
    print("veri kopyası oluşturuldu.")
    return kopya


def boyut_bul(df):
    """veri setinin boyutları"""
    print(f"satır sayısı: {df.shape[0]}, sütun sayısı: {df.shape[1]}")


def sutun_isimleri(df):
    """sütun isimlerini yazdır"""
    print("sütun isimleri:")
    print(df.columns.tolist())


def bilgi(df):
    """veri seti bilgileri"""
    print("veri seti bilgileri:")
    print(df.info())


def bos_deger_var_mi(df):
    """boş değer sorgulama"""
    print("boş değer var mı?:")
    print(df.isnull().values.any())


def sutun_bazli_deger_say(df):
    """her sütundaki değer sayısı"""
    print("her sütundaki değer sayısı:")
    print(df.count())


def toplam_deger_say(df):
    """toplam değer sayısı"""
    print("toplam değer sayısı:", df.count().sum())


def bos_sutun_isimleri(df):
    """boş değer olan sütunların isimleri"""
    boslar = df.columns[df.isnull().any()].tolist()
    print("boş değeri olan sütunlar:", boslar)


def farkli_tip_say(df):
    """kaç farklı veri tipi var"""
    print("veri tipleri:")
    print(df.dtypes.value_counts())


def essiz_tipler(df):
    """her sütundaki benzersiz değer sayısı"""
    print("benzersiz değer sayısı:")
    print(df.nunique())


def ilk_bes_satir(df):
    """ilk 5 satırı yazdır"""
    print(df.head())


def son_yedi_satir(df):
    """son 7 satırı yazdır"""
    print(df.tail(7))


def amount_price_line_info(df):
    """her satır için amount, price, linenettotal bilgilerini yaz"""
    print(df[['AMOUNT', 'PRICE', 'LINENETTOTAL']])


def linenet_gt_15(df):
    """LINENETTOTAL 15'ten büyük satırlar"""
    filtre = df[df['LINENETTOTAL'] > 15]
    print(filtre)


def balikesir_subesi(df):
    """branch 'Balıkesir Şubesi' olan satırlar"""
    balikesir = df[df['BRANCH'] == 'Balıkesir Subesi']
    print(balikesir)


# ---------------------------------------------------
# main fonksiyon
# ---------------------------------------------------

def ana():
    dosya = "MarketSales.xlsx"  # buraya kendi excel dosyanın yolunu yaz
    data = yukle_veri(dosya)
    df = kopya_olustur(data)
    boyut_bul(df)
    sutun_isimleri(df)
    bilgi(df)
    bos_deger_var_mi(df)
    sutun_bazli_deger_say(df)
    toplam_deger_say(df)
    bos_sutun_isimleri(df)
    farkli_tip_say(df)
    essiz_tipler(df)
    ilk_bes_satir(df)
    son_yedi_satir(df)
    amount_price_line_info(df)
    linenet_gt_15(df)
    balikesir_subesi(df)


if __name__ == "__main__":
    ana()
