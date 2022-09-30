l=[]
n=int(input("Enter no.of elements:"))
print("Enter elements:")
for i in range(n):
    e=int(input())
    l.append(e)
x=int(input("Enter the element to be found:"))
f=0
for i in range(n):
    if x==l[i]:
        f=1
        print("Element found at:",i)
        break
    else:
        i=i+1
if f==0:
    print("Element not present in the list")