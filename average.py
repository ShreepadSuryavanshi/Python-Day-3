# program for finding average of list

l = [1,2,3,4,5,6,7]
avg=0
sum=0
for i in  l:
    sum+=i
    avg=sum//len(l)
print(avg)