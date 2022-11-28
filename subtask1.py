# 7.3 
# Also I did a check of input DATA.
n=-1
while n<0:
    print("Please entere the correct number (n>=0) ")
    try:
        n=int(input())
    except:
        print("There is no number")
        n=-1
i=1
while i*i<=n:
    i+=1

print((i-1)**2)
#it looks like I learned how to use
# git today',