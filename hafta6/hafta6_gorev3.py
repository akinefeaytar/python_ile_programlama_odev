'''
Ad Soyad : Akın Efe Aytar
Numara   : 20253006037
Tarih    : 01.11.2026
Ders     : Python ile Programlama - Hafta 6 Lab
Görev 3  : T.C. kimlik numarası doğrulama

Açıklama:
Numarayı metin olarak alıp önce biçimini kontrol ediyorum
(11 karakter olmalı, hepsi rakam olmalı, ilk hane 0 olmamalı).
Sonra 1,3,5,7,9. hanelerin toplamı (T) ve 2,4,6,8. hanelerin toplamı (Ç)
ile iki kontrol hanesini hesaplıyorum:
    h10 = (7T - Ç) mod 10
    h11 = (T + Ç + h10) mod 10
İkisi de numaradaki 10. ve 11. haneyle aynıysa GEÇERLİ yazıyor.
Birden fazla numara denenebiliyor, boş bırakınca program kapanıyor.
Not: Sadece test numaraları kullandım (10000000146 gibi).
Liste ve def kullanmadım.
'''

print("(Çıkmak için boş bırakıp Enter'a basın.)")

while True:
    '''
    Numarayı int yapmadan string olarak alıyorum çünkü hanelere tek tek
    ulaşmam lazım. int yapsaydım baştaki 0 da kaybolurdu.
    '''
    tc_no = input("T.C. kimlik no: ").strip()
    if tc_no == "":
        print("Program sonlandı.")
        break

    '''
    BİÇİM KONTROLÜ
    Hatalıysa nedenini yazıp continue ile başa dönüyorum.
    isdigit "²" gibi karakterlere de True dediği için isascii'yi de ekledim.
    '''
    if len(tc_no) != 11:
        print("→ GEÇERSİZ (numara 11 haneli olmalı)")
        continue
    if not (tc_no.isdigit() and tc_no.isascii()):
        print("→ GEÇERSİZ (yalnızca rakam içermeli)")
        continue
    if tc_no[0] == "0":
        print("→ GEÇERSİZ (ilk hane 0 olamaz)")
        continue

    '''
    HESAPLAMA
    İlk 9 haneyi döngüyle geziyorum. Python'da indeks 0'dan başladığı için
    indeks 0 aslında 1. hane oluyor. Yani çift indeksler (0,2,4,6,8)
    1,3,5,7,9. hanelere denk geliyor, tek indeksler de 2,4,6,8. hanelere.
    '''
    tek_toplam = 0    # T
    cift_toplam = 0   # Ç
    for indeks in range(9):
        hane = int(tc_no[indeks])
        if indeks % 2 == 0:
            tek_toplam += hane
        else:
            cift_toplam += hane

    '''
    7T - Ç negatif çıkabilir ama Python'da % işlemi negatif sayıda da
    0-9 arası bir sonuç verdiği için sorun olmuyor.
    '''
    hane10 = (7 * tek_toplam - cift_toplam) % 10
    hane11 = (tek_toplam + cift_toplam + hane10) % 10

    gecerli = hane10 == int(tc_no[9]) and hane11 == int(tc_no[10])

    # ÇIKTI KISMI
    if gecerli:
        print(f"Tek: {tek_toplam} Çift: {cift_toplam} "
              f"10. hane: {hane10} 11. hane: {hane11} → GEÇERLİ")
    else:
        print("→ GEÇERSİZ")
        print(f"  (Hesaplanan kontrol haneleri: {hane10}{hane11}, "
              f"numaradaki: {tc_no[9]}{tc_no[10]})")
