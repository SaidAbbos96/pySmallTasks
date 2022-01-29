# filegacha path
path = "operations_of_files/"

# 'w'
# open('file.txt','w')
# Faylni yozish uchun ochish. Fayl mavjud bo'lmasa yangi fayl yaratiladi. Fayl mavjud bo'lsa tarkibi o'chib ketadi
# 'r'
# open('file.txt','r')
# Faylni faqat o'qish uchun ochish (yozib bo'lmaydi)
# 'w+'
# open('file.txt','w+')
# Faylni o'qish va yozish uchun ochish. Fayl mavjud bo'lmasa yangi fayl yaratiladi. Fayl mavjud bo'lsa tarkibi o'chib ketadi.
# 'r+'
# open('file.txt','r+')
# Faylni o'qish va yozish uchun ochish.
# 'a'
# open('file.txt','a')
# Faylga ma'lumot qo'shish uchun ochish. Fayl mavjud bo'lmasa yangi fayl yaratiladi.
# 'a+'
# open('file.txt','a+')
# Faylga ma'lumot qo'shish va o'qish uchun yozish. Fayl mavjud bo'lmasa yangi fayl yaratiladi.


# fileni yozish uchun ochamiz yoki yaratib yozamiz
with open(path + "test.txt", "w") as file:
    file.write("bu test file edi")

# fileni o'qish uchun ochamiz
with open(path + "test.txt", "r") as file:
    for line in file:
        print(line)
