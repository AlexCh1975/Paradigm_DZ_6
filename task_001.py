"""
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.

"""

from random import randint

def find(numbers, num):
    length_left = 0
    length_right = len(numbers) - 1
    length_center = (length_left + length_right) // 2
    
    while numbers[length_center] != num:
        if num > numbers[length_center]:
            length_left = length_center + 1
        else:
            length_right = length_center - 1
        length_center = (length_left + length_right) // 2
        if length_left >= length_right:
            break
    
    if num == numbers[length_center]:
        return length_center
    else:
        return -1

numbers = [randint(1, 100) for i in range(15)]
numbers.sort()
print(numbers)
num = int(input())
print(f'index = {find(numbers, num)}')
 
