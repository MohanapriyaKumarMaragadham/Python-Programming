a,b=raw_input().split()
c=raw_input().split()
a=int(a)
b=int(b)
x=b
d=len(c)
if(a>b):
  while(b>=0):
    print c[-b],
    b=b-1
  z=a-x
  if((z)>1):
   for i in range(1,z):
     print c[i],
else:
  for i in range(0,d):
    print c[i],
