n=input("Input a number to be checked")
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count>2):
    print("Composite Number")
else:
    print("Not Composite Number")
#changes in branch 2