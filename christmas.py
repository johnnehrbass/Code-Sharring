# Created by John Nehrbass
# Oct 21, 29023
#
import random
import sys, getopt

random.seed(int(sys.argv[1]))

people = {1: 'GMa', 2: 'Dad', 3: 'Mom', 4: 'Sammie', 5: 'Jackie', 6: 'Stephen', 7: 'Roberta', 8: 'Joey', 9: 'Trevor'}
size=len(people)
mylist =list(range(1,size+1))

for i in range(1,size+1):
    random.shuffle(mylist)
    #print("{} {} {} {}".format(i,mylist,mylist[0],mylist[-1]))
    if i==mylist[0]:
        gift=mylist[-1]
        print("{} gets a gift for {}".format(people[i],people[gift]))
        del mylist[-1]
    else:
        gift=mylist[0]
        print("{} gets a gift for {}".format(people[i],people[gift]))
        del mylist[0]
        
        
