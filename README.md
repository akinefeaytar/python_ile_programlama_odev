# Python Programlama – Lab Ödevleri

**Kurum:** İstanbul Nişantaşı Üniversitesi  
**Ders:** İleri Python Programlama (2026–2027 Güz)  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**Öğrenci Adı Soyadı:** Akın Efe Aytar  
**Öğrenci Numarası:** 20253006037  
**GitHub Deposu:** https://github.com/akinefeaytar/python_ile_programlama_odev.git  

---

## İçindekiler

- [Hafta 6 Lab – Hesapla, Karar Ver, Tekrarla](#hafta-6-lab--hesapla-karar-ver-tekrarla)
- [Hafta 5 Lab – Dekoratörler](#hafta-5-lab--dekoratörler)

---

# Hafta 6 Lab – Hesapla, Karar Ver, Tekrarla

Bu lab Hafta 3, 4 ve 5'te öğrenilenleri birleştiriyor: her görevde **hesaplama** (math, karakter dizileri, f-string), **karar** (if/elif/else, and/or/not) ve **tekrar** (while, for, break, continue) birlikte kullanıldı. Her görev **Girdi → Doğrula → İşle → Çıktı** adımlarına ayrıldı.

> Ödev kuralı gereği **liste, sözlük ve `def` kullanılmadı.** Tüm dosyalar `hafta6/` klasöründe; ayrıntılar için [hafta6/README.md](hafta6/README.md).

| Dosya | Görev | Puan | Öne çıkanlar |
|---|---|---|---|
| `hafta6/hafta6_gorev1.py` | Üçgen analizörü | 20 | Takas ile en uzun kenarı bulma, Heron formülü, `math.acos`/`math.degrees`, dik açı için `math.isclose` |
| `hafta6/hafta6_gorev2.py` | Metin analizörü | 20 | Tek `for` döngüsü, bayrakla kelime sayımı, Türkçe `I/ı – İ/i` düzeltmesi, palindrom |
| `hafta6/hafta6_gorev3.py` | T.C. kimlik no doğrulama | 20 | Biçim kontrolü (11 hane, rakam, ilk hane ≠ 0), T ve Ç toplamları, iki kontrol hanesi |
| `hafta6/hafta6_gorev4.py` | Collatz kaşifi | 20 | Tek satırlık koşullu ifade, adım sayacı, iç içe döngüyle en uzun zincir |
| `hafta6/hafta6_gorev5.py` | Adam asmaca | 20 | `tahminler += harf`, `continue` ile geçersiz/tekrar giriş, `break` ve `while … else` |
| `hafta6/hafta6_bonus.py` | Luhn kontrol hanesi | +10 | 0–9 denenir, ilk geçerli hanede `break` → **7** |

### Çalıştırma

```bash
cd hafta6
python3 hafta6_gorev1.py   # diğer görevler için dosya adını değiştirin
```

### Doğrulanan sonuçlar (örnek girdilerle)

| Görev | Girdi | Çıktı |
|---|---|---|
| 1 | `5 5 8` | `Tür: İkizkenar, Geniş açılı` – `Çevre: 18.00 Alan: 12.00 En büyük açı: 106.26°` |
| 2 | `Ey Edip Adana'da pide ye` | `Harf: 19 Sesli: 10 Sessiz: 9 Rakam: 0 Kelime: 5` – `Palindrom` |
| 3 | `10000000146` / `12345678901` | `GEÇERLİ` / `GEÇERSİZ` |
| 4 | `27`, üst sınır `1000` | `111 adım, en yüksek değer 9232` – `en uzun zincir: 871 (178 adım)` |
| 5 | `KOŞUL` | `K O Ş U L (hata: 2/6) Kazandınız!` |
| Bonus | `453914880343646` | `Kontrol hanesi: 7` |

Örnek girdilerin yanında farklı girdiler de denendi (dik/eşkenar üçgen, geçersiz kenarlar, rakamlı ve Türkçe karakterli cümle, hatalı biçimli kimlik numaraları, `n = 1`, 6 hatayla kaybetme).

### Git commit geçmişi (Hafta 6)

- `Hafta 6 Görev 1: Üçgen analizörü (Heron, kosinüs teoremi, isclose ile dik açı kontrolü)`
- `Hafta 6 Görev 2: Metin analizörü (tek for döngüsü, bayrakla kelime sayımı, palindrom)`
- `Hafta 6 Görev 3: T.C. kimlik numarası doğrulama (biçim kontrolü ve kontrol haneleri)`
- `Hafta 6 Görev 4: Collatz kaşifi (adım sayısı, en yüksek değer, iç içe döngüyle en uzun zincir)`
- `Hafta 6 Görev 5: Adam asmaca (continue, break ve while-else)`
- `Hafta 6 Bonus (+10): Luhn algoritmasıyla kontrol hanesi bulma`

---

# Hafta 5 Lab – Dekoratörler

## 1. Proje Özeti ve Yapılan Çalışmalar

Bu lab çalışmasında uzay oyunu projesi, Python'ın en güçlü metaprogramlama araçlarından biri olan **Dekoratörler (Decorators)** ve **Dekoratör Tabanlı Komut Kayıt Deseni (Registry Pattern)** ile genişletilmiştir:

- **Modüller:**
  - `uzay_oyunu/dekoratorler.py`: Dekoratör fonksiyonlarının ve yardımcı araçların yer aldığı ana modül.
  - `uzay_oyunu/komutlar.py`: Komut kayıt defteri ve durum tabanlı oyun komutları.
  - `uzay_oyunu/oyun.py`: Dekoratörlerle loglanan fonksiyonlar ve komut sistemiyle zenginleştirilmiş `travel()` döngüsü.
  - `dekorator_sirasi.md`: Dekoratör istifleme (sıralama) ve önbellekleme etkisinin derinlemesine analizi.
  - `tests/test_dekoratorler.py`: Tüm dekoratör ve komut sistemini doğrulayan 26 yeni birim test (Toplamda **74 test**).

Tüm dekoratörlerde `functools.wraps` kullanılarak orijinal fonksiyonların `__name__`, `__doc__` ve imza bilgileri korunmuş, `*args` ve `**kwargs` ile esnek çağrılar desteklenmiştir.

---

## 2. Görev Detayları ve Uygulamalar

### Görev 1 – Süre Ölçen Dekoratör (`sure_olc`) (15 Puan)
- `time.perf_counter()` ile fonksiyonun çalışma süresini hassas biçimde ölçer.
- Çıktıyı `fonksiyon_adi: 0.0123 sn` biçiminde konsola yazdırır.
- Fonksiyonun dönüş değerini değiştirmeden aynen iletir.
- Hafta 4'teki önbelleksiz rota sayacına uygulanıp $adim=20$ için süre ölçümü başarıyla gösterilmiştir.

### Görev 2 – Çağrı Sayacı (`say`) ve Dekoratör Sırası (20 Puan)
- Fonksiyon çağrılarını wrapper nesnesinin `cagri` niteliğinde sayar.
- Özyinelemeli Fibonacci fonksiyonu $fib(20)$ için üç farklı sıralama denenmiştir:
  1. **Yalnızca `@say`:** `21891` çağrı (önbellek yok, ikili karar ağacı).
  2. **`@say` üstte, `@lru_cache` altta:** `39` çağrı (her özyinelemeli çağrı önce dıştaki `@say` wrapper'ına gelir, ardından `lru_cache` önbelleğinden döner).
  3. **`@lru_cache` üstte, `@say` altta:** `21` çağrı (çağrılar doğrudan `lru_cache` sarmalayıcısına gelir; önbellek ıskalamalarında içteki `@say` tetiklenir).
  - İçteki sayaca `fib.__wrapped__.cagri` üzerinden erişilir.
- Neden farklı olduklarına dair tüm şemalar ve matematiksel açıklamalar [`dekorator_sirasi.md`](file:///Users/akinefeaytar/Projects/Python%20Oyun%20Yapma%20%C3%96devi/dekorator_sirasi.md) dosyasında belgelenmiştir.

### Görev 3 – Loglayan Dekoratör (`log_cagri`) (15 Puan)
- Fonksiyon çağrılmadan önce adı ve argümanlarını (`-> fonksiyon(arg1, k=v)`), fonksiyon tamamlandığında ise dönüş değerini (`<- fonksiyon = 'sonuc'`) loglar.
- `uzay_oyunu/oyun.py` içindeki `galaksi_kur` ve `hedef_menusu` fonksiyonlarına uygulanmıştır.
- Mevcut tüm testlerin (`tests/test_fonksiyonlar.py`, `tests/test_akis.py`) bozulmadan çalışmaya devam ettiği doğrulanmıştır.

### Görev 4 – Komut Sistemi: Kayıt Deseni (`komutlar.py`) (30 Puan)
- `komut(ad, aciklama="")` dekoratörü:
  - Fonksiyonu değiştirmeden `(fonksiyon, aciklama)` şeklinde `KOMUTLAR` sözlüğüne kaydeder.
  - Aynı ad iki kez kullanılmak istendiğinde tanım anında `ValueError` fırlatır.
- Oyun durumunu (`konum`, `baglantilar`, `credits`, `engines`, `copilot`) alan 3 komut tanımlanmıştır:
  - `yardim(durum)`: Kayıtlı tüm komutları alfabetik sırada ve açıklamalarıyla listeler.
  - `envanter(durum)`: Eldeki eşyaları durum sözlüğünden okuyarak metin olarak gösterir.
  - `harita(durum)`: Oyuncunun bulunduğu gezegenden doğrudan gidebileceği gezegenleri listeler.
- `travel()` fonksiyonu: Oyuncu bir komut adı girdiğinde komut çalıştırılır, çıktısı yazdırılır ve aynı menü tekrar gösterilir; sayı girildiğinde ise eskisi gibi gezegen yolculuğu yapılır.

### Görev 5 – Argüman Alan Dekoratör (`sinirla`) (20 Puan)
- `@sinirla(alt, ust)` dekoratörü, dekore edilen fonksiyonun ilk sayısal argümanının `[alt, ust]` aralığında olup olmadığını kontrol eder.
- Aralık dışındaysa: `ValueError: yakit_harca: 150 değeri 0-100 aralığında değil` fırlatır.
- `yakit_harca(miktar)` fonksiyonuna `@sinirla(0, 100)` uygulanmış; 0 ve 100 sınır değerleri ile aralık dışı negatif ve aşırı değerler test edilmiştir.

### Bonus (+10 Puan) – `hafiza(maxsize=None)` Dekoratörü
- `functools.lru_cache` kullanılmadan, **closure içindeki bir Python sözlüğü (`dict`)** ile geliştirilmiştir.
- `maxsize` parametresi verildiğinde, önbellek boyutu dolunca en eski (ilk eklenen / en az yakın zamanda kullanılan) girdiyi sözlükten siler (LRU/FIFO mantığı).
- `@hafiza` dekoratörünün sonuçları standart `@functools.lru_cache` ile karşılaştırılmış ve özdeş sonuçlar verdiği testlerle kanıtlanmıştır.

---

## 3. Testleri Çalıştırma ve Doğrulama

Tüm testler `uv` veya sanal ortamdaki `pytest` ile çalıştırılabilir:

```bash
# uv ile testleri çalıştırma (Ödev yönergesi gereksinimi):
uv run pytest

# veya sanal ortam python'ı ile:
.venv/bin/python -m pytest
```

### Test Özeti:
```text
============================== 74 passed in 0.13s ==============================
- tests/test_dekoratorler.py : 26 passed (Tüm Hafta 5 dekoratör ve komut testleri)
- tests/test_akis.py         : 22 passed (Hafta 4 üreteç ve akış testleri)
- tests/test_fonksiyonlar.py : 12 passed (Hafta 3 fonksiyon testleri)
- tests/test_istatistik.py   :  9 passed (Hafta 4 fonksiyonel programlama testleri)
- tests/test_tuzaklar.py     :  5 passed (Hafta 3 varsayılan argüman testleri)
TOPLAM: 74 test eksiksiz ve hatasız geçmektedir.
```

---

## 4. Git Commit Geçmişi

Ödev yönergesindeki *"Her görev en az bir commit"* kuralına titizlikle uyulmuştur:
- `Görev 1: Süre ölçen sure_olc dekoratörü ve testleri eklendi`
- `Görev 2: Çağrı sayacı say dekoratörü, Fibonacci testleri ve dekorator_sirasi.md eklendi`
- `Görev 3: Loglayan log_cagri dekoratörü eklendi ve galaksi_kur ile hedef_menusu fonksiyonlarına uygulandı`
- `Görev 4: Komut sistemi kayıt deseni, yardim/envanter/harita komutları ve travel entegrasyonu eklendi`
- `Görev 5: Argüman alan sinirla dekoratörü, yakit_harca ve sınır değeri testleri eklendi`
- `Bonus (+10): Closure sözlüğü ile hafiza(maxsize=None) önbellek dekoratörü ve lru_cache karşılaştırma testleri eklendi`
