# Akın Efe Aytar - 20253006037
# Görev 5 - closure ve lambda

import time


def hamle_sayaci():
    """Her çağrıda bir artan sayaç döndürür."""
    sayac = 0

    def artir():
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan sıralar, eşitse alfabetik."""
    baglantilar = galaksi["baglantilar"]
    return sorted(
        baglantilar.keys(),
        key=lambda p: (-len(baglantilar[p]), p)
    )


# Bonus - sure_olc

def sure_olc(fonksiyon):
    """Fonksiyonu sarıp çalışma süresini yazan sarmalayıcı döndürür."""
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        sure = time.perf_counter() - baslangic
        print(f"{fonksiyon.__name__} {sure:.6f} saniyede çalıştı")
        return sonuc
    return sarmalayici


en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
