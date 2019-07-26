'''Pattern Printing:
Ravi and Raju are best friends. Ravi given a string to Raju and print in the following format.
Please help him to print in the following format.
String : IARE
E E E E E E E
E R R R R R E
E R A A A R E
E R A I A R E
E R A A A R E
E R R R R R E
E E E E E E E
Here, IARE string length is 4.
Input format:
A string
Output format:
The above specified pattern
Sample Input:
abc
Sample Output:
c c c c c
c b b b c
c b a b c
c b b b c
c c c c c
'''

t=input()
l=[i for i in t]#converting string to list
k=len(t)
p=[]
ti=[]
s=0
count=2
pj=1
for j in range(0,2*k-1):  # for printing last char in string 2*len(string)-1 times
    print(l[k-1],end=" ")
    p.append(l[k-1])
print()
while(count<=k):    # for printing string elements ti
    g=[]
    for i in range(len(p)):
        if(i>s and i<len(p)-pj):
            p[i]=l[k-(count)]
    for i in p:
        print(i,end=" ")
        g.append(i)
    ti.append(g)  #append printing elemnts for mirror purpose
    s=s+1
    count=count+1
    pj=pj+1
    print()
i=len(ti)-2
while(i>=0):
    for r in range(len(p)):  #printing the mirror part
        print(ti[i][r],end=' ')
    print()
    i=i-1
for j in range(0,2*k-1):#printing the first statemnt again
    print(l[k-1],end=" ")


