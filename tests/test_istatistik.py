# Akın Efe Aytar - 20253006037
# Hafta 4 Lab Testleri - tests/test_istatistik.py (Görev 5)

import json
from pathlib import Path
from functools import partial
import pytest
from uzay_oyunu.istatistik import (
    gezegenleri_buyut_map,
    gezegenleri_buyut_kavrama,
    en_az_iki_baglanti_filter,
    en_az_iki_baglanti_kavrama,
    toplam_baglanti_reduce,
    toplam_baglanti_sum,
    yolculuk,
    hizli_yolculuk,
)

GALAKSI_YOLU = Path(__file__).parent.parent / "uzay_oyunu" / "galaksi.json"


@pytest.fixture
def galaksi_verisi():
    with open(GALAKSI_YOLU, encoding="utf-8") as f:
        return json.load(f)


# ----------------------------------------------------------------------------
# 1. Gezegen adlarının büyük harfli listesi
# ----------------------------------------------------------------------------

def test_gezegenleri_buyut_ornek_cikti(galaksi_verisi):
    """PDF örneği: ['DÜNYA', 'CENTAURI', 'SIRIUS', 'ORION', 'KARA_DELIK']"""
    beklenen = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]
    assert gezegenleri_buyut_map(galaksi_verisi) == beklenen
    assert gezegenleri_buyut_kavrama(galaksi_verisi) == beklenen


def test_gezegenleri_buyut_iki_yol_ayni(galaksi_verisi):
    """map ve liste kavrayımı yöntemlerinin aynı sonucu verdiğini doğrular."""
    r_map = gezegenleri_buyut_map(galaksi_verisi)
    r_comp = gezegenleri_buyut_kavrama(galaksi_verisi)
    assert r_map == r_comp


# ----------------------------------------------------------------------------
# 2. En az iki bağlantısı olan gezegenler
# ----------------------------------------------------------------------------

def test_en_az_iki_baglanti_ornek_cikti(galaksi_verisi):
    """PDF örneği: ['dünya', 'centauri', 'sirius', 'orion'] (kara_delik 1 bağlantılı olduğu için elenir)"""
    beklenen = ["dünya", "centauri", "sirius", "orion"]
    assert en_az_iki_baglanti_filter(galaksi_verisi) == beklenen
    assert en_az_iki_baglanti_kavrama(galaksi_verisi) == beklenen


def test_en_az_iki_baglanti_iki_yol_ayni(galaksi_verisi):
    """filter ve liste kavrayımı yöntemlerinin aynı sonucu verdiğini doğrular."""
    r_filter = en_az_iki_baglanti_filter(galaksi_verisi)
    r_comp = en_az_iki_baglanti_kavrama(galaksi_verisi)
    assert r_filter == r_comp


# ----------------------------------------------------------------------------
# 3. Toplam bağlantı sayısı
# ----------------------------------------------------------------------------

def test_toplam_baglanti_ornek_cikti(galaksi_verisi):
    """PDF örneği: Galaksideki toplam bağlantı ucu sayısının 10 olduğunu doğrular."""
    assert toplam_baglanti_reduce(galaksi_verisi) == 10
    assert toplam_baglanti_sum(galaksi_verisi) == 10


def test_toplam_baglanti_iki_yol_ayni(galaksi_verisi):
    """reduce ve sum yöntemlerinin aynı toplamı ürettiğini doğrular."""
    r_reduce = toplam_baglanti_reduce(galaksi_verisi)
    r_sum = toplam_baglanti_sum(galaksi_verisi)
    assert r_reduce == r_sum


# ----------------------------------------------------------------------------
# 4. functools.partial: yolculuk ve hizli_yolculuk
# ----------------------------------------------------------------------------

def test_hizli_yolculuk_partial_ve_hesaplama():
    """hizli_yolculuk'un partial olduğunu ve hiz=3 ile çalıştığını doğrular."""
    assert isinstance(hizli_yolculuk, partial)
    assert hizli_yolculuk.keywords == {"hiz": 3}
    assert hizli_yolculuk.func == yolculuk

    # 30 birimlik yolculuk hiz=3 ile 10 birim sürmeli
    assert hizli_yolculuk(30) == 10.0
    # 9 birimlik yolculuk hiz=3 ile 3 birim sürmeli
    assert hizli_yolculuk(9) == 3.0


def test_yolculuk_varsayilan_hiz():
    """yolculuk fonksiyonunun varsayılan hızının 1.0 olduğunu doğrular."""
    assert yolculuk(15) == 15.0
    assert yolculuk(20, hiz=2) == 10.0


def test_istatistik_fonksiyonlari_docstring():
    """Tüm istatistik fonksiyonlarının docstring içerdiğini doğrular."""
    for fn in (
        gezegenleri_buyut_map,
        gezegenleri_buyut_kavrama,
        en_az_iki_baglanti_filter,
        en_az_iki_baglanti_kavrama,
        toplam_baglanti_reduce,
        toplam_baglanti_sum,
        yolculuk,
    ):
        assert fn.__doc__ is not None
        assert len(fn.__doc__.strip()) > 0
