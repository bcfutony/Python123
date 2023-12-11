#ham trong python
x = int(input("nhap x: "))
y = int(input("nhap y: "))

def TinhTong(a, b):
    return a + b

def TinhHieu(a, b):
    return a - b
#su dung ham
kq = TinhTong(x,y)
print(f"tong cua 2 so {x} va {y} la: {kq}")

kq2 = TinhHieu(x, y)
print(f"hieu cua {x} va {y} la {kq2}")



#---------------------------------------------------
#tinh tong cua 2 so giua 2 so moi nhap
def tinh_tong(x, y):
    if x > y:
        print("Không hợp lệ, x không thể lớn hơn y.")
        return None
    else:
        tong = 0
        for so in range(x, y):
            tong += so
        return tong

# Sử dụng hàm4
ket_qua = tinh_tong(x, y)

if ket_qua is not None:
    print(f"Tổng từ {x} đến {y-1} là: {ket_qua}")
