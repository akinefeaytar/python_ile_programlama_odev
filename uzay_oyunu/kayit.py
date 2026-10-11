# Akın Efe Aytar - 20253006037
# Görev 2 - esnek parametreler


def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler) -> None:
    """Görevi adımları ve ek bilgilerle birlikte ekrana yazar."""
    print(f"[{oncelik.upper()}] {baslik}")
    for i, adim in enumerate(adimlar, 1):
        print(f"  {i}. {adim}")
    for anahtar, deger in ekler.items():
        print(f"  {anahtar}: {deger}")


if __name__ == "__main__":
    # doğrudan çağrı
    print("--- doğrudan çağrı ---")
    gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al",
                oncelik="yüksek", sorumlu="Ayşe")

    print()

    # liste ve sözlük açarak çağrı
    print("--- * ve ** ile çağrı ---")
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler)
