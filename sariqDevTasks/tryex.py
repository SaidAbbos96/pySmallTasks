raqam = input("Raqamni kiriting: ")
try:
    raqam = int(raqam)
    # raqam = raqam
    print("Try block boshlandi !!!")
except ValueError:
    print("except ValueError bajarildi !!!")
except ZeroDivisionError:
    print("except ZeroDivisionError bajarildi !!!")
else:
    print("else bajarildi !!!")
    print(raqam * raqam)
finally:
    print("finally bajarildi !!!")

print("Dastur ohirigacha bajarildi !!!")