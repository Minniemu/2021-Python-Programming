#HW1 Monopoly(大富翁)
#!/usr/bin/env python
# coding: utf-8
import random

monoplyMap = [200, -200, 10000, -600, -2000, -3000, 0, 1000, 3000, -400]
monoplyStr = ["中發票+200元", "闖紅燈-200元", "中樂透+10000元", "紅線停車-600元", "繳汽車稅-2000元", "繳房屋稅-3000元", "停止一次", "得到股息+1000元", "工作得到獎金+3000元", "繳停車費-400元"]
#class monopoly to record the item of every single player
class Monopoly:
    def __init__(self, property, steps, name): #initialize
        self.property = property
        self.steps = steps
        self.name = name
        self.go = True
        #self.position = 0
        #print("Property = ",property)
        #print("Steps = ",steps)
        #print("Name = ",name)
    
    def step(self,s):  #count steps
        print("{0} move {1} steps".format(self.name,s))
        self.steps += s
            
        if self.steps > 9:
            print("繞行一周,得到特別獎金5000元")
            self.property += 5000
            self.steps = self.steps%9 - 1
        if self.steps == 6:
            self.go = False
        self.result()
        
    def result(self): #print out the result of every round
        self.property += monoplyMap[self.steps]
        print(monoplyStr[self.steps])
        print("=========={}==========".format(self.name))
        print("money : ",str(self.property))
        print("position : ",str(self.steps))
        print("\n")
    
    def stop(self): #print out message while user stop in this round
        print("=========={}==========".format(self.name))
        print("money : ",str(self.property))
        print("position : ",str(self.steps))
        print("\n")
#Input 
n = input("Please input numbers of players = ")
n = int(n)
objs = [Monopoly(10000,0,'Player ' + str(i+1)) for i in range(n)] #create list of object
count = 0    #count the number of round
while True:
    num = input("(0 for exit)")
    if num == '0':
        break
    obj_num = count%n
    #print("==========Player{}==========".format(obj_num+1))
    if objs[obj_num].go == False:
        print("{}本回合禁止移動".format(objs[obj_num].name))
        objs[obj_num].go = True
        objs[obj_num].stop()
    else:
        rand = random.randint(1,6)
        objs[obj_num].step(rand)
    count += 1 #plus the round number every time
#End of the game
money = {}
winner = []
for i in range(n):
    m = objs[i].property
    n = objs[i].name
    money[n] = m
#print(money)
#find winner
all_values = money.values()
max_value = max(all_values)
#print("max_values = ",max_value)
for key,value in money.items():
    if value == max_value:
        winner.append(key)
listToStr = ' '.join([str(elem) for elem in winner])
print("{} win!".format(listToStr))
        
#HW2 Reorganize Words 
def standardize(s):
    s = s.lower()
    s = sorted(s)
    return "".join(s)
list_A = []
dict_D = {}
B = []
while True:
    n = input("Please enter a word. (0 for exit):")
    if n == '0':
        break
    list_A.append(n)
    std_str = standardize(n)
    if std_str not in dict_D:
        dict_D[std_str] = 1
    else:
        dict_D[std_str] += 1
#print(dict_D)
for w in list_A:
    if dict_D[standardize(w)] == 1:
        B.append(w)
print("Output = ",B)