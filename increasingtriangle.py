'''
Author: Nandana Hasheed
Date:19-11-2024
python program to print increasing triangle
'''
row=int(input("Enter the number of row"))
for i in range(row):
 for j in range(i+1):
     print('*',end=" ")
 print(" ")
