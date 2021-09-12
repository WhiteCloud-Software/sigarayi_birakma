# sigarayı bırakma uygulaması
# sigarayı bırakın adam olun


name = str(input("isminiz nedir? :"))

user_age = int(input("kaç yaşındasınız "   +name+  " bey/hanım?: "))

if (user_age < 18):
    print("CİDDİ MİSİNİZ SİZ!!?? Neyse belki dertleriniz vardır ama hayat bir şekil devam ediyor")
else:
    pass
pack_or_branch = str(input("günde dal mı paket mi bitiriyorsun p/d?: "))

def packcigared(pack):
    if pack == 1:
       much = int(input("günde kaç paket bitiriyorsunuz?: "))
    total = much*20
    print(total , "TL bosa gidiyor demek :( Neyse Senin icin görev.txt olusturdum klasöre bak,görevlere basla WhiteCloud Software saglıklı günler diler.")
    packmission_text = open("görev.txt" , "x") 
    packmission_text.write("1.Gün \n - - - - - -\n -İlk Gün zorlu geçicektir çünkü bazı sigara içen arkadaşlarınıza ve (kafein nikotin) içeren ürünlere veda etmeniz gerekiyor \n biraz diyet listesi gibi olucak ama :) ; \n -sabah kahvaltısında süt bal yumurta zeytin varsa reçel tüketin \n -ağaçlık alana çıkın ve derin derin nefes alın \n -EN ÖNEMLİSİ bol bol su iç akciğerinin buna ihtiyacı çok ihtiyacı var özellikle soğuk olsun  \n (eğer) sigara içen arkadaşın mesaj atarsa hayır de \n nescafe kola v.b gazlı içecek içmiyorsun \n bunları tamamladığın an mission.exe'ye tıkla ve tamamlandı 1 yaz")


if pack_or_branch == "p":
    packcigared(1)
else:
    print("yanlıs deger girdiniz veya büyük harfle yazdiniz uygulamayı yeniden baslatin")