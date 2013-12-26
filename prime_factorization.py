# Program to carry out the Prime Factorization Process.
# It takes an integer no as the Input and find the Prime factor of the given No.
#author@Pratik Narode(pratiknarode143@gmail.com)

a=list()
factor=list()
def prime():
    for i in range(2,50):
        flag=0
        for j in range(2,(i/2)+1):
            if i%j==0:
                flag=1
                break
        if flag==0:
            a.append(i)
    return

def primefactor(n):
    while n!=1:
        for i in range(len(a)):
            if n%a[i]==0:
                factor.append(a[i])
                n=n/a[i]
                break
    fac=""
    for i in range(len(factor)-1):
        fac+=str(factor[i])+"x"
    i+=1
    fac+=str(factor[i])
    print "The Prime Factors are:",fac
    return

if __name__=="__main__":
    prime()
    print "Enter the No to Prime Factorize:"
    n=int(raw_input())
    primefactor(n)

