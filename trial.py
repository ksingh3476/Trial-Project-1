
##from pathlib import Path
##
##        
##
##
##
##
##            
##def count(path:str):
##    IF = []
##    text = path.open('r')
##    content = text.readlines()
##    for item in content:
##        split_content = item.split()
##        num = len(split_content)
##        IF.append(num)
##    return IF
##p = Path('C:\\Users\\tan\\Desktop\\ICS32\\test1.txt')
##print(count(p))



def increment_all(x:list):
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] +=1
    return x

def increment_diagonal(x:list):
    for i in range(len(x)):
        print(i)
        x[i][(len(x)-(i+1))] += 1
    return x


#hello    
a = [[1, 2,3],
     [3, 4,3],
     [5, 6,3]]


print(increment_diagonal(a))  
