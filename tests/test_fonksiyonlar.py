# Akın Efe Aytar - 20253006037
# Görev 1 testleri - önce testleri yazdım, sonra fonksiyonları ekledim

import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


# envanter_metni testleri

def test_kredi_ve_pilot():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"

def test_hicbirsey_yok():
    assert envanter_metni(False, False, False) == ""

def test_yalnizca_kredi():
    assert envanter_metni(True, False, False) == "Sende: bol kredi"

def test_yalnizca_motor():
    assert envanter_metni(False, True, False) == "Sende: güçlü motorlar"

def test_yalnizca_pilot():
    assert envanter_metni(False, False, True) == "Sende: yetenekli bir pilot"

def test_hepsi_mevcut():
    assert envanter_metni(True, True, True) == "Sende: bol kredi, güçlü motorlar, yetenekli bir pilot"

def test_donus_tipi_str():
    assert isinstance(envanter_metni(True, True, True), str)


# hedef_menusu testleri

def test_iki_hedef():
    sonuc = hedef_menusu(["centauri", "sirius"])
    assert sonuc == "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"

def test_tek_hedef():
    assert hedef_menusu(["mars"]) == "Nereye gitmek istersin?\n[1] mars"

def test_bos_hedef_listesi():
    assert hedef_menusu([]) == "Nereye gitmek istersin?"

def test_numaralar_dogru_siralanmis():
    sonuc = hedef_menusu(["a", "b", "c"])
    assert "[1] a" in sonuc
    assert "[2] b" in sonuc
    assert "[3] c" in sonuc

def test_ilk_satir_baslik():
    sonuc = hedef_menusu(["x", "y"])
    assert sonuc.startswith("Nereye gitmek istersin?")
