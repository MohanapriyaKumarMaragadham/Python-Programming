a=raw_input()
if a.isdigit():
    l=[]
    w=[]
    z=[]
    s=1
    pt=[]
    for i in range(0,len(a)):
        l.append(a[i])
    t=all(int(l[i]) <= int(l[i+1]) for i in xrange(len(l)-1))
    if t==True:
        temp=l[len(a)-1]
        l.remove(temp)
        temp1=l[len(a)-2]
        l.remove(temp1)
        l.append(str(temp))
        l.append(str(temp1))
        print "".join(l)
    elif t==False:
        r=all(int(l[i]) >= int(l[i+1]) for i in xrange(len(l)-1))
        if r==True:
            print "impossible"
        else:
            o=len(l)-1
            f=o
            largest=int(l[o])
            z.append(largest)
            while o>0:
                inp=int(l[o-1])
                if inp>=largest:
                    s=s+1
                    z.append(inp)
                    o=o-1
                else:
                    break
            q=f-s
            temp=l[q]
            l[q]=l[f]
            l[f]=temp
            for j in range(q+1,len(l)):
                w.append(l[j])
            w.sort()
            for j in range(0,q+1):
                pt.append(l[j])
            for j in range(0,len(w)):
                pt.append(w[j])
            print "".join(pt)
else:
    print "invalid"
                
      
