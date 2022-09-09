
class sirket():
    def __init__(self,ad):
        self.ad = ad
        #self.calisma = True

#******************************************************************************************************************************************

    def program(self):
        secim = self.menusecim()

        if secim == 1:
            self.calisanekle()
        if secim == 2:
            self.calisancikar()
        if secim == 3:
            ay_yil_secim = input("yıllık bazda görmek ister misiniz?e/h : ")
            if ay_yil_secim == "e":
                self.verilecekmaasgöster(hesap="y")
            else:
                self.verilecekmaasgöster()
        if secim == 4:
            self.maaslariver()
        if secim == 5:
            self.masrafgir()
        if secim == 6:
            self.gelirgir()
        if secim == 7:
            self.listele()

#******************************************************************************************************************************************

    def menusecim(self):
        secim = int(input("\n**** {} otomasyona hoş geldiniz ****\n\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek Maaş Göster\n4-Maaşları Ver\n5-Masraf Gir\n6-Gelir Gir\n7-Çalışanları Listele\n\nSeçiminizi Giriniz : ".format(self.ad)))
        while secim < 1 or secim > 7:
            secim = int(input("lütfen 1-6 arası bir değer gir! : "))
        return secim

#******************************************************************************************************************************************

    def calisanekle(self):
        id = 1
        ad = input("çalışanın adını gir : ")
        soyad = input("çalışanın soyadını gir : ")
        yas = input("çalışanın yaşını gir : ")
        cinsiyet = input("çalışanın cinsiyetini gir : ")
        maas = input("çalışanın maaşını gir : ")
        
        with open("calisanlar.txt","r",encoding="utf-8") as dosya:
            calisanlistesi = dosya.readlines()
        if len(calisanlistesi) == 0:
            id = 1
        else:
            with open("calisanlar.txt","r",encoding="utf-8") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
        
        with open("calisanlar.txt","a+",encoding="utf-8") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))

#******************************************************************************************************************************************

    def calisancikar(self):
        with open("calisanlar.txt","r",encoding="utf-8") as dosya:
            calisanlar = dosya.readlines()

        gosterilcekcalisanlar = []

        for calisan in calisanlar:
            gosterilcekcalisanlar.append(" ".join(calisan[:-1].split("-")))
        
        for calisan in gosterilcekcalisanlar:
            print(calisan)

        secim = int(input("lütfen çıkarmak istediğiniz çalışanın numarasını gir(1-{}) : ".format(len(gosterilcekcalisanlar))))

        while secim < 1 or secim > len(gosterilcekcalisanlar):
            secim = int(input("lütfen 1-{} arası değer gir : ".format(len(gosterilcekcalisanlar))))

        calisanlar.pop(secim-1)

        sayac = 1

        degisimcalisanlar = []

        for calisan in calisanlar:
            degisimcalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
            sayac+=1
        
        with open("calisanlar.txt","w",encoding="utf-8") as dosya:
            dosya.writelines(degisimcalisanlar)

#******************************************************************************************************************************************

    def verilecekmaasgöster(self,hesap="a"):
        with open("calisanlar.txt","r",encoding="utf-8") as dosya:
            calisanlar = dosya.readlines()

        toplam = 0
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(calisan[2:].split("-")[0] + " " + calisan.split("-")[1] + ": " + calisan.split("-")[-1])
            toplam += int(calisan.split("-")[-1])
        for calisan in maaslar:
            print(calisan[0:-1] + "TL")

        if hesap == "a":
            print("bu ay toplam vermeniz gereken maas : {}".format(toplam))
        else:
            print("bu yıl toplam vermeniz gereken maas : {}".format(toplam*12))
        
#******************************************************************************************************************************************

    def maaslariver(self,hesap="a"):
        with open("calisanlar.txt","r",encoding="utf-8") as dosya:
            calisanlar = dosya.readlines()
        
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        toplammaas = sum(maaslar)


        with open("butce.txt","r",encoding="utf-8") as dosya:
            toplambutce = int(dosya.readlines()[0])

        toplambutce -= toplammaas

        with open("butce.txt","w",encoding="utf-8") as dosya:
            dosya.write(str(toplambutce))

#******************************************************************************************************************************************

    def masrafgir(self):
        masrafadi = input("lütfen masrafın adını gir : ")
        masraf = int(input("lütfen masraf tutarını gir : "))


        with open("butce.txt","r",encoding="utf-8") as dosya:
            toplambutce = int(dosya.readlines()[0])

        with open("butce.txt","w",encoding="utf-8") as dosya:
            dosya.write(str(toplambutce-masraf))

        with open("masraflar.txt","a",encoding="utf-8") as dosya:
            dosya.write(masrafadi + ": " + str(masraf) + "TL\n")

        print("masraf bütçeden düşüldü ve masraflar dosyasına yazıldı")

#******************************************************************************************************************************************

    def gelirgir(self):
        geliradi = input("lütfen gelirin adını gir : ")
        gelir = int(input("lütfen gelir tutarını gir : "))


        with open("butce.txt","r",encoding="utf-8") as dosya:
            toplambutce = int(dosya.readlines()[0])

        with open("butce.txt","w",encoding="utf-8") as dosya:
            dosya.write(str(toplambutce+gelir))

        with open("gelirler.txt","a",encoding="utf-8") as dosya:
            dosya.write(geliradi + ": " + str(gelir) + "TL\n")

        print("gelir bütçeye eklendi ve gelirler dosyasına yazıldı")

#******************************************************************************************************************************************

    def listele(self):
        with open("calisanlar.txt","r",encoding="utf-8") as dosya:
            calisanlar = dosya.readlines()
            
        gosterilcekcalisanlar = []

        for calisan in calisanlar:
            gosterilcekcalisanlar.append(" ".join(calisan[:-1].split("-")))
        
        for calisan in gosterilcekcalisanlar:
            print(calisan)

#******************************************************************************************************************************************

Sirket = sirket("muhammet köseoğlu")

while True:
    Sirket.program()