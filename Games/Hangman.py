import random
a=['good','bad','devil','fantasy','health','patient','adventurous','father','mother','sister','uncle','aunt','brother','grandfather','grandmother']
x=random.choice(a)
r=a.index(x)
def clue():
    if r>6:
        print "Relation of family"
    elif r<2:
        print "Two aspects of life"
    elif r==4 or r==5:
        print "related to body condition"
    else:
        print "Movie jonors"
        
w=len(x)
l=[]
p=[]
for i in range(0,w):
    p.append("_")
for i in range(0,w):
    print p[i],
for i in range(0,w):
    l.append(x[i])
print "You can have 3 choices to guess the word"
for i in range(0,3):
    a=raw_input()
    if a==x:
        print "Cogratulations"
        break
    elif a in l:
        z=l.index(a)
        p.insert(z+1,a)
        p.remove("_")
        for j in range(0,len(p)):
            print p[j],
    else:
        print "you reduced 1 choice of guessing"
        print "Need clue? press 5"
        e=int(raw_input())
        clue()
print "You failed to guess"
print "Answer is:",
print x
        
    
    

