# if else structure
# nhap vao tuoi mot nguoi. Neu tuoi < 4: ve mien phi.
# neu < 18 : nua ve
# con lai full ve

ticket_price = 10
#nhap vao tuoi
age = int(input("Nhap so tuoi cua ban: "))
if age < 4:
    print(f"ban ko ton phi nhe!")
elif age <  18:
    print(f"gia ve cua ban: {age/2}")
else:
    print(f"gia ve la {age}")


#-------------------------------------
# nhap so nguoi va so tuoi cua tung nguoi tinh tong ve???
# dung OOP trong python ???
#-------------------------------------


# giai phuong trinh bac 2: ax2 + bx + c = 0
# delta = b*b - 4*a*c
# ham can **0.5 int(number**0.5)

a = int(input("nhap a: "))
b = int(input("nhap b: "))
c = int(input("nhap c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("pt vo so nghiem")
        else:
            print("pt vo nghiem")
    else:
        print(f"pt co nghiem la: {-c/b}")
else: #a !=0
    delta = b*b - 4*a*c
    if delta < 0:
        print("pt vo nghiem")
    elif delta == 0:
        print(f"pt co nghiem kep: {-b/2*a}")
    else:
        print(f"pt co 2 nghiem la: x1 = {
              (-b + delta**0.5)/(2*a)}, x2 = {(-b - delta**0.5)/(2*a)}")
