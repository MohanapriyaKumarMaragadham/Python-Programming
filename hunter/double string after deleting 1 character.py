a=raw_input()
b=len(a)
l=[]
for i in range(0,b):
    l.append(a[i])
t=len(list(set(l)))
k=b%t
if k==1:
    print "YES"
else:
    print "NO"
