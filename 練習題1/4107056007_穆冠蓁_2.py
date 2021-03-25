testTakers = frozenset({"蘇俞方", "杜政宏", "黃怡君", "沈昱廷" ,"羅軒豪", "白俊瑋", "陳玉定", "張碧新", "陳信秀", "孫思妤"})
subset = set()
for i in testTakers:
    subset.add(i)
length = len(testTakers)
available = 0
while True:
    c = input("Who's comming?(end or END for quit:)")
    if c == "end" or c =="END":
        print("======考試結束======")
        print("應到人數:"+str(length)+"人")
        print("實到人數:"+str(available)+"人")
        print("未到人數:"+str(length-available)+"人")
        print("未到名單:")
        for i in subset:
            print(i)
        break
    elif c in testTakers:
        print("歡迎進場，"+str(c))
        subset.remove(c)
        available += 1
    else :
        print(str(c)+" 不在應試名單中，請離場")

