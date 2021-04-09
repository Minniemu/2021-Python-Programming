import random

class C_guess():
    def __init__(self, digit = 4):
        self.digit = digit
        self.password = random.sample([str(i) for i in range(10)], digit)
        self.step = 0

    def play(self):
        correct = False
        while not correct:
            inp = input("input a {}-digit number: ".format(self.digit))

            if not self.checkValid(inp):    # 輸入不合法
                continue    # 回到while-loop的開始，重新輸入

            correct = self.guess(inp)       # 猜inp，如果猜到correct會變True，否則False
        print("答對了！")
        print("你總共猜了{}次。".format(self.step))

    def checkValid(self, inp):
        if not str.isdigit(inp):        # 所有字元都是數字
            print("輸入不全為數字")
            return False
        elif not len(inp) == self.digit:
            print("輸入不為{}位數".format(self.digit))
            return False
        else:
            return True                 # 輸入合法

    def guess(self, inp):
        self.step += 1
        a = b = 0
        for i in range(self.digit):
            if self.password[i] == inp[i]:   # 位置相同、數字也相同
                a += 1
            elif self.password[i] in inp:    # 位置不相同(elif)，數字在裡面
                b += 1
        print("第{}回合，{}A{}B".format(self.step, a, b))

        return True if a == self.digit else False

if __name__ == "__main__":
    game = C_guess()
    game.play()