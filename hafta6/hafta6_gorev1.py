'''
Ad Soyad : Akın Efe Aytar
Numara   : 20253006037
Tarih    : 01.11.2026
Ders     : Python ile Programlama - Hafta 6 Lab
Görev 1  : Üçgen analizörü

Açıklama:
Kullanıcıdan üç kenar alıyorum. Kenarlardan biri pozitif değilse ya da
üçgen eşitsizliği sağlanmıyorsa uyarı veriyorum. Üçgen oluşuyorsa
kenarlarına göre (eşkenar/ikizkenar/çeşitkenar) ve en büyük açısına göre
(dar/dik/geniş) sınıflandırıp çevre, alan ve en büyük açıyı yazdırıyorum.
Liste ve def kullanmadım.
'''

import math

'''
GİRDİ KISMI
3 kenarı ayrı ayrı yazmak yerine "abc" yazısı üzerinde for döngüsü kurdum,
her harf bir kenarın adı oluyor. Liste kullanamadığım için okuduğum sayıyı
if/elif ile a, b veya c değişkenine atadım.
Kullanıcı sayı yerine harf falan girerse while döngüsü aynı kenarı tekrar soruyor.
'''
a = b = c = 0.0
for etiket in "abc":
    while True:
        metin = input(f"{etiket}: ").strip().replace(",", ".")  # 2,5 yazılırsa 2.5 yapsın diye
        try:
            deger = float(metin)
        except ValueError:
            print("Uyarı: Lütfen sayısal bir değer girin.")
            continue
        '''
        float("nan") ve float("inf") hata vermiyor, o yüzden bunları da
        isfinite ile ayrıca kontrol ettim.
        '''
        if not math.isfinite(deger):
            print("Uyarı: Sonlu bir sayı girin.")
            continue
        break  # doğru sayı geldi, döngüden çıkıyorum

    if etiket == "a":
        a = deger
    elif etiket == "b":
        b = deger
    else:
        c = deger

'''
DOĞRULAMA KISMI
Önce kenarların pozitif olup olmadığına bakıyorum.
'''
if a <= 0 or b <= 0 or c <= 0:
    print("Uyarı: Kenar uzunlukları pozitif olmalıdır.")
else:
    '''
    Formülde a en uzun kenar olmalı. sort kullanamadığım için takas yaptım:
    b a'dan büyükse yer değiştiriyorlar, sonra c için de aynısı.
    '''
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a

    '''
    Üçgen eşitsizliği: en uzun kenar diğer ikisinin toplamından küçük olmalı.
    Eşit olursa üçgen düz bir çizgi oluyor, onu da geçersiz saydım.
    '''
    if a >= b + c:
        print("Uyarı: Bu kenarlarla üçgen oluşmaz (üçgen eşitsizliği sağlanmıyor).")
    else:
        '''
        HESAPLAMA KISMI
        Ondalıklı sayılarda == bazen yanlış sonuç verebiliyor, o yüzden
        kenarların eşitliğini math.isclose ile kontrol ettim.
        '''
        ab_esit = math.isclose(a, b)
        bc_esit = math.isclose(b, c)
        ac_esit = math.isclose(a, c)

        if ab_esit and bc_esit:
            kenar_turu = "Eşkenar"
        elif ab_esit or bc_esit or ac_esit:
            kenar_turu = "İkizkenar"
        else:
            kenar_turu = "Çeşitkenar"

        '''
        En büyük açı en uzun kenarın (a) karşısında olur.
        Kosinüs teoremi: cos(alfa) = (b^2 + c^2 - a^2) / (2bc)
        Bazen küçük yuvarlama hatası yüzünden sonuç 1'den biraz büyük çıkabiliyor
        ve acos hata veriyor, bu yüzden değeri -1 ile 1 arasına sınırladım.
        '''
        cos_alfa = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
        cos_alfa = max(-1.0, min(1.0, cos_alfa))
        en_buyuk_aci = math.degrees(math.acos(cos_alfa))

        # dik açıyı ödevde istendiği gibi == ile değil isclose ile kontrol ettim
        if math.isclose(en_buyuk_aci, 90):
            aci_turu = "Dik"
        elif en_buyuk_aci > 90:
            aci_turu = "Geniş"
        else:
            aci_turu = "Dar"

        '''
        Heron formülü:
        u = (a+b+c) / 2  (yarı çevre)
        Alan = karekök( u(u-a)(u-b)(u-c) )
        '''
        cevre = a + b + c
        u = cevre / 2
        alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

        # ÇIKTI KISMI (örnek çıktıdaki gibi iki ondalık)
        print(f"Tür: {kenar_turu}, {aci_turu} açılı")
        print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {en_buyuk_aci:.2f}°")
