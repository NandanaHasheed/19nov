'''
Author: Nandana Hasheed
Date:19-11-2024
python program to print reverse hill pattern
'''
row=int(input("Enter the number of row"))
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end=" ")

    for k in range(1,2*i):
         print("*",end=" ")
    print(" ")