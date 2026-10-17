# Akın Efe Aytar - 20253006037
# İleri Python Programlama - Hafta 4 Lab: Görev 5 (map, filter, reduce, partial)

from functools import reduce, partial
from typing import Callable


# ============================================================================
# OKUNABİLİRLİK VE YAZIM TERCİHİ DEĞERLENDİRMESİ:
#
# Python topluluğu ve PEP 20 (The Zen of Python - "Readability counts")
# prensiplerine uygun olarak, liste üreteçleri (list comprehensions) ve gömülü
# sum() fonksiyonunu map/filter/reduce yaklaşımlarına kıyasla çok daha okunaklı,
# temiz ve anlaşılır buluyorum.
#
# Gerekçeler:
# 1. Lambda Kirliliğinin Önlenmesi: filter ve reduce fonksiyonlarında koşul veya
#    biriktirme kuralı belirtmek için sıklıkla 'lambda' ifadelerine başvurulur.
#    Bu durum kodun görsel sadeliğini bozar. Liste üreteçlerinde ise 'if' koşulu
#    veya dönüşüm doğrudan doğal dil akıcılığında (ör. [g for g in ... if ...]) yazılır.
# 2. list() Sarmalama İhtiyacının Olmaması: Python 3'te map ve filter tembel
#    üreteçler döndürdüğü için bunları listeye çevirmek adına 'list(filter(...))'
#    şeklinde iç içe parantezli yapılar gerekir. Liste kavrayımı doğrudan [ ... ]
#    ile nihai listeyi üretir.
# 3. İfade Açıklığı: 'reduce(lambda acc, g: acc + len(...), ...)' yerine
#    'sum(len(...) for ...)' yazmak hem matematiksel niyeti anında gösterir hem de
#    hata yapma riskini minimuma indirir.
# ============================================================================


# ----------------------------------------------------------------------------
# Soru 1: Gezegen adlarının büyük harfli listesi
# ----------------------------------------------------------------------------

def gezegenleri_buyut_map(galaksi: dict) -> list[str]:
    """map() fonksiyonunu kullanarak gezegen adlarını büyük harfe çevirir.

    Args:
        galaksi: Gezegenler listesini içeren galaksi sözlüğü.

    Returns:
        list[str]: Büyük harflerle yazılmış gezegen isimleri listesi.
    """
    return list(map(str.upper, galaksi["gezegenler"]))


def gezegenleri_buyut_kavrama(galaksi: dict) -> list[str]:
    """Liste üreteci (comprehension) kullanarak gezegen adlarını büyük harfe çevirir.

    Args:
        galaksi: Gezegenler listesini içeren galaksi sözlüğü.

    Returns:
        list[str]: Büyük harflerle yazılmış gezegen isimleri listesi.
    """
    return [g.upper() for g in galaksi["gezegenler"]]


# ----------------------------------------------------------------------------
# Soru 2: En az iki bağlantısı olan gezegenler
# ----------------------------------------------------------------------------

def en_az_iki_baglanti_filter(galaksi: dict) -> list[str]:
    """filter() fonksiyonunu kullanarak en az iki bağlantısı olan gezegenleri süzer.

    Args:
        galaksi: Gezegenler ve baglantilar içeren galaksi sözlüğü.

    Returns:
        list[str]: En az 2 bağlantısı olan gezegenlerin listesi.
    """
    baglantilar = galaksi["baglantilar"]
    return list(filter(lambda g: len(baglantilar[g]) >= 2, galaksi["gezegenler"]))


def en_az_iki_baglanti_kavrama(galaksi: dict) -> list[str]:
    """Liste üreteci kullanarak en az iki bağlantısı olan gezegenleri süzer.

    Args:
        galaksi: Gezegenler ve baglantilar içeren galaksi sözlüğü.

    Returns:
        list[str]: En az 2 bağlantısı olan gezegenlerin listesi.
    """
    baglantilar = galaksi["baglantilar"]
    return [g for g in galaksi["gezegenler"] if len(baglantilar[g]) >= 2]


# ----------------------------------------------------------------------------
# Soru 3: Toplam bağlantı sayısı
# ----------------------------------------------------------------------------

def toplam_baglanti_reduce(galaksi: dict) -> int:
    """functools.reduce kullanarak galaksideki toplam bağlantı sayısını hesaplar.

    Args:
        galaksi: Bağlantılar sözlüğünü içeren galaksi sözlüğü.

    Returns:
        int: Galaksideki toplam bağlantı ucu sayısı (örnek veri için 10).
    """
    baglantilar = galaksi["baglantilar"]
    return reduce(
        lambda toplam, g: toplam + len(baglantilar[g]),
        galaksi["gezegenler"],
        0,
    )


def toplam_baglanti_sum(galaksi: dict) -> int:
    """Gömülü sum() fonksiyonunu kullanarak galaksideki toplam bağlantı sayısını hesaplar.

    Args:
        galaksi: Bağlantılar sözlüğünü içeren galaksi sözlüğü.

    Returns:
        int: Galaksideki toplam bağlantı ucu sayısı (örnek veri için 10).
    """
    baglantilar = galaksi["baglantilar"]
    return sum(len(baglantilar[g]) for g in galaksi["gezegenler"])


# ----------------------------------------------------------------------------
# functools.partial: yolculuk ve hizli_yolculuk
# ----------------------------------------------------------------------------

def yolculuk(mesafe: float, hiz: float = 1.0) -> float:
    """Verilen mesafe ve hız için gereken yolculuk süresini hesaplar.

    Args:
        mesafe: Kat edilecek mesafe (ışık yılı / birim).
        hiz: Seyahat hızı katsayısı (varsayılan: 1.0).

    Returns:
        float: Yolculuk süresi (mesafe / hiz).
    """
    if hiz <= 0:
        raise ValueError("Hız 0 veya negatif olamaz.")
    return mesafe / hiz


# functools.partial ile hiz=3 sabitlenmiş hızlı yolculuk fonksiyonu
hizli_yolculuk: Callable[..., float] = partial(yolculuk, hiz=3)
