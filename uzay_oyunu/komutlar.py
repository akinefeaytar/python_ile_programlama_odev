# Akın Efe Aytar - 20253006037
# İleri Python Programlama - Hafta 5 Lab Ödevi: Komut Sistemi

from collections.abc import Callable
from typing import Any

# Komut kayıt defteri: komut_adi -> (fonksiyon, aciklama)
KOMUTLAR: dict[str, tuple[Callable, str]] = {}


# ============================================================================
# Görev 4 – Komut sistemi: kayıt deseni (30 puan)
# ============================================================================

def komut(ad: str, aciklama: str = "") -> Callable:
    """Argüman alan komut kayıt dekoratörü.

    Dekore edilen fonksiyonu değiştirmeden (fonksiyon, aciklama) ikilisi
    olarak KOMUTLAR sözlüğüne kaydeder. Aynı komut adı ikinci kez tanımlanmak
    istenirse tanım anında ValueError fırlatır.

    Args:
        ad: Komutun çağrılacağı isim/komut anahtarı.
        aciklama: Komutun işlevini belirten kısa açıklama.

    Returns:
        Callable: Orijinal fonksiyonu değiştirmeden döndüren dekoratör.

    Raises:
        ValueError: Komut adı zaten kayıtlıysa fırlatılır.
    """
    def dekorator(func: Callable) -> Callable:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' adlı komut zaten tanımlı!")
        KOMUTLAR[ad] = (func, aciklama)
        return func

    return dekorator


@komut("yardim", "komutları listeler")
def yardim(durum: dict[str, Any]) -> str:
    """Kayıtlı tüm komutları ve açıklamalarını alfabetik sırada listeler.

    Args:
        durum: Oyunun mevcut durumunu taşıyan sözlük.

    Returns:
        str: Komutların ve açıklamalarının formatlanmış listesi.
    """
    satirlar = []
    for ad, (_, aciklama) in sorted(KOMUTLAR.items()):
        satirlar.append(f"{ad:<10}{aciklama}")
    return "\n".join(satirlar)


@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict[str, Any]) -> str:
    """Oyuncunun elindeki mevcut eşyaları durum sözlüğünden okuyarak listeler.

    Args:
        durum: Oyunun mevcut durumunu taşıyan sözlük (credits, engines, copilot).

    Returns:
        str: Sahip olunan eşyaların metin temsili.
    """
    esyalar = []
    if durum.get("credits"):
        esyalar.append("bol kredi")
    if durum.get("engines"):
        esyalar.append("güçlü motorlar")
    if durum.get("copilot"):
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return "Envanterin boş."
    return "Sende: " + ", ".join(esyalar)


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict[str, Any]) -> str:
    """Oyuncunun mevcut konumundan doğrudan gidebileceği gezegenleri listeler.

    Args:
        durum: Oyunun mevcut durumunu taşıyan sözlük (konum, baglantilar).

    Returns:
        str: Gidilebilecek komşu gezegenlerin virgülle ayrılmış isimleri.
    """
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {})
    hedefler = baglantilar.get(konum, [])
    if not hedefler:
        return "Gidebileceğin hiçbir gezegen yok!"
    return ", ".join(hedefler)
