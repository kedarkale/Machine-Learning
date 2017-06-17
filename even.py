import numpy as np

a=[]

a=np.random.randint(1,100,10)

print("full list : ",end=' ')
for j in a:
    print(j,end=' ')
print('')    

def even (list):
    print("even list : ",end=' ')
    for i in list:
        if (i%2==0):
            print(i,end=' ')
    return 
    
even (a)   