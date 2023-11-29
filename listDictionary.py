# Tạo một danh sách các từ điển
people = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "San Francisco"},
    {"name": "Bob", "age": 35, "city": "Los Angeles"}
]

# In thông tin từng người trong danh sách
for person in people:
    print(f"Name: {person['name']}, Age: {
          person['age']}, City: {person['city']}")

new_person = {"name": "Eva", "age": 28, "city": "Chicago"}
people.append(new_person)

# Nhập thông tin cho new_person từ người dùng
new_person = {}
new_person["name"] = input("Enter name: ")
new_person["age"] = int(input("Enter age: "))
new_person["city"] = input("Enter city: ")

# Thêm new_person vào danh sách
people.append(new_person)

# In thông tin từng người trong danh sách
for person in people:
    print(f"Name: {person['name']}, Age: {
          person['age']}, City: {person['city']}")
