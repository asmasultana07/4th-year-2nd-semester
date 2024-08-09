import sys
from collections import defaultdict, deque

f = open("input.txt", "r")
exp = f.readline().rstrip().split(" ")

#operator

op = {'^':0,'*': 1,'/': 1,'%': 1,'+': 2,'-': 2}
stack = []
tac = deque() 

counter = 1

#bracket
for c in exp:
    if c==")":
        temp = []
        while stack and stack[-1] != "(": 
            temp.append(stack.pop())
        if stack[-1]=='(':
            stack.pop()
        tac.append((counter, temp[::-1]))
        stack.append("t"+str(tac[counter-1][0]))
        counter+=1
    else:
        stack.append(c)
tac.append((counter, stack))

result = deque()

counter = 1
t = defaultdict(int)
while tac:
    current = tac.popleft()
    index = current[0]
    current = current[1]
    
    #update t
    for i in range(len(current)):
        if current[i][0]=='t':
            current[i] = 't'+str(t[int(current[i][1])])

    
    while len(current)>2:
        #sqrt
        for i in range(len(current)):
            if current[i]=='sqrt':
                result.append(("t"+str(counter),"sqrt("+current[i+1]+")"))
                current = current[:i]+["t"+str(counter)]+current[i+2:]
                counter+=1
                break
        
        # ^
        for i in range(len(current)):
            if current[i]=='^':
                temp = "*".join([current[i-1] for j in range(int(current[i+1]))])
                temp = deque(temp)
                while len(temp)>2:
                    for j in range(len(temp)):
                        if temp[j]=='*':
                            result.append(("t"+str(counter), temp[j-1]+"*"+temp[j+1]))
                            temp.popleft()
                            temp.popleft()
                            temp.popleft()
                            temp.appendleft("t"+str(counter))
                            counter+=1
                            break
                current = [result[-1][0]]+current[i+2:]
                break
        
        # *
        flag = False
        for i in range(len(current)):
            if current[i]=='*' or current[i]=='/' or current[i]=='%':
                result.append(("t"+str(counter),current[i-1]+current[i]+current[i+1]))
                current = current[:i-1]+["t"+str(counter)]+current[i+2:]
                counter+=1
                flag = True
                break
        if flag:
            continue
        
        # + -
        for i in range(len(current)):
            if current[i]=='+' or current[i]=='-':
                if current[i]=='-' and i==0:
                    result.append(("t"+str(counter),'0'+current[i]+current[i+1]))
                    current = ["t"+str(counter)]+current[i+2:]
                else:
                    result.append(("t"+str(counter),current[i-1]+current[i]+current[i+1]))
                    current = current[:i-1]+["t"+str(counter)]+current[i+2:]
                counter+=1
                break
        
        # =
        for i in range(len(current)):
            if current[i]=='=':
                result.append((current[i-1],current[i+1]))
                current = current[:i-1]+["t"+str(counter)]+current[i+2:]
                counter+=1
                break
    
    t[index] = len(result)

for item in result:
    print(f"{item[0]} := {item[1]}")