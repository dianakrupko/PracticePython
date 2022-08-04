numbers_list = [9.56, 3.99, 4.45, 5.0, 6, 7, 8.3, 9.7]
print("Початковий список: ",numbers_list)
print("Сума всіх елементів списку: ",sum(numbers_list))
print("Кількість елементів: ",len(numbers_list))
new_elem=sum(numbers_list)/len(numbers_list)
print("Середнє арифметичне: ",new_elem)
numbers_list.append(new_elem)
print("Новий список: ",numbers_list)