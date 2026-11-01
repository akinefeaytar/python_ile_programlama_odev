# Python ile Programlama – Hafta 6 Lab: Hesapla, Karar Ver, Tekrarla

**Kurum:** İstanbul Nişantaşı Üniversitesi  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**Öğrenci:** Akın Efe Aytar – 20253006037  
**Dönem:** 2026–2027 Güz

Bu lab Hafta 3, 4 ve 5'i birleştiriyor: her görevde hesaplama (math, karakter dizileri, f-string),
karar (if/elif/else, and/or/not) ve tekrar (while, for, break, continue) birlikte kullanıldı.
Her görev **Girdi → Doğrula → İşle → Çıktı** adımlarına ayrıldı. **Liste, sözlük ve def kullanılmadı.**

## Dosyalar

| Dosya | Görev | Puan |
|---|---|---|
| `hafta6_gorev1.py` | Üçgen analizörü (Heron, kosinüs teoremi, `math.isclose`) | 20 |
| `hafta6_gorev2.py` | Metin analizörü (tek for döngüsü, bayrakla kelime sayımı, palindrom) | 20 |
| `hafta6_gorev3.py` | T.C. kimlik numarası doğrulama (kontrol haneleri) | 20 |
| `hafta6_gorev4.py` | Collatz kaşifi (tek satırlık koşullu ifade, iç içe döngü) | 20 |
| `hafta6_gorev5.py` | Adam asmaca (`continue`, `break`, `while … else`) | 20 |
| `hafta6_bonus.py` | Luhn kontrol hanesi | +10 |

## Çalıştırma

```bash
cd hafta6
python3 hafta6_gorev1.py
```

## Örnek çıktılar

```
a: 5  b: 5  c: 8
Tür: İkizkenar, Geniş açılı
Çevre: 18.00 Alan: 12.00 En büyük açı: 106.26°
```

```
Cümle: Ey Edip Adana'da pide ye
Harf: 19 Sesli: 10 Sessiz: 9 Rakam: 0 Kelime: 5
Ters: ey edip ad'anadA pidE yE
Palindrom
```

```
T.C. kimlik no: 10000000146
Tek: 2 Çift: 0 10. hane: 4 11. hane: 6 → GEÇERLİ
T.C. kimlik no: 12345678901
→ GEÇERSİZ
```

```
n: 27
27 → 1: 111 adım, en yüksek değer 9232
Üst sınır: 1000
1–1000 arasında en uzun zincir: 871 (178 adım)
```

```
K O Ş U L (hata: 2/6) Kazandınız!
```

```
Kontrol hanesi: 7
Geçerli numara: 4539148803436467 (Luhn toplamı: 80)
```

## Dikkat edilen noktalar

- Türkçe harf sorunu: `"i".upper()` → `"I"` ve `"I".lower()` → `"i"` verdiği için `i/İ` ve `ı/I` elle düzeltildi.
- Ondalıklı sayılarda `==` yerine `math.isclose` kullanıldı.
- Geçersiz girişler (harf, negatif sayı, boş giriş, yanlış uzunluk, tekrar edilen harf) yakalanıyor.
- T.C. kimlik doğrulamasında yalnızca test numaraları kullanıldı.
