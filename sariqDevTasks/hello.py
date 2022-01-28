'''
Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:
"Nexia", "Tico", 'Damas' ko'rganlar qilar havas
Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:
5 ning 4-darajasini toping
22 ni 4 ga bo'lganda qancha qoldiq qoladi?
Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
Diametri 12 ga teng bo'lgan doiraning yuzini toping  ( deb oling)
Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
'''
# print("Nexia", "Tico", "'Damas' ko'rganlar qilar havas")
# print(5**4)
# print(22%4)
# tomon = 125
# print(tomon * tomon)
# print((tomon + tomon)*2)

# AMALIYOT
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# Ro'yxatning uzunligini konsolga chiqaring
# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# Asl ro'yxatni qaytadan konsolga chiqaring
# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# Ro'yxatdagi elementlar sonini hisoblang
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.


# countres = ["uzb", "rus", "usa"]
# print(type(countres))
# print(len(countres))
# print(sorted(countres))
# print(sorted(countres, reverse=True))
# countres.reverse()
# print(countres)
# countres.sort()
# print(countres)
# countres.sort(reverse=True)
# print(countres)
# numbers = list(range(120, 1200, 2))
# # print(numbers)
# print(sum(numbers))
# print(max(numbers) - min(numbers))
# print(len(numbers))
# print(numbers[:20])
# center = len(numbers) // 2
# print(numbers[center:center+20])
# print(numbers[len(numbers) - 20:])

# taomlar = ["osh", "somsa", "manti", "tuxum", "quymoq"]
# nonushta = taomlar[:]
# print(taomlar)
# nonushta.remove("somsa")
# nonushta.remove("manti")
# nonushta.append("qaymoq")
# nonushta.append("shokolad")
# print(nonushta)
# print(type(nonushta))
# nonushta = tuple(nonushta)
# print(type(nonushta))
# nonushta[2] = "patir" # typeError beradi