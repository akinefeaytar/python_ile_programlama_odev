# Akın Efe Aytar - 20253006037
# Hafta 4 Lab Testleri - tests/test_akis.py

from itertools import islice, takewhile
import inspect
import pytest
from uzay_oyunu.akis import fibonacci


# ============================================================================
# Görev 1 Testleri: Fibonacci Üreteci (15 puan)
# ============================================================================

def test_fibonacci_ilk_uc_next():
    """next() çağrıları ile ilk üç değerin (0, 1, 1) geldiğini doğrular."""
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


def test_fibonacci_islice_ilk_oniki():
    """itertools.islice ile ilk 12 değerin beklenen liste olduğunu doğrular."""
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(islice(fibonacci(), 12)) == beklenen


def test_fibonacci_takewhile_yuzden_kucuk():
    """itertools.takewhile ile 100'den küçük değerlerin alındığını doğrular."""
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    sonuc = list(takewhile(lambda x: x < 100, fibonacci()))
    assert sonuc == beklenen
    # 89'dan sonraki değerin 144 olduğunu ve 100'den büyük olduğu için durduğunu kontrol et
    assert all(x < 100 for x in sonuc)


def test_fibonacci_tek_kullanimlik():
    """Aynı üreteçten ikinci list(islice(...)) çağrısının farklı sonuç verdiğini gösterir.

    Üreteçler durumlarını (internal state) korur ve tek kullanımlıktır (exhaustion).
    İkinci çağrıda baştan başlamaz, kaldığı yerden devam eder.
    """
    g = fibonacci()
    ilk_cagri = list(islice(g, 5))     # [0, 1, 1, 2, 3]
    ikinci_cagri = list(islice(g, 5))  # [5, 8, 13, 21, 34]

    assert ilk_cagri == [0, 1, 1, 2, 3]
    assert ikinci_cagri == [5, 8, 13, 21, 34]
    assert ilk_cagri != ikinci_cagri


def test_fibonacci_uretec_ve_docstring():
    """fibonacci fonksiyonunun üreteç olduğunu ve docstring içerdiğini doğrular."""
    g = fibonacci()
    assert inspect.isgenerator(g)
    assert fibonacci.__doc__ is not None
    assert len(fibonacci.__doc__.strip()) > 0
