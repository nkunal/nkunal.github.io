#Program to count no. of words in the given text file.
#author@Pratik Narode(pratiknarode143@gmail.com)


import re

def countword():
    filename="sample.txt"
    words=re.split("\w+",file(filename).read().lower())
    print "No of words in the file are:",len(words)
    return

if __name__=="__main__":
    countword()
    
