
a=int(input())
s=0
c=a*a
for i in range(c):
    i=c%10
    s=s+i
    c=c//10
sum=int(s)
if(a==sum):
    print('Neon Number')
else:
    print('Not Neon Number')
