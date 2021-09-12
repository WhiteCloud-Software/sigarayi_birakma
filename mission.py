
mission_successful= input("tamamlandı (hangi günü bitirdiysen onu yaz: ")
def complete(succesful):
    if succesful == 1:
        packmission_text = open("görev.txt", "a")
        packmission_text.write(" - - - - - - - - - \n 2.GÜN \n HADİ BUGÜN BİRAZ EGZERSİZ YAPALIM!! \n - Kahvaltı olarak süt,yumurta,bal ve reçel ile yap çünkü sağlıklı beslenmek nikotin oranını azaltır \n -Egzersiz yap Squad Ve mekik tarzı \n -Ağaçlık alana çık ve derin derin nefes al \n -Daralırsan 1 dal s****a içmene izin veriyorum \n S****a içtiysen sigaradan sonra içmediysen ağaçlık alana çıktıktan sonra soğuk su iç \n -Akşam yemeğinde patlıcan ye patlıcan bağımlılığı azaltmada en önemli faktördür(kaynak:internet) günü bitirince mission.exe ye tamamlandı 2 yaz")
    elif succesful == 2:
        packmission2_text = open("görev.txt", "a")
        packmission2_text.write(".\n 3.GÜN \n HADİ BUGÜN SİGARA İÇMEYEN ARKADAŞLARLA KONUŞALIM!! \n -Kahvaltı olarak süt,yumurta,bal ve reçel ile yap \n -Saf arkadaşınızla konuşun yoksa tanışın tanışamıyorsan en yakın arkadaşınla konuş ama sigara içmeyeninden lütfen mesela benimle konuşabilirsin :) @ismailakbulutoffical \n arkadaşınla ağaçlık bir alanda oturabilirsin \n -akşam yemeği olarak patlıcan ye \n günü tamamladığın an mission.exeye tamamlandı 3 yaz ")
    elif succesful == 3:
        packmission3_text = open("görev.txt", "a")
        packmission3_text.write(".\n 4.GÜN \n HADİ BUGÜN Gezmeye Gidelim!! \n -Kahvaltı olarak süt,yumurta,bal ve reçel ile yap \n -Dolaşmaya çık \n a ağaçlık bir alana çık ve derin derin nefes al \n -Bol bol soğuk Su iç \n -akşam yemeği olarak patlıcan ye \n günü tamamladığın an mission.exeye tamamlandı 4 yaz ")
    elif succesful ==4:
        packmission4_text = open("görev.txt", "a")
        packmission4_text.write(".\n 5.GÜN \n SON GÜN!! \n BUGÜNÜN BİR ESPRİSİ YOK DÜN İLE AYNI\n -Kahvaltı olarak süt,yumurta,bal ve reçel ile yap \n -Dolaşmaya çık \n a ağaçlık bir alana çık ve derin derin nefes al \n -Bol bol soğuk Su iç \n -akşam yemeği olarak patlıcan ye \n günü tamamladığın an mission.exeye tamamlandı 5 yaz ")
    
def used(leave):
        if leave == 1:
          last_day = str(input("SİGARAYI BIRAKTIN MI y/n?: "))
        if last_day == "y":
            print("klasöre bir daha bakmanı rica edicem")
            amazing_text = open("amazing.txt","x")
            amazing_text.write("DOSTUM BU HARİKA!!! \n ŞİMDİ YAPMAN GEREKEN ŞEY ARKADAŞLARIN SANA 'SİGARA İÇER MİSİN?' DİYE SORDUKLARINDA 'HAYIR,BIRAKTIM' DİYİP HAVA ATMAK \n WhiteCloud Software Sağlıklı Günler diler \n instagram:@whitecloudsoftware \n Developer:İsmail Akbulut ")
        elif last_day =="n":
            sorry_text = open("noproblem.txt","x")
            sorry_text.write("Bu program sadece kendimi geliştirmek için yazdığım bir konsept tabiki profesyonel bir doktor değilim ama bir doktora görünsen iyi olur ya da alo 171 sigara bırakma hattını arayabilirsin \n WhiteCloud Software Sağlıklı günler diler \n Developer:İsmail Akbulut ")
      
if mission_successful == "tamamlandı 1":
    complete(1)
    print("not defteri başarıyla güncellenmiştir.")

elif mission_successful == "tamamlandı 2":
    complete(2)
    print("not defteri başarıyla güncellenmiştir.")
elif mission_successful == "tamamlandı 3":
    complete(3)
    print("not defteri başarıyla güncellenmiştir.")
elif mission_successful == "tamamlandı 4":
    complete(4)
elif mission_successful ==  "tamamlandı 5":
    used(1)    

else:
    print("yanlış değer girdiniz")