# Akın Efe Aytar - 20253006037
# İleri Python Programlama - Hafta 4 Lab Ödevi: Üreteçler ve functools

from collections.abc import Generator, Iterable, Callable
from itertools import islice, takewhile
from pathlib import Path
from typing import Union
import time


# ============================================================================
# Görev 1 – Fibonacci üreteci (15 puan)
# ============================================================================

def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayı dizisini üreten üreteç (generator).

    0'dan başlayarak sırasıyla 0, 1, 1, 2, 3, 5, 8... sayılarını üretir.
    Üreteç yapısı sayesinde bellekte yer tutmaz ve sonsuz eleman üretebilir.

    Yields:
        int: Sıradaki Fibonacci sayısı.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# ============================================================================
# Görev 2 – Yakıt göstergesi (20 puan)
# ============================================================================

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her next() çağrısında yakıtı tuketim kadar azaltıp kalan yakıtı üreten üreteç.

    Yakıt 0'a indiğinde üreteç sonlanır (StopIteration). Kalan yakıt negatif
    olamaz; 0'ın altına inerse 0 olarak üretilir ve ardından durur.

    Args:
        yakit: Başlangıç yakıt miktarı.
        tuketim: Her adımda tüketilen yakıt miktarı.

    Yields:
        int: Kalan güncel yakıt miktarı.
    """
    kalan = yakit
    while kalan > 0:
        kalan -= tuketim
        if kalan < 0:
            kalan = 0
        yield kalan


# ============================================================================
# Görev 3 – Seyir defteri boru hattı (25 puan)
# ============================================================================

def satirlari_oku(yol: Union[str, Path]) -> Generator[str, None, None]:
    """Dosyayı satır satır tembel (lazy) okuyarak satırları üreten üreteç.

    Boş satırları ve '#' ile başlayan yorum satırlarını atlar.
    Bellek verimliliği için tüm dosyayı bir listeye okumaz (stream/generator).

    Args:
        yol: Okunacak dosya yolu (str veya Path).

    Yields:
        str: Temizlenmiş satır metni.
    """
    with open(yol, mode="r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz


def ayristir(
    satirlar: Iterable[str],
) -> Generator[tuple[str, str, int], None, None]:
    """Her satırdan (kaynak, hedef, yakit) demetini tembelce üreten üreteç.

    'dünya -> sirius 12' biçimindeki satırları ayrıştırır.

    Args:
        satirlar: Ham satırları sağlayan yinelenebilir (iterable) nesne.

    Yields:
        tuple[str, str, int]: (kaynak_gezegen, hedef_gezegen, harcanan_yakit).
    """
    for satir in satirlar:
        kaynak_kismi, hedef_yakit_kismi = satir.split("->")
        kaynak = kaynak_kismi.strip()
        hedef, yakit_str = hedef_yakit_kismi.strip().split()
        yield (kaynak, hedef, int(yakit_str))


def uzun_yolculuklar(
    kayitlar: Iterable[tuple[str, str, int]], esik: int
) -> Generator[tuple[str, str, int], None, None]:
    """Yakıt tüketimi verilen eşikten kesinlikle büyük olan kayıtları süzen üreteç.

    Args:
        kayitlar: (kaynak, hedef, yakit) demetlerini içeren yinelenebilir nesne.
        esik: Yakıt filtreleme alt sınırı (yakit > esik olanlar geçer).

    Yields:
        tuple[str, str, int]: Eşiği aşan yolculuk kaydı.
    """
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit


