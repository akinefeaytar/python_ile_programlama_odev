'''
Ad Soyad : Akın Efe Aytar
Numara   : 20253006037
Tarih    : 01.11.2026
Ders     : Python ile Programlama - Hafta 6 Lab
Görev 2  : Metin analizörü

Açıklama:
Kullanıcıdan bir cümle alıyorum. Tek bir for döngüsüyle harf, sesli harf,
sessiz harf, rakam ve kelime sayısını buluyorum. Kelimeleri saymak için
bayrak kullandım. Sonra cümleyi ters yazdırıp palindrom olup olmadığına bakıyorum.
Liste ve def kullanmadım.
'''

SESLILER = "aeıioöuü"

'''
GİRDİ VE DOĞRULAMA
Kullanıcı boş bir şey girerse ya da sadece boşluk girerse tekrar soruyorum.
'''
cumle = input("Cümle: ")
while cumle.strip() == "":
    print("Uyarı: Boş cümle girilemez.")
    cumle = input("Cümle: ")

'''
Sayaçları sıfırdan başlatıyorum.
kelime_icinde benim bayrağım: şu an bir kelimenin içinde miyim onu tutuyor.
harfler değişkeninde sadece harflerin küçük hallerini biriktiriyorum,
bunu palindrom kontrolü için kullanacağım.
'''
harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0
kelime_icinde = False
harfler = ""

for karakter in cumle:
    '''
    Kelime sayma mantığı:
    Boşluk görünce bayrağı False yapıyorum. Boşluk olmayan bir karakter
    gelince eğer bayrak False ise yeni bir kelime başlamış demektir,
    sayacı 1 arttırıp bayrağı True yapıyorum.
    Böyle yapınca arka arkaya birkaç boşluk olsa bile yanlış saymıyor.
    "Adana'da" gibi kesme işaretli kelimeler de tek kelime sayılıyor.
    '''
    if karakter.isspace():
        kelime_icinde = False
    elif not kelime_icinde:
        kelime_sayisi += 1
        kelime_icinde = True

    if karakter.isalpha():
        harf_sayisi += 1

        '''
        Burada Türkçe karakter sorunu var: Python "I".lower() yapınca "i"
        veriyor ama Türkçede "ı" olması lazım. "İ".lower() da garip bir şekilde
        iki karakterlik bir şey veriyor. Bu yüzden bu iki harfi kendim düzelttim.
        '''
        if karakter == "I":
            kucuk = "ı"
        elif karakter == "İ":
            kucuk = "i"
        else:
            kucuk = karakter.lower()

        harfler += kucuk

        if kucuk in SESLILER:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1
    elif karakter.isdigit():
        rakam_sayisi += 1

# [::-1] yazıyı sondan başa doğru okuyor, yani ters çeviriyor
ters_cumle = cumle[::-1]

'''
Palindrom kontrolü: sadece harflerden oluşan küçük harfli yazı
tersiyle aynıysa palindromdur. Boşluk ve kesme işaretini saymıyorum.
'''
palindrom_mu = harfler != "" and harfler == harfler[::-1]

# ÇIKTI KISMI
print(f"Harf: {harf_sayisi} Sesli: {sesli_sayisi} Sessiz: {sessiz_sayisi} "
      f"Rakam: {rakam_sayisi} Kelime: {kelime_sayisi}")
print(f"Ters: {ters_cumle}")
if palindrom_mu:
    print("Palindrom")
else:
    print("Palindrom değil")
