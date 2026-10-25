from __future__ import annotations

# Akın Efe Aytar - 20253006037
# İleri Python Programlama - Hafta 5 Lab Ödevi: Dekoratörler

from collections.abc import Callable
import functools
import time
from typing import Any, Optional, Union



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


# ============================================================================
# Görev 2 – Çağrı sayacı ve dekoratör sırası (20 puan)
# ============================================================================

def say(func: Callable) -> Callable:
    """Çağrıları fonksiyonun bir niteliğinde sayan dekoratör.

    Her fonksiyon çağrısında wrapper nesnesinin 'cagri' niteliğini 1 artırır.
    functools.wraps kullanarak orijinal fonksiyonun niteliklerini korur.
    Sayaca fonksiyon üzerinden (func.cagri) veya sarılmış durumdaysa
    func.__wrapped__.cagri üzerinden erişilebilir.

    Args:
        func: Çağrıları sayılacak fonksiyon.

    Returns:
        Callable: Çağrı sayacı eklenmiş sarıcı fonksiyon.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.cagri += 1
        return func(*args, **kwargs)

    wrapper.cagri = 0
    return wrapper


# ============================================================================
# Görev 3 – Loglayan dekoratör (15 puan)
# ============================================================================

def log_cagri(func: Callable) -> Callable:
    """Her çağrıdan önce fonksiyon adını ve argümanlarını, sonra dönüş değerini yazdıran dekoratör.

    Örnek çıktı formatı:
    -> yolculuk('orion', hiz=3)
    <- yolculuk = 'orion hiz=3'

    functools.wraps kullanarak orijinal fonksiyonun __name__, __doc__ ve imza
    niteliklerini korur. Fonksiyonun sonucunu değiştirmeden döndürür.

    Args:
        func: Çağrıları loglanacak fonksiyon.

    Returns:
        Callable: Loglama yapan sarıcı fonksiyon.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        parcalar = [repr(a) for a in args]
        parcalar.extend(f"{k}={repr(v)}" for k, v in kwargs.items())
        arg_str = ", ".join(parcalar)
        print(f"-> {func.__name__}({arg_str})")
        sonuc = func(*args, **kwargs)
        print(f"<- {func.__name__} = {repr(sonuc)}")
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


# ============================================================================
# Görev 5 – Argüman alan dekoratör (20 puan)
# ============================================================================

def sinirla(alt: float, ust: float) -> Callable:
    """Dekore edilen fonksiyonun ilk argümanını [alt, ust] aralığıyla sınırlandıran dekoratör.

    İlk argüman [alt, ust] kapalı aralığında değilse anlamlı bir ValueError fırlatır:
    '{func.__name__}: {ilk_arg} değeri {alt}-{ust} aralığında değil'

    functools.wraps kullanarak orijinal fonksiyonun niteliklerini korur.

    Args:
        alt: İzin verilen en küçük sayısal değer (dahil).
        ust: İzin verilen en büyük sayısal değer (dahil).

    Returns:
        Callable: Sınır kontrolü uygulayan dekoratör.
    """
    def dekorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not args:
                raise ValueError(f"{func.__name__}: İlk argüman bulunamadı!")
            ilk_arg = args[0]
            if ilk_arg < alt or ilk_arg > ust:
                raise ValueError(
                    f"{func.__name__}: {ilk_arg} değeri {alt}-{ust} aralığında değil"
                )
            return func(*args, **kwargs)

        return wrapper

    return dekorator


@sinirla(0, 100)
def yakit_harca(miktar: int) -> int:
    """100 birimlik depodan verilen miktar kadar yakıt harcar ve kalanı döndürür.

    @sinirla(0, 100) dekoratörü ile miktar parametresi 0-100 aralığında sınırlandırılmıştır.

    Args:
        miktar: Harcanacak yakıt miktarı (0 <= miktar <= 100).

    Returns:
        int: Kalan yakıt miktarı.
    """
    depo = 100
    return depo - miktar


# ============================================================================
# Bonus (+10 Puan) – hafiza(maxsize=None) dekoratörü
# ============================================================================

def hafiza(maxsize: int | None = None) -> Callable:
    """functools.lru_cache kullanmadan, closure içindeki bir sözlükle çalışan önbellek dekoratörü.

    Fonksiyon çağrılarının sonuçlarını closure içindeki bir Python sözlüğünde (dict)
    saklar. Aynı argümanlarla tekrar çağrıldığında fonksiyonu tekrar çalıştırmadan
    önbellekteki sonucu döndürür.

    maxsize argümanı verildiğinde, önbellek boyutu maxsize sınırını aşarsa
    en eski girdi (en az yakın zamanda kullanılan / ilk eklenen) sözlükten silinir.
    maxsize=None ise önbellek sınırsız büyüyebilir.

    Args:
        maxsize: Tutulacak azami önbellek elemanı sayısı (None ise sınırsız).

    Returns:
        Callable: Önbellekleme yapan fonksiyon dekoratörü.
    """
    def dekorator(func: Callable) -> Callable:
        # Closure içinde saklanan önbellek sözlüğü
        onbellek: dict[Any, Any] = {}

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Hashable anahtar oluştur: konumsal argümanlar ve sıralı adlı argümanlar
            anahtar = (args, tuple(sorted(kwargs.items())))

            if anahtar in onbellek:
                # LRU mantığı: erişilen elemanı en sona (en güncele) taşı
                deger = onbellek.pop(anahtar)
                onbellek[anahtar] = deger
                return deger

            sonuc = func(*args, **kwargs)
            onbellek[anahtar] = sonuc

            # Eğer maxsize sınırı aşılmışsa en eski (ilk eklenen) anahtarı tahliye et
            if maxsize is not None and len(onbellek) > maxsize:
                en_eski_anahtar = next(iter(onbellek))
                del onbellek[en_eski_anahtar]

            return sonuc

        # Test ve inceleme için önbellek sözlüğüne referans ekle
        wrapper.cache = onbellek
        return wrapper

    return dekorator



