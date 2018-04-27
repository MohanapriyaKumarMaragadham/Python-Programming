print "This is an assessment test with simple GK questios"
print "1:Science  2:Basic Maths  3:General"
import time
w=[]
def questions():
    while True:
        print f.readline(),
        line=f.readline()
        if line:
            b=int(raw_input())
            w.append(int(b))
        else:
            break
def answers():
    s=0
    if a==2:
        ans=[6,0,209,-103,176]
    elif a==1:
        ans=[1,1,1,1,2]
    elif a==3:
        ans=[2,2,1,1,2]
    for i in range(0,5):
          if w[i]==ans[i]:
            s=s+1
    print "YOUR SCORE IS PROCESSING"
    print "Kindly wait............"
    time.sleep(10)
    print "your score out of 5 is:",
    print s
    
a=int(raw_input())
if a==2:
    f=open('C:/Users/V-TECH SOLUTIONS/Desktop/file/priya.txt')
    questions()
    answers()
elif a==1:
    f=open('C:/Users/V-TECH SOLUTIONS/Desktop/file/priya1.txt')
    questions()
    answers()
elif a==3:
    f=open('C:/Users/V-TECH SOLUTIONS/Desktop/file/priya2.txt')
    questions()
    answers()
   
