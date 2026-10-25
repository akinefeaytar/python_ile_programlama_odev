# Akın Efe Aytar - 20253006037
# Hafta 5 Lab Testleri - tests/test_dekoratorler.py

import pytest
from functools import lru_cache
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, onbelleksiz_rota_sayaci
from uzay_oyunu.komutlar import komut, KOMUTLAR, yardim, envanter, harita
from uzay_oyunu.oyun import galaksi_kur, hedef_menusu, travel


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


# ============================================================================
# Görev 3 Testleri: Loglayan Dekoratör (15 puan)
# ============================================================================

def test_log_cagri_ornek_formati(capsys):
    """PDF'te belirtilen log formatını birebir doğrular:
    -> yolculuk('orion', hiz=3)
    <- yolculuk = 'orion hiz=3'
    """
    @log_cagri
    def yolculuk(hedef: str, hiz: int = 1) -> str:
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"

    yakalanan = capsys.readouterr()
    assert "-> yolculuk('orion', hiz=3)" in yakalanan.out
    assert "<- yolculuk = 'orion hiz=3'" in yakalanan.out


def test_log_cagri_wraps_korunumu():
    """log_cagri dekoratörünün wraps ile __name__ ve __doc__ niteliklerini koruduğunu doğrular."""
    @log_cagri
    def test_fn():
        """Fonksiyon açıklaması."""
        return 42

    assert test_fn.__name__ == "test_fn"
    assert test_fn.__doc__ == "Fonksiyon açıklaması."


def test_log_cagri_oyun_fonksiyonlari_entegrasyonu(capsys):
    """oyun.py içindeki galaksi_kur ve hedef_menusu fonksiyonlarının loglandığını doğrular."""
    # hedef_menusu çağrısı
    menu = hedef_menusu(["dünya", "mars"])
    yakalanan = capsys.readouterr()
    assert "-> hedef_menusu(['dünya', 'mars'])" in yakalanan.out
    assert "<- hedef_menusu = " in yakalanan.out
    assert "[1] dünya" in menu

    # galaksi_kur çağrısı
    galaksi = galaksi_kur(["a", "b"], {"a": ["b"], "b": []}, "a", yakit=80)
    yakalanan2 = capsys.readouterr()
    assert "-> galaksi_kur(" in yakalanan2.out
    assert "<- galaksi_kur = " in yakalanan2.out
    assert galaksi["konum"] == "a"
    assert galaksi["yakit"] == 80


# ============================================================================
# Görev 4 Testleri: Komut Sistemi ve Kayıt Deseni (30 puan)
# ============================================================================

def test_komut_dekoratoru_kayit_ve_degistirmeme():
    """komut dekoratörünün fonksiyonu değiştirmeden kaydettiğini doğrular."""
    @komut("test_komutu", "test açıklaması")
    def ornek_komut(durum):
        return "calisti"

    assert "test_komutu" in KOMUTLAR
    kayitli_fn, aciklama = KOMUTLAR["test_komutu"]
    assert kayitli_fn is ornek_komut
    assert aciklama == "test açıklaması"
    assert ornek_komut({}) == "calisti"
    del KOMUTLAR["test_komutu"]



def test_komut_ayni_ad_iki_kez_valueerror():
    """Aynı komut adı ikinci kez tanımlanırsa ValueError fırlatıldığını doğrular."""
    with pytest.raises(ValueError, match="zaten tanımlı"):
        @komut("yardim", "tekrar eden komut")
        def sahte_yardim(durum):
            pass


def test_komut_yardim():
    """yardim komutunun tüm komutları alfabetik sırada ve açıklamalarıyla listelediğini doğrular."""
    durum = {}
    cikti = yardim(durum)
    satirlar = cikti.strip().split("\n")
    # yardim, envanter, harita listede olmalı
    assert any("yardim" in s and "komutları listeler" in s for s in satirlar)
    assert any("envanter" in s and "eşyalarını gösterir" in s for s in satirlar)
    assert any("harita" in s and "gidebileceğin gezegenleri gösterir" in s for s in satirlar)

    # Alfabetik sıra kontrolü
    komut_adlari = [s.split()[0] for s in satirlar]
    assert komut_adlari == sorted(komut_adlari)


def test_komut_envanter():
    """envanter komutunun durum sözlüğündeki eşyaları doğru yansıttığını doğrular."""
    durum_dolu = {"credits": True, "engines": False, "copilot": True}
    cikti_dolu = envanter(durum_dolu)
    assert "bol kredi" in cikti_dolu
    assert "yetenekli bir pilot" in cikti_dolu
    assert "güçlü motorlar" not in cikti_dolu

    durum_bos = {"credits": False, "engines": False, "copilot": False}
    cikti_bos = envanter(durum_bos)
    assert "Envanterin boş" in cikti_bos


def test_komut_harita():
    """harita komutunun o anki konumdan gidilebilecek gezegenleri doğru listelediğini doğrular."""
    durum = {
        "konum": "dünya",
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya"]
        }
    }
    cikti = harita(durum)
    assert cikti == "centauri, sirius"

    durum_izole = {
        "konum": "kara_delik",
        "baglantilar": {"kara_delik": []}
    }
    assert "Gidebileceğin hiçbir gezegen yok" in harita(durum_izole)


def test_travel_komut_isleme_ve_menu_tekrar(monkeypatch, capsys):
    """travel() fonksiyonunda oyuncu komut girdiğinde komutun çalıştırılıp
    sonucunun yazdırıldığını, aynı menünün tekrar gösterildiğini ve ardından
    seçim yapıldığında yolculuğun gerçekleştiğini doğrular.
    """
    import uzay_oyunu.oyun as oyun_modul

    # Oyun durumunu kontrollü hale getirelim
    oyun_modul.galaksi["konum"] = "dünya"
    oyun_modul.galaksi["baglantilar"]["dünya"] = ["centauri", "sirius"]
    # Göstergeyi tazeleyelim
    from uzay_oyunu.akis import yakit_gostergesi
    oyun_modul._gosterge = yakit_gostergesi(100, 5)

    # Sırasıyla girdiler: önce 'yardim', sonra 'harita', sonra geçerli seçim '1' (centauri)
    girdiler = iter(["yardim", "harita", "1"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(girdiler))

    oyun_modul.travel()

    yakalanan = capsys.readouterr()
    # yardim komutunun çıktısı yazdırılmış olmalı
    assert "komutları listeler" in yakalanan.out
    # harita komutunun çıktısı yazdırılmış olmalı
    assert "centauri, sirius" in yakalanan.out
    # Yeni konuma gidilmiş olmalı
    assert oyun_modul.galaksi["konum"] == "centauri"



