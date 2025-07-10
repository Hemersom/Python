import math
import os

i = 2
primo = True
while(True):
    i+=1
    primo = True
    for j in range(2,int(math.sqrt(i))+1):
        if(i % j == 0):
            primo = False
            break
            
    if(primo == True):
        print(f'|{i}|-')
        os.system("pause")
        os.system("cls")