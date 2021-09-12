help = str(input("/help yazın: "))
if help == "/help":
    print("/sigaraistiyorum","/programauymadım")
what_happened = str(input("ne oldu: "))

   
def panic(wantcigared):
 if wantcigared == 1:
    print("klasöre bak sakın.txt adlı dosyayı aç")
    sakın_text = open("sakın.txt" , "x")
    sakın_text.write("Aslında sigara istemiyorsun sigara bağımlısı olduğun için ve uzun zamandır sigara içmediğin için vücudunda kinetik enerji oluştu kinetik enerjiyi şöyle atarsın; \n -Dans et(tercihim)\n -hobi edin\n -yeni arkadaşlar edin(sigara içmeyenlerden olsun \n - - - - - - - - - - - - - - - -\n WhiteCloud Software Sağlıklı Günler Diler")

def shit(rulesdontcare):
    if rulesdontcare == 1:
        fuck_text = open("görev.txt" , "w")
        fuck_text.write("PROGRAMA UYMADIĞIN İÇİN BAŞTAN BAŞLIYORUZ >:( \n -İlk Gün zorlu geçicektir çünkü bazı sigara içen arkadaşlarınıza ve (kafein nikotin) içeren ürünlere veda etmeniz gerekiyor \n biraz diyet listesi gibi olucak ama :) ; \n -sabah kahvaltısında süt bal yumurta zeytin varsa reçel tüketin \n -ağaçlık alana çıkın ve derin derin nefes alın \n -EN ÖNEMLİSİ bol bol su iç akciğerinin buna ihtiyacı çok ihtiyacı var özellikle soğuk olsun  \n (eğer) sigara içen arkadaşın mesaj atarsa hayır de \n nescafe kola v.b gazlı içecek içmiyorsun \n bunları tamamladığın an mission.exe'ye tıkla ve tamamlandı 1 yaz")

if what_happened == "/sigaraistiyorum":
    panic(1)
elif what_happened =="/programauymadım":
    yapma = str(input("sakın sigara içtim deme baba y/n?: "))
if yapma == "y":
    shit(1)
    print("Görev.txt başarıyla sıfırlanmıştır")
    
elif yapma =="n":
    print("ohh tamam gerisi önemli değil yola devam")