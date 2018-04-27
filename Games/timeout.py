import random
from threading import Timer
timeout=False
def time():
    print "timeout"
    timeout=True
a=['good','bad','devil','fantasy','health','patient','adventurous','father','mother','sister','uncle','aunt','brother','grandfather','grandmother']
x=random.choice(a)
word=x
inp="".join(random.sample(word,len(word)))
print "you have 30 seconds to guess the word()"
print inp
t=Timer(10,time)
t.start()
c=raw_input()
if c!=None and not timeout:
    print "good"
    t.cancel()
