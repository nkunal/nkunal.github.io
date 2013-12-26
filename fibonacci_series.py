# Program to find the Fibonacci Sequence with the length of series equal to that specified by the user.
# The input to the Program is the limit of the Sequence.
#author@Pratik Narode(pratiknarode143@gmail.com)


def fib(a,b,n):
    if n!=0:
        print a
        fib(a+b,a,n-1)
    return 0


if __name__=="__main__":
    print "Enter the Limit for Sequence:"
    n=int(raw_input())
    fib(1,1,n)



        
        
        
    
