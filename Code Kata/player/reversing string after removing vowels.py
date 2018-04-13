a=raw_input()
d=len(a)
z=[]
for i in range(1,d):
  z.append(a[-i])
z.append(a[0])
for i in z:
  if i=='a':
    z.remove(i)
  elif i=='e':
    z.remove(i)
  elif i=='i':
    z.remove(i)
  elif i=='o':
    z.remove(i)
  elif i=='u':
    z.remove(i)
k="".join(z)
print k
