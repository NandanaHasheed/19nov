'''
Author: Nandana Hasheed
Date:19-11-2024
python program to merge 2 list
'''
list1=[]
list2=[]
list1_size=int(input("Enter the size of list 1"))
print("Enter the elements of list 1: ")
for i in range(list1_size):
    list1.append(int(input()))
list2_size=int(input("Enter the size of second list"))
print("Enter the elements of list 2: ")
for i in range(list2_size):
    list2.append(int(input()))
print("list 1= ",list1,"\n","List 2 = ",list2)
combinedlist=list1+list2
print("Combined list= ",combinedlist)
evenlist=[]
oddlist=[]
for i in combinedlist:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("Even List= ",evenlist)
print("Odd List= ",oddlist)
evenlist.sort()
oddlist.sort()
print("Sorted even list =",evenlist)
print("Sorted odd list =",oddlist)
combinedlist=evenlist+oddlist
combinedlist.sort()
print("Combined even and odd list =",combinedlist)