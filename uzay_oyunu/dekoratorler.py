# Akın Efe Aytar - 20253006037
# İleri Python Programlama - Hafta 5 Lab Ödevi: Dekoratörler

from collections.abc import Callable
import functools
import time
from typing import Any


# ============================================================================
# Görev 1 – Süre ölçen dekoratör (15 puan)
# ============================================================================

def sure_olc(func: Callable) -> Callable:
    """Fonksiyonun çalışma süresini time.perf_counter() ile ölçen dekoratör.

    Süreyi 'ad: 0.0123 sn' biçiminde konsola yazdırır ve fonksiyonun orijinal
    dönüş değerini değiştirmeden döndürür. functools.wraps kullanarak orijinal
    fonksiyonun __name__, __doc__ ve imza niteliklerini korur.

    Args:
        func: Süresi ölçülecek çağrılabilir nesne (fonksiyon).

    Returns:
        Callable: Süre ölçümü yapan sarıcı (wrapper) fonksiyon.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"{func.__name__}: {gecen_sure:.4f} sn")
        return sonuc

    return wrapper


def onbelleksiz_rota_sayaci(
    baglantilar: dict[str, list[str]],
) -> Callable[[str, int], int]:
    """Hafta 4'teki rota sayacının lru_cache kullanılmayan önbelleksiz sürümü.

    Args:
        baglantilar: Gezegen bağlantı grafiği sözlüğü.

    Returns:
        Callable[[str, int], int]: Önbelleksiz rota_sayisi fonksiyonu.
    """
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        return sum(
            rota_sayisi(komsu, adim - 1)
            for komsu in baglantilar.get(gezegen, [])
        )

    return rota_sayisi
