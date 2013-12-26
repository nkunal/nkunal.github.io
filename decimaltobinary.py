#Program to convert a given Decimal no. into its equivalent Binary Sequence.
# It also convert a given Binary no. back into Decimal No.
#author@Pratik Narode(pratiknarode143@gmail.com)


def bintodec(n):
    bn=list()
    while n>0:
        bn.append(n%2)
        n=n/2
    bno=""
    for i in range(len(bn)):
        bno+=str(bn.pop())
    print "The Binary sequence is ",bno
    return

def dectobin(n):
    dno=0
    i=0
    while n>0:
        dno+=(n%10)*(2**i)
        i+=1
        n=n/10
    print "The Decimal No is ",dno
    return

if __name__=="__main__":
    print "Enter the Decimal No:"
    no=int(raw_input())
    bintodec(no)
    print "Enter the Binary No:"
    no=int(raw_input())
    dectobin(no)    
        
