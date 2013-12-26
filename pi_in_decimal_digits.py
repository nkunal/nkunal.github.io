# This Programs finds the value of PI, a mathematical constant upto the specified Decimal digits.
# The input to the Program is number of decimal digits specified by the user.
#author@Pratik Narode(pratiknarode143@gmail.com)

pi=list()
def gen(n):
## KN while naming variables use descriptive names instead of letters, makes it easier to follow the code.
## for e.g. 'quotient' instead of q, 'divisor' instead of d, 'counter' instead of c
    q=22
    d=7
    i=1
    flag=0
    while i<n:
        if q/d!=0:
            r=q%d
            pi.append(q/d)
        else:
            if flag==0:
                flag=i
                i=0
            r=(q*10)%d
            pi.append((q*10)/d)
        i+=1
        q=r
    vpi=""
    for i in range(len(pi)):
        if i+1==flag:
            vpi=vpi+"."+str(pi[i])
        else:
            vpi=vpi+str(pi[i])
    print vpi
    return



if __name__=="__main__":
    print "The Limit for decimal digits of PI"
    n=int(raw_input())
    gen(n)

    
