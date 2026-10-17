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


# ============================================================================
# Görev 2 Testleri: Yakıt Göstergesi (20 puan)
# ============================================================================

from uzay_oyunu.akis import yakit_gostergesi


def test_yakit_gostergesi_ornek_cikti():
    """PDF'teki örnek list(yakit_gostergesi(100, 30)) çıktısını doğrular: [70, 40, 10, 0]"""
    sonuc = list(yakit_gostergesi(100, 30))
    assert sonuc == [70, 40, 10, 0]


def test_yakit_gostergesi_stop_iteration():
    """Yakıt 0'a indikten sonra next() çağrıldığında StopIteration fırlatıldığını doğrular."""
    g = yakit_gostergesi(100, 60)
    assert next(g) == 40
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


def test_yakit_gostergesi_tam_kat():
    """Yakıt tüketimin tam katı olduğunda son adımda tam 0 üretilip durduğunu doğrular."""
    g = yakit_gostergesi(20, 10)
    assert next(g) == 10
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


def test_yakit_gostergesi_tek_adimda_tukenme():
    """Tüketim mevcut yakıttan büyükse 0 üretip ardından StopIteration fırlattığını doğrular."""
    g = yakit_gostergesi(50, 100)
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


def test_yakit_gostergesi_uretec_ve_docstring():
    """yakit_gostergesi'nin generator olduğunu ve docstring içerdiğini doğrular."""
    g = yakit_gostergesi(100, 10)
    assert inspect.isgenerator(g)
    assert yakit_gostergesi.__doc__ is not None
    assert len(yakit_gostergesi.__doc__.strip()) > 0

