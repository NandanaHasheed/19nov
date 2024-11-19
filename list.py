'''
Author: Nandana Hasheed
Date:19-11-2024
python program to check whether a number is prime or not
'''
first_list=[1,2,3,4,5]
second_list=[]
for number in first_list:
    if number not in second_list:
        second_list.append(number)
print("The original list is :",second_list)
print(second_list)