# Akın Efe Aytar - 20253006037
# İleri Python Programlama - Hafta 4 Lab: Bonus Görev (+10 Puan)
# zamanlayici(aralik) üreteci ile 10 saniyelik tik-tak meşgul bekleme programı

import time
from uzay_oyunu.akis import zamanlayici, tik_tak_programi


def aciklama_yazdir():
    print("=" * 70)
    print("MEŞGUL BEKLEME (BUSY WAITING) VE time.sleep FARKI")
    print("=" * 70)
    print("""
1. Meşgul Bekleme (Busy Waiting / Polling):
   - Program, 'while True' döngüsü içinde sürekli olarak geçerli zamanı
     (time.perf_counter) sorgular.
   - Koşul henüz sağlanmamış olsa bile işlemci (CPU) sürekli olarak bu döngüyü
     çalıştırmaya devam eder.
   - Sonuç olarak tek bir CPU çekirdeği %100 kullanım oranına ulaşır.
   - Bu durum bataryanın hızla tükenmesine, işlemcinin ısınmasına ve diğer
     arka plan işlemlerinin CPU'dan yeterli pay alamamasına yol açar.

2. time.sleep() İle Farkı (Interrupt-driven / OS Sleep):
   - time.sleep() çağrıldığında Python, işletim sistemi çekirdeğine (kernel)
     sistem çağrısı (nanosleep vb.) gönderir.
   - İşletim sistemi bu iş parçacığını (thread) 'BLOCKED' (uyku) durumuna alır.
   - Bu süre zarfında CPU ilgili thread için HİÇBİR işlem döngüsü harcamaz (%0 CPU).
   - CPU diğer süreçleri çalıştırabilir ya da enerji tasarrufu moduna geçebilir.
   - Süre dolduğunda donanım zamanlayıcısı bir kesme (interrupt) sinyali üretir
     ve işletim sistemi thread'i tekrar 'READY' konumuna alarak uyandırır.
""")
    print("=" * 70)


if __name__ == "__main__":
    aciklama_yazdir()
    print("Tik-Tak programı başlatılıyor (10 saniye sürecek)...")
    tik_tak_programi(toplam_sure=10.0, yazdir=True)
    print("Program tamamlandı.")
