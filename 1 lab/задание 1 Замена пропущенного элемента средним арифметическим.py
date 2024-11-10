numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = 4
summa = sum(numbers[:index]) + sum(numbers[index+1:])
count = len(numbers[0:])
average = round(summa / count, 2)
# TODO заменить значение пропущенного элемента средним арифметическим
numbers[index] = average
print("Измененный список:", numbers)
