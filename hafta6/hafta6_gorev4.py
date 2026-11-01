'''
Ad Soyad : Akın Efe Aytar
Numara   : 20253006037
Tarih    : 01.11.2026
Ders     : Python ile Programlama - Hafta 6 Lab
Görev 4  : Collatz kaşifi

Açıklama:
Collatz kuralı: sayı çiftse ikiye bölünüyor, tekse 3n+1 yapılıyor,
1'e ulaşana kadar devam ediliyor.
(a) Girilen n için kaç adımda 1'e ulaştığını ve dizideki en büyük değeri buluyorum.
(b) Girilen üst sınıra kadar iç içe döngüyle en uzun zinciri veren sayıyı buluyorum.
Kuralı ödevde istendiği gibi koşullu ifadeyle tek satırda yazdım.
Liste ve def kullanmadım.
'''

'''
(a) GİRDİ VE DOĞRULAMA
isdigit eksi işaretini ve noktayı kabul etmediği için negatif ve ondalıklı
sayılar da otomatik olarak yakalanıyor. 0 girilmesin diye >= 1 kontrolü de ekledim.
'''
metin = input("n: ").strip()
while not (metin.isdigit() and metin.isascii() and int(metin) >= 1):
    print("Uyarı: Lütfen 1 veya daha büyük bir tam sayı girin.")
    metin = input("n: ").strip()
baslangic = int(metin)

'''
(a) HESAPLAMA
adim sayacı her turda 1 artıyor. en_yuksek'i başlangıç sayısından başlattım
çünkü başlangıç sayısı da dizinin içinde.
'''
n = baslangic
adim = 0
en_yuksek = n
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1   # Collatz kuralı tek satırda
    adim += 1
    if n > en_yuksek:
        en_yuksek = n

print(f"{baslangic} → 1: {adim} adım, en yüksek değer {en_yuksek}")

# (b) GİRDİ VE DOĞRULAMA (yukarıdakiyle aynı mantık)
metin = input("Üst sınır: ").strip()
while not (metin.isdigit() and metin.isascii() and int(metin) >= 1):
    print("Uyarı: Lütfen 1 veya daha büyük bir tam sayı girin.")
    metin = input("Üst sınır: ").strip()
ust_sinir = int(metin)

'''
(b) İÇ İÇE DÖNGÜ
Dıştaki for 1'den üst sınıra kadar bütün sayıları tek tek deniyor.
İçteki while da o sayının zincirini 1'e kadar götürüp adımları sayıyor.
Daha uzun bir zincir bulunca en_uzun değişkenlerini güncelliyorum.
> kullandığım için eşitlik olursa ilk bulunan sayı kalıyor.
'''
en_uzun_sayi = 1
en_uzun_adim = 0
for aday in range(1, ust_sinir + 1):
    n = aday
    zincir_adim = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        zincir_adim += 1
    if zincir_adim > en_uzun_adim:
        en_uzun_adim = zincir_adim
        en_uzun_sayi = aday

print(f"1–{ust_sinir} arasında en uzun zincir: {en_uzun_sayi} ({en_uzun_adim} adım)")
