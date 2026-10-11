# Kapsam Analizi
**Akın Efe Aytar - 20253006037**

Python'da değişkenlerin hangi kapsamda arandığını LEGB kuralı belirliyor: Local, Enclosing, Global, Built-in.

---

## Örnek 1

```python
renk = "mavi"

def boya():
    renk = "kırmızı"
    print(renk)

boya()
print(renk)
```

**Tahminim:** kırmızı, sonra mavi yazacak diye düşündüm.

**Gerçek sonuç:**
```
kırmızı
mavi
```

**Neden:** `boya()` içinde `renk = "kırmızı"` yeni bir yerel değişken oluşturuyor. Global `renk` bu işlemden etkilenmiyor, fonksiyon bitince yerel kapsam kayboluyor.

---

## Örnek 2

```python
puan = 100

def goster():
    print(puan)

goster()
```

**Tahminim:** 100 yazar

**Gerçek sonuç:**
```
100
```

**Neden:** Fonksiyon içinde `puan`'a atama yapılmıyor. Python LEGB sırasıyla önce yerel bakıyor, bulamayınca global'deki 100'ü buluyor.

---

## Örnek 3 - UnboundLocalError

```python
puan = 100

def guncelle():
    print(puan)
    puan = 200
    print(puan)

guncelle()
```

**Tahminim:** İlk print 100 yazar, sonra 200'e günceller diye düşündüm.

**Gerçek sonuç:**
```
UnboundLocalError: local variable 'puan' referenced before assignment
```

**Neden:** Python, `puan = 200` satırını görünce `puan`'ı fonksiyonun tamamında yerel olarak işaretliyor. Bu yüzden birinci satırdaki `print(puan)` çalışmaya çalıştığında yerel `puan` henüz yoktur ve hata alınır. Bunu anlamak biraz zor oldu çünkü Python kodu yukarıdan aşağı çalıştırırken aynı zamanda hangi değişkenlerin yerel olduğuna da önceden karar veriyor.

Düzeltmek için değeri parametre olarak almak daha doğru:

```python
def guncelle(p):
    print(p)
    p = 200
    print(p)
```
