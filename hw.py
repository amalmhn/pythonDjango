lst1 = [10,20,30,40,50]
lst2 = [8,9,10,20,21]

lst3=[]
lst_common=[]

for i in lst1:
    lst3.append(i)

for j in lst2:
    if j in lst3:
        lst_common.append(j)

print('The commom numbers are',lst_common)

