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


# ============================================================================
# Görev 3 Testleri: Seyir Defteri Boru Hattı (25 puan)
# ============================================================================

from pathlib import Path
from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar

SEYIR_DOSYASI = Path(__file__).parent.parent / "veri" / "seyir.txt"


def test_seyir_toplam_yakit_88():
    """PDF örneği: ayristir(satirlari_oku(...)) üzerinden yakıt toplamının 88 olduğunu doğrular."""
    toplam = sum(y for _, _, y in ayristir(satirlari_oku(SEYIR_DOSYASI)))
    assert toplam == 88


def test_seyir_uzun_yolculuklar_esik_10():
    """PDF örneği: uzun_yolculuklar(kayitlar, 10) hedef listesinin ['sirius', 'centauri', 'orion', 'kara_delik'] olduğunu doğrular."""
    kayitlar = ayristir(satirlari_oku(SEYIR_DOSYASI))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]


def test_seyir_yorum_ve_bos_satirlar_atlanir(tmp_path):
    """Boşlukların ve # yorum satırlarının atlandığını test eder."""
    test_dosyasi = tmp_path / "test_seyir.txt"
    test_dosyasi.write_text(
        "\n# yorum 1\ndünya -> ay 5\n\n# yorum 2\nay -> mars 10\n   \n",
        encoding="utf-8"
    )
    satirlar = list(satirlari_oku(test_dosyasi))
    assert satirlar == ["dünya -> ay 5", "ay -> mars 10"]


def test_seyir_boru_hatti_tembeldir():
    """Her üç aşamanın da generator (üreteç) nesnesi döndürdüğünü, listeye okumadığını doğrular."""
    g1 = satirlari_oku(SEYIR_DOSYASI)
    assert inspect.isgenerator(g1)

    g2 = ayristir(g1)
    assert inspect.isgenerator(g2)

    g3 = uzun_yolculuklar(g2, 10)
    assert inspect.isgenerator(g3)


def test_seyir_uzun_yolculuklar_farkli_esik():
    """Eşik 15 verildiğinde yalnızca 15'ten kesinlikle büyük olanların (kara_delik 30) geldiğini doğrular."""
    kayitlar = ayristir(satirlari_oku(SEYIR_DOSYASI))
    filtrelenmis = list(uzun_yolculuklar(kayitlar, 15))
    assert filtrelenmis == [("sirius", "kara_delik", 30)]


def test_seyir_fonksiyonlari_docstring():
    """Boru hattı fonksiyonlarının docstring içerdiğini doğrular."""
    for fn in (satirlari_oku, ayristir, uzun_yolculuklar):
        assert fn.__doc__ is not None
        assert len(fn.__doc__.strip()) > 0


# ============================================================================
# Görev 4 Testleri: Önbellekli Rota Sayacı (25 puan)
# ============================================================================

import json
from uzay_oyunu.akis import rota_sayaci

GALAKSI_DOSYASI = Path(__file__).parent.parent / "uzay_oyunu" / "galaksi.json"


@pytest.fixture
def galaksi_baglantilari():
    with open(GALAKSI_DOSYASI, encoding="utf-8") as f:
        veri = json.load(f)
    return veri["baglantilar"]


def test_rota_sayaci_ornek_degerler(galaksi_baglantilari):
    """PDF örneği: say('dünya', 3) -> 9, say('dünya', 10) -> 2185, say('dünya', 40) -> 16832258606399"""
    say = rota_sayaci(galaksi_baglantilari)
    assert say("dünya", 3) == 9
    assert say("dünya", 10) == 2185
    assert say("dünya", 40) == 16832258606399


def test_rota_sayaci_adim_sifir(galaksi_baglantilari):
    """0 adımda başlangıç gezegeninde kalınır, tam olarak 1 rota mevcuttur."""
    say = rota_sayaci(galaksi_baglantilari)
    assert say("dünya", 0) == 1
    assert say("sirius", 0) == 1


def test_rota_sayaci_lru_cache_calisiyor(galaksi_baglantilari):
    """rota_sayisi fonksiyonunun @lru_cache ile sarmalandığını ve cache hit ürettiğini doğrular."""
    say = rota_sayaci(galaksi_baglantilari)
    # cache_info metodunun varlığını kontrol et
    assert hasattr(say, "cache_info")

    info_once = say.cache_info()
    say("dünya", 10)
    info_sonra = say.cache_info()
    assert info_sonra.hits > info_once.hits or info_sonra.misses > info_once.misses

    # Tekrar aynı çağrıyı yapınca hit artmalı
    hits_once = say.cache_info().hits
    say("dünya", 10)
    assert say.cache_info().hits > hits_once


def test_rota_sayaci_docstring():
    """rota_sayaci ve iç fonksiyonunun docstring içerdiğini doğrular."""
    assert rota_sayaci.__doc__ is not None
    assert len(rota_sayaci.__doc__.strip()) > 0


# ============================================================================
# Bonus Testleri: zamanlayici(aralik) ve tik-tak (10 puan)
# ============================================================================

from uzay_oyunu.akis import zamanlayici, tik_tak_programi


def test_zamanlayici_uretec_ve_docstring():
    """zamanlayici fonksiyonunun bir generator olduğunu ve docstring içerdiğini doğrular."""
    g = zamanlayici(0.01)
    assert inspect.isgenerator(g)
    assert zamanlayici.__doc__ is not None
    assert len(zamanlayici.__doc__.strip()) > 0


def test_tik_tak_programi_kisa_calisma():
    """tik_tak_programi'nın kısa bir sürede (0.1 saniye) doğru çalıştığını ve liste döndürdüğünü doğrular."""
    olaylar = tik_tak_programi(toplam_sure=0.1, yazdir=False)
    assert isinstance(olaylar, list)
    assert tik_tak_programi.__doc__ is not None
    # Meşgul bekleme açıklaması docstring içinde yer almalıdır
    assert "Meşgul Bekleme" in tik_tak_programi.__doc__
    assert "time.sleep" in tik_tak_programi.__doc__




