import random


def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


print("==================Сортування бульбашкою==================")
arr = []
n = int(input("Введіть довжину масиву: "))
for i in range(0, n):
    # element = int(input("arr[" + str(i + 1) + "] = "))
    element = random.randint(0, 99)
    arr.append(element)
print("Масив: ")
print(arr)
bubble_sort(arr)
print("Відсортований масив: ")
print(arr)
