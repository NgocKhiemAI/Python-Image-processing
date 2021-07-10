def find_sencond(lst):
    lst.sort(reverse=True)
    return lst[1]
lst=[]
n=int(input("nhap n: "))
for i in range(n):
    lst.append(int(input(f"Nhap phan tu {i+1}: ")))
print(find_sencond(lst))