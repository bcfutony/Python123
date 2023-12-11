#nhap vao 1 mang
#tim so nguyen to
#tim tong so nguyen to

dsSoNT = [1, 2, 3, 11, 4, 5, 6, 7, 11]
def ktSNT(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number%2 == 0:
                return False
        return True

#tong cua so nguyen to
tong = 0
for i in dsSoNT:
    if(ktSNT(i)):
        print(f"{i} la so nguyen to")
        tong += i
    else:
        print(f"{i} ko la so nguyen to")

print(f"tong cua cac so nguyen to la: {tong}")

#tim so nguyen to lon nhat
def FindSNTMax():
    soNTMax = 2
    for so in dsSoNT:   
        if ktSNT(so):
            if soNTMax <= so:
                soNTMax = so
    print(f"so nguyen to lon nhat: {soNTMax}")
    return soNTMax

#tim tong so nguyen to lon nhat
tongSNT = 0
count = 0
for number in dsSoNT:
    sntmax = FindSNTMax()
    if number == sntmax:
        tongSNT += number
        count += 1

print(f"tong so nt max la: {tongSNT}, gom {count} so {FindSNTMax()}")