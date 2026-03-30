a = input ("please enter your word")
c = input ("please enter your character")
i = 0 
count = 0
while (i< len(a)):
    if (a[i]==c):
        count = count + 1 
    i = i + 1
print (count)