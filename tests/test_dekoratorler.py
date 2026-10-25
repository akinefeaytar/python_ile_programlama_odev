# Akın Efe Aytar - 20253006037
# Hafta 5 Lab Testleri - tests/test_dekoratorler.py

import pytest
from functools import lru_cache
from uzay_oyunu.dekoratorler import sure_olc, say, onbelleksiz_rota_sayaci


# ============================================================================
# Görev 1 Testleri: Süre Ölçen Dekoratör (15 puan)
# ============================================================================

def test_sure_olc_sonuc_degismeden_donuyor():
    """sure_olc dekoratörünün fonksiyon sonucunu değiştirmeden döndürdüğünü doğrular."""
    @sure_olc
    def topla(a: int, b: int) -> int:
        return a + b

    assert topla(3, 7) == 10
    assert topla(-5, 5) == 0


def test_sure_olc_adli_ve_konumsal_argumanlar():
    """sure_olc dekoratörünün hem konumsal hem de adlı argümanları doğru ilettiğini doğrular."""
    @sure_olc
    def gemi_bilgisi(isim: str, model: str = "X-Wing", hiz: int = 100) -> str:
        return f"{isim} ({model}) - Hız: {hiz}"

    sonuc1 = gemi_bilgisi("Avcı", model="Falcon", hiz=500)
    assert sonuc1 == "Avcı (Falcon) - Hız: 500"

    sonuc2 = gemi_bilgisi("Keşif", hiz=250)
    assert sonuc2 == "Keşif (X-Wing) - Hız: 250"


def test_sure_olc_name_ve_doc_korunuyor():
    """functools.wraps ile orijinal __name__ ve __doc__ niteliklerinin korunduğunu doğrular."""
    @sure_olc
    def ornek_fonksiyon():
        """Bu fonksiyonun özel bir dokümantasyonu vardır."""
        return "tamam"

    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Bu fonksiyonun özel bir dokümantasyonu vardır."


def test_sure_olc_cikti_formati(capsys):
    """Konsol çıktısının 'fonksiyon_adi: 0.0000 sn' biçiminde olduğunu doğrular."""
    @sure_olc
    def selamla(kisi: str) -> str:
        return f"Merhaba {kisi}"

    selamla("Dünya")
    yakalanan = capsys.readouterr()
    assert "selamla: " in yakalanan.out
    assert " sn" in yakalanan.out


def test_sure_olc_onbelleksiz_rota_sayaci_adim_20(capsys):
    """Hafta 4'teki önbelleksiz rota sayacına sure_olc uygulanıp adim=20 için süreyi gösterir."""
    # Basit bir 2 düğümlü çift yönlü çizge (dünya <-> centauri)
    # adim=20 durumunda 2^20 gibi devasa üstel patlama olmaması için
    # doğrusal veya kontrollü bir çizge üzerinde adim=20 için rota sayısı ölçülür.
    baglantilar = {
        "dünya": ["centauri"],
        "centauri": ["dünya"]
    }
    ham_sayac = onbelleksiz_rota_sayaci(baglantilar)

    @sure_olc
    def rotalari_hesapla(gezegen: str, adim: int) -> int:
        return ham_sayac(gezegen, adim)

    sonuc = rotalari_hesapla("dünya", 20)
    assert sonuc == 1  # Her adımda tek komşu var, 20 adımda tam 1 rota vardır

    yakalanan = capsys.readouterr()
    assert "rotalari_hesapla: " in yakalanan.out
    assert " sn" in yakalanan.out


# ============================================================================
# Görev 2 Testleri: Çağrı Sayacı ve Dekoratör Sırası (20 puan)
# ============================================================================

def test_say_temel_islevsellik():
    """say dekoratörünün fonksiyon çağrılarını doğru saydığını doğrular."""
    @say
    def karesi(x: int) -> int:
        return x * x

    assert karesi.cagri == 0
    assert karesi(3) == 9
    assert karesi.cagri == 1
    assert karesi(4) == 16
    assert karesi.cagri == 2


def test_fibonacci_yalnizca_say():
    """Yalnızca @say uygulandığında fib(20) için çağrı sayısının tam 21891 olduğunu doğrular."""
    @say
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    sonuc = fib(20)
    assert sonuc == 6765
    assert fib.cagri == 21891


def test_fibonacci_say_ustte_lru_altta():
    """@say üstte, @lru_cache altta iken fib(20) için çağrı sayısının tam 39 olduğunu doğrular."""
    @say
    @lru_cache(maxsize=None)
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    sonuc = fib(20)
    assert sonuc == 6765
    assert fib.cagri == 39


def test_fibonacci_lru_ustte_say_altta():
    """@lru_cache üstte, @say altta iken fib(20) için iç sayaca fib.__wrapped__.cagri ile
    ulaşıldığını ve değerinin tam 21 olduğunu doğrular."""
    @lru_cache(maxsize=None)
    @say
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    sonuc = fib(20)
    assert sonuc == 6765
    assert fib.__wrapped__.cagri == 21

