from datetime import datetime as dt
car = []
car_num = []
while True:
    inp = input("input car number (Q or q for quit):")
    if inp=="q" or inp == "Q":
        print("System terminated.")
        break
    else :
        index = 0
        if inp not in car_num:
            dict1 ={}
            car_num.append(inp)
            dict1['car_number'] = inp
            dict1['Enter time'] = dt.now()
            dict1['enter_num'] = 1
            car.append(dict1)
        #index = car_num.index(inp)
        elif (car[car_num.index(inp)]['enter_num'] %2 == 1):
            index = car_num.index(inp)
            car[index]['Leave time'] = dt.now()
            t = car[index]['Leave time'] - car[index]['Enter time']
            car[index]['Stay time'] = round(t.total_seconds(),1)
            car[index]['enter_num'] += 1
            print("Enter time:"+str(car[index]['Enter time']))
            print("Leave time:"+str(car[index]['Leave time']))
            print("Stay time:"+str(car[index]['Stay time'])+"seconds")
        else :
            index = car_num.index(inp)
            car[index]['Enter time'] = dt.now()
            car[index]['enter_num'] += 1
            







