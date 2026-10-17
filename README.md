# İleri Python Programlama – Hafta 4 Lab Ödevi: Üreteçler ve functools

**Kurum:** İstanbul Nişantaşı Üniversitesi  
**Ders:** İleri Python Programlama (2026–2027 Güz)  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**Öğrenci Adı Soyadı:** Akın Efe Aytar  
**Öğrenci Numarası:** 20253006037  
**GitHub Deposu:** https://github.com/akinefeaytar/python_ile_programlama_odev.git  

---

## 1. Proje Özeti ve Yapılan Çalışmalar

Bu lab çalışmasında uzay oyunu projesi; sonsuz üreteçler (infinite generators), bellek dostu veri işleme boru hatları (data pipelines), `@functools.lru_cache` tabanlı rota dinamik programlaması, fonksiyonel programlama araçları (`map`, `filter`, `reduce`, `partial`) ve meşgul bekleme (busy waiting) analizi ile genişletilmiştir.

Projedeki her fonksiyonda **tip ipuçları (type hints)** ve **ayrıntılı docstring** dokümantasyonları eksiksiz uygulanmış; tüm gereksinimler için birim testler (`tests/test_akis.py`, `tests/test_istatistik.py`, `tests/test_fonksiyonlar.py`, `tests/test_tuzaklar.py`) yazılmıştır.

---

## 2. Görev 4: Önbellekli Rota Sayacı Performans Ölçümleri

`rota_sayaci(baglantilar)` fonksiyonu, içinde `@lru_cache(maxsize=None)` ile dekore edilmiş `rota_sayisi(gezegen, adim)` fonksiyonunu barındırır. Bu fonksiyon, verilen gezegenden başlayarak tam `adim` uzunluğundaki farklı rota sayısını hesaplar.

`time.perf_counter()` kullanılarak $adim = 20$ için önbelleksiz (saf özyineleme) ve önbellekli sürümler karşılaştırılmıştır:

### Performans Karşılaştırma Tablosu

| Metrik | Önbelleksiz Sürüm (No Cache) | Önbellekli Sürüm (@lru_cache) | Hızlanma / Fark |
| :--- | :--- | :--- | :--- |
| **Hesaplanan Rota Sayısı** | `4.315.343` | `4.315.343` | Birebir Eşit |
| **Çalışma Süresi (adim=20)** | `0.921855` saniye | `0.000028` saniye | **~33.000 Kat Daha Hızlı** |
| **Zaman Karmaşıklığı** | $O(b^N)$ (Üstel - Exponential) | $O(V \times N)$ (Doğrusal - Linear) | Üstel karmaşıklıktan kurtulundu |
| **`cache_info()` Çıktısı** | Yok | `CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)` | Toplam 51 alt problem çözüldü |

### `cache_info()` Detaylı Analizi
- **`currsize=51` / `misses=51`:** Galaksideki gezegenler ve adım kombinasyonlarından yalnızca 51 benzersiz `(gezegen, adim)` durumu hesaplanmıştır.
- **`hits=47`:** Tekrar eden 47 çağrı doğrudan bellek önbelleğinden (O(1) sürede) getirilmiştir.
- Bu önbellekleme sayesinde, önbelleksiz sürümde $adim=40$ gibi büyük değerlerde özyineleme derinliği ve çağrı sayısı trilyonları bularak sistemin kilitlenmesine neden olacakken, önbellekli sürümde `say("dünya", 40)` yalnızca milisaniyeler içinde `16832258606399` sonucunu üretmektedir.

---

## 3. Görev 5: map / filter / reduce ile Liste Üreteçleri Karşılaştırması

`istatistik.py` modülünde üç temel soru hem fonksiyonel araçlarla (`map`, `filter`, `reduce`) hem de Pythonik yapılarla (`list comprehension`, `sum`) çözülmüştür:

1. **Gezegen adlarının büyük harfli listesi:**
   - Fonksiyonel: `list(map(str.upper, galaksi["gezegenler"]))`
   - Liste Üreteci: `[g.upper() for g in galaksi["gezegenler"]]`
   - Çıktı: `['DÜNYA', 'CENTAURI', 'SIRIUS', 'ORION', 'KARA_DELIK']`

