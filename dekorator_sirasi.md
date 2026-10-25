# Dekoratör Sırası ve Önbellek Etkisi Analizi

**Öğrenci:** Akın Efe Aytar  
**Numara:** 20253006037  
**Ders:** İleri Python Programlama (Hafta 5)  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  

---

## Giriş ve Dekoratör Zincirleme Mekanizması

Python'da fonksiyonların üzerine birden fazla dekoratör eklendiğinde (dekoratör istifleme / *decorator stacking*), dekoratörler **aşağıdan yukarıya** doğru uygulanır (tanım anında) ve **yukarıdan aşağıya** doğru işletilir (çağrı anında).

Matematiksel olarak:
```python
@dekorator1
@dekorator2
def fonksiyon():
    pass
```
sözdizimi, perde arkasında şu fonksiyon bileşkesine (*function composition*) eşdeğerdir:
$$\text{fonksiyon} = \text{dekorator1}(\text{dekorator2}(\text{fonksiyon}))$$

Bu lab ödevinde özyinelemeli Fibonacci algoritması $fib(20)$ için üç farklı dekoratör yerleşimi incelenmiş ve elde edilen çağrı sayıları aşağıda analiz edilmiştir.

---

## Ölçüm Sonuçları Özeti

| Deney Durumu | Dekoratör Dizilimi | $fib(20)$ Çağrı Sayısı | Sayaca Erişim Şekli |
| :--- | :--- | :---: | :--- |
| **Durum 1** | Yalnızca `@say` | **21891** | `fib.cagri` |
| **Durum 2** | `@say` üstte, `@lru_cache` altta | **39** | `fib.cagri` |
| **Durum 3** | `@lru_cache` üstte, `@say` altta | **21** | `fib.__wrapped__.cagri` |

---

## Durumların Detaylı Açıklaması

### 1. Durum: Yalnızca `@say` (21891 Çağrı)

```python
@say
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

#### Neden 21891 çağrı oluştu?
Önbellekleme (memoization) mekanizması bulunmadığında, klasik özyinelemeli Fibonacci fonksiyonu ikili bir karar ağacı (*binary recursion tree*) oluşturur.
- $fib(20)$ hesaplanırken $fib(19)$ ve $fib(18)$ çağrılır.
- $fib(19)$ hesaplanırken tekrar $fib(18)$ ve $fib(17)$ çağrılır.
- Aynı alt problemler (örneğin $fib(2)$, $fib(3)$) ağacın farklı dallarında defalarca ve gereksiz yere baştan hesaplanır.

$n$ elemanı için toplam çağrı sayısı matematiksel olarak:
$$C(0) = 1, \quad C(1) = 1$$
$$C(n) = 1 + C(n-1) + C(n-2) = 2 \cdot F(n+1) - 1$$
$F(21) = 10946$ olduğundan:
$$C(20) = 2 \times 10946 - 1 = 21891$$
olur. `@say` dekoratörü her bir fonksiyon çağrısını doğrudan saydığı için sonuç tam **21891**'dir.

---

### 2. Durum: `@say` Üstte, `@lru_cache` Altta (39 Çağrı)

```python
@say
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

#### Neden 39 çağrı oluştu?
Burada dekoratör uygulama sırası:
$$\text{fib} = \text{say}(\text{lru\_cache}(\text{fib}))$$
şeklindedir. Yani fonksiyonun en dış katmanında `@say` dekoratörünün ürettiği wrapper fonksiyon bulunmaktadır:

1. Global isim alanındaki `fib` ismi, `@say` tarafından döndürülen `wrapper_say` fonksiyonunu gösterir.
2. `fib(n - 1)` veya `fib(n - 2)` özyinelemeli çağrısı yapıldığında, doğrudan en dıştaki `wrapper_say` fonksiyonu çağrılır ve **`wrapper_say.cagri` sayacı her çağrıda 1 artar**.
3. Ardından `wrapper_say`, kendi içindeki `lru_cache` sarmalayıcısını çağırır.
4. `lru_cache`, istenen $n$ değeri daha önce hesaplanmışsa önbellekten anında sonucu döner; hesaplanmamışsa orijinal fonksiyonu çalıştırır.

Dolayısıyla `lru_cache` sayesinde hesaplama $O(N)$ karmaşıklığına düşer; ancak **özyinelemeli çağrılar en dıştaki `fib` adına (yani `@say` sarmalayıcısına) yapıldığı için**, önbellek sorgulaması yapılmadan önce her seferinde `cagri` sayacı tetiklenir.
- 0'dan 20'ye kadar 21 girdi ilk kez hesaplanır.
- Dallanma gereği önbelleğe yapılan 18 tekrar sorgusu da önce dıştaki `@say` üzerinden geçer.
- Toplam çağrı sayısı: $21 + 18 = \mathbf{39}$ olur.

---

### 3. Durum: `@lru_cache` Üstte, `@say` Altta (21 Çağrı)

```python
@lru_cache(maxsize=None)
@say
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

#### Neden 21 çağrı oluştu?
Bu dizilimde fonksiyon bileşkesi:
$$\text{fib} = \text{lru\_cache}(\text{say}(\text{fib}))$$
olarak gerçekleşir. Bu kez en dış katmanda `@lru_cache` sarmalayıcısı yer alır:

1. Global isim alanındaki `fib` ismi doğrudan `lru_cache` wrapper nesnesidir.
2. Özyinelemeli olarak `fib(n - 1)` veya `fib(n - 2)` çağrıldığında, istek doğrudan en dıştaki `lru_cache` sarmalayıcısına gider.
3. **Önbellekte Değer Varsa (*Cache Hit*):** `lru_cache` alt katmandaki `@say` fonksiyonuna hiç uğramadan değeri anında döndürür. Dolayısıyla `@say` sayacı artmaz.
4. **Önbellekte Değer Yoksa (*Cache Miss*):** `lru_cache` içteki `@say` fonksiyonunu tetikler ve sayaç 1 artarak gerçek hesaplama yapılır.
5. $0 \le n \le 20$ aralığında toplamda 21 farklı değer olduğu için, `@say` tam olarak **21** kez çalışır.

#### `fib.__wrapped__.cagri` İpucu Açıklaması:
En dıştaki fonksiyon `lru_cache` wrapper'ı olduğundan doğrudan `fib.cagri` özniteliği bulunmaz. Ancak `functools.wraps` mekanizması, sarmalanan alt fonksiyonu `__wrapped__` niteliği altında saklar. Bu sayede en dıştaki `lru_cache` kabuğunu delerek içteki `@say` fonksiyonunun `cagri` niteliğine şu şekilde ulaşılır:
```python
fib.__wrapped__.cagri  # 21
```

---

## Özet ve Mühendislik Çıkarımı

- **Dekoratörlerin Sırası Davranışı Belirler:** Hangi dekoratörün dışta olduğu, gelen çağrıyı ilk kimin karşılayacağını ve önbelleğin kimi koruyacağını belirler.
- **Süre ve Sayaç Ölçümlerinde Sıra:**
  - Eğer fonksiyonun *dış dünyadan aldığı tüm talepleri* (önbellek isabetleri dahil) saymak istiyorsanız sayacı en dışa koymalısınız (`@say` üstte).
  - Eğer fonksiyonun *gerçekten CPU harcayarak hesapladığı saf iş sayısını* (önbellek ıskalamalarını) saymak istiyorsanız sayacı en içe koymalısınız (`@lru_cache` üstte).
