# Akın Efe Aytar - 20253006037
# Görev 4 - mutable default argument tuzağı

import pytest


# ADIM 1: hatalı fonksiyon, testin başarısız olduğunu gördüm

def yakit_ekle_hatali(miktar, depo=[]):
    depo.append(miktar)
    return depo


def test_hatali_versiyon_tuzagi():
    # iki çağrı aynı liste nesnesini paylaşıyor
    r1 = yakit_ekle_hatali(10)
    r2 = yakit_ekle_hatali(20)
    assert r1 is r2


# ADIM 2: None kalıbıyla düzelttim

def yakit_ekle(miktar, depo=None):
    """None kontrolü ile her seferinde yeni liste oluşturur."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_duzeltilmis_tek_deger():
    assert yakit_ekle(10) == [10]

def test_duzeltilmis_bagimsiz_listeler():
    d1 = yakit_ekle(10)
    d2 = yakit_ekle(20)
    assert d1 == [10]
    assert d2 == [20]

def test_mevcut_depoya_ekleme():
    mevcut = [5]
    assert yakit_ekle(10, mevcut) == [5, 10]

def test_ardisik_cagrilar_bagimsiz():
    assert yakit_ekle(1) == [1]
    assert yakit_ekle(2) == [2]
    assert yakit_ekle(3) == [3]
