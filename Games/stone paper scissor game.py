p1=0
p2=0
while True:
    try:
        print "1:Stone 2:Paper 3:Scissor"
        a=int(raw_input('player 1 choice'))
        b=int(raw_input('player 2 choice'))
        if a<=3 or b<=3:
            if a==1 and b==1:
                p1=p1+0
                p2=p2+0
            elif a==2 and b==2:
                p1=p1+0
                p2=p2+0
            elif a==3 and b==3:
                p1=p1+0
                p2=p2+0
            elif a==1 and b==2:
                p2=p2+1
            elif a==2 and b==1:
                p1=p1+1
            elif a==2 and b==3:
                p2=p2+1
            elif a==3 and b==2:
                p1=p1+1
            elif a==3 and b==1:
                p2=p2+1
            elif a==1 and b==3:
                p1=p1+1
            else:
                break
        else:
            print "input you entered is invalid"
            break
    except:
        break
print "Player 1 total score is:",
print p1
print "Player 2 total score is:",
print p2
if p1>p2:
    print "Player 1 wins the game"
elif p1==p2:
    print "match draw"
else:
    print "Player 2 wins the game"

        
        
            
            
