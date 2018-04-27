a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
s=0
pos=[]
oy=[]
ui=[]
for i in range(0,a):
    a=raw_input().split()
    l.append(a)
print l
for i in range(0,len(l)):
    k=l[i]
    t=l[i]
    for j in range(0,len(k)):
        if '0' in k[j]:
            u=k.index('0')
            ui.append(u)
            k=[]
            for r in range(0,len(l[i])):
                k.append('0')
            oy.append(k)
            k=[]
            break
        else:
            s=s+1
    if s==b:
        for z in range(0,b):
            pos.append(t[z])
        oy.append(pos)
        pos=[]
    s=0
print oy
print ui
for i in oy:
	for j in range(0,len(i)):
		if j in ui:
			i.insert(j+1,'0')
			i.remove('0')
	print i


        
    
                
