# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:11:33 2023

@author: Bobur
"""

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"

#print(viloyat + " viloyati, "+ tuman + " tumani,\n "+ mahalla + " mahallasi, " + kocha + " ko'chasi")

# ism = input("ismingiz: ")
# familiya = input("familiyangiz: ")
# print(f"assalom alaykum  {ism}  {familiya}")

            # Sonlar bilan ishlash
            
# a = input("istalgan sonni kiriting: ")
# a = int(a)
# print(f"{a} ning kvadrati {a**2} ga teng")
# print(f"{a} ning kubi {a**3} ga teng")

# yosh = int(input("yoshingiz nechchida:" ))
# print(f"siz {2023-yosh} yilda tug'ilgansiz")


            # List (Royxatlar)
            
# dostlar = ['Asqar', 'Nodir', 'Alisher']
# print(f"salom do'stim {dostlar[0]} qaleysan" )
# print(f"{dostlar[1]} halyam yuripsanmi o''sha boyvachcha o'rtolaring bilan a")

# tarixiy_shaxslar = ["Amir Temur", "Umar Hayyom", "Alisher Navoiy"]
# zamonaviy_shaxslar = ["Muhammadali Esonqulov", "Shahvkat Mirziyoyev", "Rustamjon domla"]
# print(f"men tarixiy shaxslardan {tarixiy_shaxslar.pop(1)} bilan \n zamonaviy shaxslardan esa {zamonaviy_shaxslar.pop(1)} bilan ko'rishishni hohlar edimeeee")
# print(zamonaviy_shaxslar,  tarixiy_shaxslar)



            # Ro'yxatlar bilan ishlash
            
            
# davlatlar = ["Falastin", "BAA", "Qatar", "Misr", "Arabiston"]
# print(sorted(davlatlar))

juft_sonlar=list(range(120, 1201, 2))
# print(juft_sonlar)
# print(sum(juft_sonlar))
# print(max(juft_sonlar)-min(juft_sonlar))
# print(len(juft_sonlar))
# print(f"{juft_sonlar[:10]} \n {juft_sonlar[270:280]} \n {juft_sonlar[-10:]}")
# print(juft_sonlar[:10])
# print(juft_sonlar[270:280])
# print(juft_sonlar[-10:])


            # for sikli bilan tanishamiz
            
# ismlar = ["Suxrob", "Nurbek", "Sirojiddin", "Xumoyiddin"]
# for ism in ismlar:
#     print(f"{ism} ko't bopqopsanku oshna")
# print(f"kod {len(ismlar)} marta takrorlandi")

# sonlar = list(range(10, 101))
# sonlar_kubi = []
# for son in sonlar:
#     sonlar_kubi.append(son**3)
# print(sonlar)
# print(sonlar_kubi)

# kinolar = []
# print("5 ta sevimli kinolar nomini kiriting: ")
# for n in range(5):
#     kinolar.append(input(f"{n+1} - kino nomini kiriting: "))
# print(kinolar)


            
            # if - else sart operatori
            
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if(car!="gm"):
#         print(car.title())
#     else:
#         print(car.upper())
    
# login = input("isminizni kiriting: ")
# if(login.lower() =="admin"):
#     print("Xush kelibsiz Admin! Foydalanuvchilar ro'yxatini korasizmi? ")
# else:
#     print(f"Xush kelibsiz {login}")

# son = int(input("istalgan son kiriting: "))
# if(son > 0):
#     print("musbat son")
# else:
#     print("manfiy son")



            #if elif else
            
# yosh =int( input("yoshingizni kiriting: "))
# if(yosh<4 or yosh>60):
#     print("Sizga bepul")
# elif(yosh<18):
#     print("Sizga kirish 10000 so'm")
# else:
#     print("Sizga kirish 20000 so'm pul")

# mahsulotlar = ["non", "un", "shakar", "tuz", "kartoshka", "sabzi", "piyoz", "karom", "olma", "nok"]
# savat=[]
# for mahsulot in range(5):
#     mahsulot=input("olmoqchi bo'lgan mahsulot nomini kiriting: ")
#     savat.append(mahsulot)
#     if(mahsulot in mahsulotlar):
#         print("Mahsulot do'konimizda bor")
#     else:
#         print("Mahsulot do'konimizda yo'q")



        #Lug'at 

# otam={"ismi": "G'anisher", "familiyasi": "Pardayev", "Yayashash manzili": "Toshkent shahri", "tugilgan yili": "1964 yilda" }
# print(f"Menin otam {otam['ismi']}, familyasi {otam['familiyasi']} {otam['tugilgan yili']}da tug'ilgan")

# word = input("biror soz kiriting: \n>>>>>")
# dictionary = {"apple": "olma", "pen": "ruchka"}
# # print(word + " so'zining ma'nosi " + dictionary.get(word))
# print(f"{word} so'zining tarjimasi {dictionary.get(word)}")



        # Luatda islash

# python_dictionary = {"if":"agar", "for":"uchun", "begin":"boshlash","end":"tamom"}
# for k,v in sorted(python_dictionary.items()):
#     # print(k + " so'zining ma'nosi "+v)
#     print(f"{k} so'zining ma'nosi {v}")

# countrys = {"Uzbekistan":"toshkent", "USA":"new york", "Qatar":"doxa"}
# print(sorted(countrys.keys()))
# print(sorted(countrys.values()))

# countrys = {"Uzbekistan":"toshkent", "USA":"new york", "Qatar":"doxa"}
# country=input("Istalgan davlatni kiriting: \n>>>>> ")
# print(countrys.get(country))



            # Nesting (ichc ma ich lug'at)
            
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlari': ['din', 'islom axloqlari', 'arab istilosi']
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlari': ['til dil', 'o\'tkan kunlar', 'mehrobdan chayon']
           
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlari': ['o\'zbekiston', 'vatan']
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlari': ['hayrat ul abror', 'farhod va shirin', 'layli va majnun']
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism']} ning yozgan asarlari quyidagilar:\   n")
#     for asar in shaxs['asarlari']:
#         print(f"{asar} \n")


            # wile sikli

# kitoblar=[]
# while True:
#     kitob = input("Yaxsi ko'rgan kitob nomini kiriing: \n " + "stop so'zini bossaniz tugaydi \n >>>>>")
#     kitoblar.append(kitob)
#     if(kitob=="stop"):
#         break;
# print(kitoblar)

# while True:
#     qiymat =input("Yoshingnizni kiriting: \n>>>>>")
#     if(qiymat=="quit" or qiymat == "exit"):
#         break
#     yosh = int(qiymat)
    
#     if(yosh<7):
#         narx=2000
#     elif(7<=yosh<18):
#         narx=3000
#     elif(18<=yosh<65):
#         narx = 10000
#     else:
#         narx=0    
#     if(narx==0):
#         print("'bepul sizga togo'")
#     else:
#         print(f" {yosh} ga muzeyga kirish {narx}")

    

            # Funksiyalar
            
# def yoshini_bilish(ism, yosh):
#     print(f"{ism.title()}ning tug'ilgan yili {2023-yosh} yil")
# yoshini_bilish("Asqar", 30)

# def taqqoslash(son1, son2):
#     if(son1>son2):
#         print(son1)
#     elif(son2>son1):
#         print(son2)
#     else:
#         print("Sonlar teng!!!")

# taqqoslash(2,5)

# def bolinish_alomatlari(son):
#     for n in range(2,11):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")

# bolinish_alomatlari(20)



            # Funksiyada qiymat qaytarish
            
# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")



            # funksiyaga ro'hat tuzish
            
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()   

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()   
#         return matnlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)


        #   pytonga kiris bo'limidagi darslar kodi

