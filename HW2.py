#Задание 2 
# Факториал

# def factorial(n):
# 	result = 1
# 	i=1
# 	while i<=n:
# 		result*=i
# 		i+=1
# 	return result

# n = int(input('Enter a number: '))
# result = factorial(n)
# print(result)

# Задание 1 
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# number=input('Введите вещественное  число')
# result = 0
# for char in number:
#     if char.isdigit():
#         result += int(char)
# print(f'{number} -> {result}')


# Задание 3 
# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# n = int(input("Input number  N: "))
# result_array = [0] * n
# summ = 0
# for i in range(n):
#     result_array[i] = (1 + 1/(i + 1))**(i+1)
#     summ += result_array[i]

# print(f"Sequence: \r\n {result_array}")
# print(f"Sum: {summ}")

import time
test_list = [a for a in range(20)]
print("The original list is : " + str(test_list))
for i in range(len(test_list)):
    n=str(time.time())[-1]
    j=int(n)
    if j < len(test_list):
     test_list[i], test_list[j] = test_list[j], test_list[i]

print("The shuffled list is : " + str(test_list))