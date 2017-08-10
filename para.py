from sys import argv
import sys
def parameter(arg1):
    for i in arg1:
        print i
    a=len(arg1)
    print ("You pass arg no is:",a)




n=sys.argv[1:]
parameter(n)