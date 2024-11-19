'''
Author: Nandana Hasheed
Date:19-11-2024
python program to print decreasing triangle
'''
row=int(input("Enter the number of rows"))
for i in range(1,row+1):
 for j in range(i,row+1):
     print('*',end=" ")
 print()
