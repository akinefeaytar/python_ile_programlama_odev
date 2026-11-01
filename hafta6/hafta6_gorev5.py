'''
Ad Soyad : Akın Efe Aytar
Numara   : 20253006037
Tarih    : 01.11.2026
Ders     : Python ile Programlama - Hafta 6 Lab
Görev 5  : Adam asmaca

Açıklama:
Gizli kelime bir değişkende duruyor. Denenen harfleri liste yerine bir
string içinde biriktiriyorum (tahminler += harf). Her turda kelimeyi
"K _ Ş U _" şeklinde ve hata sayısıyla gösteriyorum. Tek harf olmayan
girişleri ve daha önce denenmiş harfleri continue ile atlıyorum.
Kelime bitince break ile çıkıyorum, 6 hata olursa while-else ile kelimeyi gösteriyorum.
Liste ve def kullanmadım.
'''

GIZLI_KELIME = "KOŞUL"
MAKS_HATA = 6

tahminler = ""   # denenen harfler burada birikiyor
hata = 0         # yanlış tahmin sayacı

while hata < MAKS_HATA:
    '''
    Kelimenin ekranda görünecek halini hazırlıyorum.
    Tahmin edilmiş harfleri açık yazıyorum, edilmemişlerin yerine "_" koyuyorum.
    tamamlandi bayrağını True başlatıyorum, açılmamış bir harf bile
    varsa False oluyor.
    '''
    gorunum = ""
    tamamlandi = True
    for harf in GIZLI_KELIME:
        if harf in tahminler:
            gorunum += harf + " "
        else:
            gorunum += "_ "
            tamamlandi = False

    if tamamlandi:
        print(f"{gorunum}(hata: {hata}/{MAKS_HATA}) Kazandınız!")
        break   # break ile çıkınca alttaki else kısmı çalışmıyor

    print(f"{gorunum}(hata: {hata}/{MAKS_HATA})")

    '''
    GİRDİ VE DOĞRULAMA
    Birden fazla karakter, boş giriş ya da harf olmayan bir şey girilirse
    uyarı verip continue ile tekrar soruyorum.
    '''
    tahmin = input("Harf: ").strip()
    if len(tahmin) != 1 or not tahmin.isalpha():
        print("→ Lütfen yalnızca tek bir harf girin.")
        continue

    '''
    Ödevdeki ipucunda da yazdığı gibi "i".upper() "İ" değil "I" veriyor.
    Bu yüzden küçük i girilirse kendim "İ" yaptım, diğerlerinde upper yeterli.
    '''
    if tahmin == "i":
        tahmin = "İ"
    else:
        tahmin = tahmin.upper()

    if tahmin in tahminler:
        print("→ Bu harfi zaten denediniz.")
        continue

    # yeni harfi ekliyorum, kelimede yoksa hata sayısını arttırıyorum
    tahminler += tahmin
    if tahmin not in GIZLI_KELIME:
        hata += 1
        print(f"→ '{tahmin}' kelimede yok.")
else:
    '''
    while-else: döngü break ile bitmezse yani hata 6 olunca bu kısım çalışıyor.
    Kazanınca break ile çıktığımız için bu mesaj gözükmüyor.
    '''
    print(f"(hata: {hata}/{MAKS_HATA}) Kaybettiniz! Gizli kelime: {GIZLI_KELIME}")
