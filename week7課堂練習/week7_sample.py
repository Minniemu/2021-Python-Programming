import random
# 請勿修改除了標有TODO以外的任何程式碼，並讓這份程式能夠正確執行。

class C_guess():
    def __init__(self, digit = 4):
        # 請勿修改除了標有TODO以外的任何程式碼，並讓這份程式能夠正確執行。
        self.digit = digit
        self.password = random.sample([str(i) for i in range(10)], digit)
        self.step = 0

    def play(self):
        # 請勿修改除了標有TODO以外的任何程式碼，並讓這份程式能夠正確執行。
        correct = False
        while not correct:
            inp = input("input a {}-digit number: ".format(self.digit))

            if not self.checkValid(inp):    # 輸入不合法
                continue    # 回到while-loop的開始，重新輸入

            correct = self.guess(inp)       # 猜inp，如果猜到correct會變True，否則False
        print("答對了！")
        print("你總共猜了{}次。".format(self.step))

    def checkValid(self, inp):
        # TODO: Finish the logic here.
        # 假如inp不全是數字或inp的長度不符，印出error message並return False表示不合法
        # 否則return True表示合法
        return False

    def guess(self, inp):
        # TODO: Finish the logic here.
        # inp已經確定合法，判斷inp是幾A幾B並印出玩家回合數及猜的是幾A幾B
        # 假如A的數量等於self.digit，則return True代表猜對了
        # 否則return False代表猜錯了
        return False

if __name__ == "__main__":
    # 請勿修改除了標有TODO以外的任何程式碼，並讓這份程式能夠正確執行。
    game = C_guess()
    game.play()

    