print("hello python123 git")
#dictionary list...
dsSP = ["ong", "phu tung", "keo dan"]

for sp in dsSP:
    print(f"ds sp la: {sp}")

for k, value in enumerate(dsSP):
    print(f"ds sp la: {value}, vi tri: {k}")

#abc
if(2>1):
    print("troi mua")

person = {"name": "John", "age": 40, "city": "sai gon"}

for key, value in person.items():
    print(f"{key}: {value}", end=' | ')
