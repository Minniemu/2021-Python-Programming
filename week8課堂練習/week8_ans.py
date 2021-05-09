import random

class C_guess():
    def __init__(self):
        self.passwordList = []
        for i in reversed(range(1,10000)):          # 從後往前刪，避免index偏移
            drop = False
            pw = '{0:04d}'.format(i)                # 補成四位數，原本內容靠右，其餘用0填滿(如：1 -> 0001)
            for j in range(len(pw)-1):
                if pw[j] in pw[j+1:]:               # 四位數ABCD，A看BCD有沒有一樣的，B只要看CD，C只要看D，有一樣的話這個密碼就不要了
                    drop = True
                    break
            if not drop:
                self.passwordList.append(pw)
        # print(self.passwordList)
        self.lastGuess = ""
        self.step = 0

    def AIGuess(self):
        self.step += 1
        self.lastGuess = random.choice(self.passwordList)       # 要猜的數字，這裡的選擇是備選清單中隨機猜一個
        return self.lastGuess
    
    def AIThink(self, A, B):
        # print("上個猜", self.lastGuess)
        for i in reversed(range(0, len(self.passwordList))):    # 從後往前刪，避免index偏移
            thinkPw = self.passwordList[i]
            thinkA = thinkB = 0

            for j in range(len(thinkPw)):
                if thinkPw[j] == self.lastGuess[j]:     # 位置相同、數字也相同
                    thinkA += 1
                elif thinkPw[j] in self.lastGuess:      # 位置不相同(elif)，數字在裡面
                    thinkB += 1
            if thinkA != A or thinkB != B:
                self.passwordList.pop(i)                # A B數不相同的移除可能性

        # print(self.passwordList)
        # print("剩：", len(self.passwordList), "個")

        if self.passwordList:               # 備選清單是不是空的
            return True
        else:                               # 是空的話，要告訴play函式
            return False

    def play(self):
        correct = False
        while not correct:
            inp = self.AIGuess()
            print("AI猜", inp)
            a, b = input("請告訴他是幾A幾B(用空格分開)：").split()
            if a == "4":
                correct = True
            elif not self.AIThink(int(a), int(b)):
                print("你把AI考倒了，他不覺得有這種數字存在。")
                return

        print("答對了！")
        print("你總共猜了{}次。".format(self.step))

if __name__ == "__main__":
    game = C_guess()
    game.play()