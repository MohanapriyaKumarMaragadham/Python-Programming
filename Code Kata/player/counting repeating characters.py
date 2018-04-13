a=raw_input().split()
print a
q=[]
d=len(a)
count=0
for i in range(0,d):
  f=a[i]
  c=len(a[i])
  for j in range(0,c):
    w=f.count(f[j])
    q.append(w)
  if(w>1):
    print f[j]
    
