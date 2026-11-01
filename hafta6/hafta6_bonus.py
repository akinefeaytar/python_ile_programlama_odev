'''
Ad Soyad : Akın Efe Aytar
Numara   : 20253006037
Tarih    : 01.11.2026
Ders     : Python ile Programlama - Hafta 6 Lab
Bonus    : Luhn kontrol hanesi

Açıklama:
453914880343646 numarasının sonuna 0'dan 9'a kadar rakamları sırayla ekleyip
Luhn algoritmasına göre geçerli olup olmadığına bakıyorum.
İlk geçerli rakamı bulunca break ile çıkıyorum. (Cevap 7 çıkmalı)

Luhn algoritması nasıl çalışıyor:
Sağdan başlayarak her ikinci hane 2 ile çarpılıyor, sonuç 9'dan büyükse
9 çıkarılıyor. Sonra bütün haneler toplanıyor, toplam 10'a tam
bölünüyorsa numara geçerli oluyor.
Liste ve def kullanmadım.
'''

TABAN_NUMARA = "453914880343646"

for kontrol_hanesi in range(10):
    aday = TABAN_NUMARA + str(kontrol_hanesi)   # sonuna rakamı ekleyince 16 hane oluyor

    '''
    Sağdan başlamam gerektiği için aday[::-1] ile numarayı ters çevirdim.
    konum 0 en sağdaki hane oluyor, tek konumlar (1,3,5...) da
    sağdan her ikinci haneler oluyor, onları 2 ile çarpıyorum.
    '''
    toplam = 0
    konum = 0
    for karakter in aday[::-1]:
        hane = int(karakter)
        if konum % 2 == 1:
            hane *= 2
            if hane > 9:
                hane -= 9
        toplam += hane
        konum += 1

    if toplam % 10 == 0:
        print(f"Kontrol hanesi: {kontrol_hanesi}")
        print(f"Geçerli numara: {aday} (Luhn toplamı: {toplam})")
        break
else:
    # normalde her zaman bir rakam bulunuyor, bunu sadece ne olur ne olmaz diye yazdım
    print("Geçerli bir kontrol hanesi bulunamadı.")
