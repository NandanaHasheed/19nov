'''
Author: Nandana Hasheed
Date:19-11-2024
python program to print hill pattern
'''
row=int(input("Enter the number of row"))
for i in range(row):
    for j in range(row-i):
        print(" ",end=" ")

    for k in range(1,2*i):
         print("*",end=" ")
    print(" ")