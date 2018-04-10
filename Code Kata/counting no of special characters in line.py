a=raw_input()
b=a.split(".")
c=len(b)
count =0
for i in range(0,c):
	z=b[i]
	d=len(z)
	for j in range(0,d):
		if ((z[j]=='!')or(z[j]=='@')or(z[j]=='#')or(z[j]=='$')or(z[j]=='%')or(z[j]=='^')or(z[j]=='&')or(z[j]=='*')or(z[j]=='(')or(z[j]==')')or(z[j]=='_')):
			count=count+1
print count
