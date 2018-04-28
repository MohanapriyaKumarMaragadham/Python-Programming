import random
a=['good','bad','devil','fantasy','health','patient','adventurous','father','mother','sister','uncle','aunt','brother','grandfather','grandmother']
x=random.choice(a)
r=a.index(x)
def clue():
    if r>6:
        print ("Relation of family")
    elif r<2:
        print ("Two aspects of life")
    elif r==4 or r==5:
        print ("related to body condition")
    else:
        print ("Movie jonors")
        
w=len(x)
l=[]
p=[]
print ("length of word is:")
print (w)
for i in range(0,w):
    p.append("_")
for i in range(0,w):
    print (p[i],end=" ")
for i in range(0,w):
    l.append(x[i])
print ("\n")
print ("You can have 3 choices to guess the word")
print ("Need clue? press 5")
print ("if you press 5 your chance of guessing word is reduced by 1")
for i in range(0,3):
    e=input()
    if e=='5':
        clue()
    else:
        a=e
    if a==x:
        print ("Cogratulations")
        break
    elif a in l:
        z=l.index(a)
        p.insert(z+1,a)
        p.remove("_")
        for j in range(0,len(p)):
            print (p[j],end=" ")
    else:
        print ("you reduced 1 choice of guessing")
if a!=x:
    print ("\n")
    print ("you failed to guess")
    print ("answer is:")
    print (x)
    
