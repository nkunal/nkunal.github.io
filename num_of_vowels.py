#Program to count no. of vowels into the given sentence.
#author@Pratik Narode(pratiknarode143@gmail.com)

vowel=('a','e','i','o','u')
no={'a':0,'e':0,'i':0,'o':0,'u':0}
def count(string):
    cv=0
    for letter in string:
        if letter in vowel:
            cv=cv+1
            no[letter]=no[letter]+1
    print "The No of Vowels in the String is:",cv
    print no.keys()
    print no.values()
    return

if __name__=="__main__":
    print "Enter the String:"
    string=raw_input().lower()
    count(string)
    
    
    
