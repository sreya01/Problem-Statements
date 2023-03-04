#kth smallest element in a list
a=[1,1,2,2,3,4,4,4,5,5,5,5]
k=5
lista=list(set(a))
counter=[]
for i in lista:
    c=a.count(i)
    counter.append(c)
pairs = list(zip(lista, counter))
counter.sort()
for p in pairs:
    if p[1]==counter[k-1]:
        print(p[0])