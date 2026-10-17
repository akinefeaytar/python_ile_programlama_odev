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

