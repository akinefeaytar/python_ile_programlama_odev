# İleri Python Programlama – Hafta 5 Lab Ödevi: Dekoratörler

**Kurum:** İstanbul Nişantaşı Üniversitesi  
**Ders:** İleri Python Programlama (2026–2027 Güz)  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**Öğrenci Adı Soyadı:** Akın Efe Aytar  
**Öğrenci Numarası:** 20253006037  
**GitHub Deposu:** https://github.com/akinefeaytar/python_ile_programlama_odev.git  

---

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