2. **En az iki bağlantısı olan gezegenler:**
   - Fonksiyonel: `list(filter(lambda g: len(baglantilar[g]) >= 2, gezegenler))`
   - Liste Üreteci: `[g for g in gezegenler if len(baglantilar[g]) >= 2]`
   - Çıktı: `['dünya', 'centauri', 'sirius', 'orion']`

3. **Toplam bağlantı sayısı:**
   - Fonksiyonel: `reduce(lambda toplam, g: toplam + len(baglantilar[g]), gezegenler, 0)`
   - Liste / Üreteç toplamı: `sum(len(baglantilar[g]) for g in gezegenler)`
   - Çıktı: `10`

### Okunabilirlik Değerlendirmesi (Zen of Python / PEP 20):
- **Liste Üreteçleri ve `sum()` tercihimdir.**
- **Lambda Kirliliği Yoktur:** `filter` ve `reduce` kullanırken `lambda` tanımlamak sözdizimini ağırlaştırır. Oysa liste üreteçlerindeki `[g for g in ... if ...]` yapısı İngilizce bir cümle gibi doğal ve akıcı okunur.
- **Tip Dönüşümü Gereksizdir:** Python 3'te `map` ve `filter` tembel iterator döndürdüğünden dıştan `list(...)` ile sarılmalıdır. Liste üreteçleri ise doğrudan hedef listeyi `[ ]` sözdizimiyle üretir.
- **Hata Ayıklama Kolaylığı:** `reduce` akümülatör mantığı takip edilmesi zor bir soyutlama iken, `sum(...)` amacı anında gösterir.

### `functools.partial` Kullanımı
`yolculuk(mesafe, hiz)` fonksiyonundan `hiz=3` parametresi sabitlenerek `hizli_yolculuk` türetilmiştir. Bu sayede fonksiyon tekrar tekrar hız parametresi girilmeden özel bir amaca yönelik kullanılabilir hale getirilmiştir.

---

## 4. Bonus (+10 Puan): Meşgul Bekleme (Busy Waiting) ve time.sleep Farkı

### Meşgul Bekleme (Busy Waiting / Polling / Spinlock) Nedir?
Bonus kapsamında uygulanan `zamanlayici(aralik)` üreteci, bir `while True` döngüsü içinde sürekli olarak `time.perf_counter()` ile geçen süreyi sorgular:
```python
while True:
    simdi = time.perf_counter()
    if simdi - son >= aralik:
        ...
```
Bu yöntem **"meşgul bekleme"** olarak adlandırılır çünkü:
- İşlemci çekirdeği (CPU core) koşul sağlanana kadar boşta beklemez; döngüyü saniyede milyonlarca kez koşturmaya devam eder.
- CPU kullanım oranı anında **%100** seviyesine fırlar.
- İşlemci aşırı ısınır, enerji tüketimi tavan yapar ve işletim sistemindeki diğer süreçlerin CPU zamanından çalınmış olur.

### `time.sleep()` İle Farkı
- `time.sleep()`, işletim sistemi çekirdeğine (kernel) sistem çağrısı (`nanosleep` / `select`) gönderir.
- İşletim sistemi zamanlayıcısı (scheduler), bu çağrıyı yapan iş parçacığını (thread) **BLOCKED / SLEEPING** durumuna alır.
- Uyku süresi boyunca ilgili thread CPU çalıştırma kuyruğundan tamamen çıkarılır; CPU kullanımı **%0** olur. İşlemci diğer süreçlere tahsis edilir veya güç tasarrufu moduna geçer.
- Süre dolduğunda donanım zamanlayıcısının ürettiği kesme (hardware interrupt) ile çekirdek, thread'i uyandırıp **READY** durumuna getirir.

---

## 5. Testleri Çalıştırma

Projeyi test etmek için sanal ortam veya `uv` kullanılabilir:

```bash
# uv ile testleri çalıştırma (Yönerge gereksinimi):
uv run pytest

# veya venv içerisindeki pytest ile:
pytest
```

Tüm 48 test (17 eski + 31 yeni) eksiksiz olarak geçmektedir:
- `tests/test_akis.py` (Görev 1, 2, 3, 4 ve Bonus testleri)
- `tests/test_istatistik.py` (Görev 5 testleri)
- `tests/test_fonksiyonlar.py` (Hafta 3 fonksiyon testleri)
- `tests/test_tuzaklar.py` (Hafta 3 mutable default tuzak testleri)
