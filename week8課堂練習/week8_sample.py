import random

class C_guess():
    def __init__(self):
        """TODO: 初始化下面這個密碼清單"""
        self.passwordList = []

        self.lastGuess = ""     # 記錄AI上一個猜的數字，可有可無。如果沒有的話，AIThink需要多傳一個參數進去。
        self.step = 0           # 記錄AI猜了幾次

    def AIGuess(self):
        """TODO: AI選擇一個隨機的密碼，假如你有lastGuess變數，需要同時在這把猜的密碼存進去"""
        return "0000"
    
    def AIThink(self, A, B):
        """
        TODO:
        AI把剛剛猜完的密碼對自己的密碼清單進行思考，哪些不可能是密碼。
        假如密碼清單被清空了，導致AI猜不出來，return False告訴主程式
        """
        return False

    def play(self):
        correct = False
        while not correct:
            inp = self.AIGuess()
            print("AI猜", inp)
            a, b = input("請告訴他是幾A幾B(用空格分開)：").split()
            if a == "4":                                # 假如猜對了就不用思考了，否則就會思考，所以是if-elif
                correct = True
            elif not self.AIThink(int(a), int(b)):      # 假如思考之後發現答案不存在
                print("你把AI考倒了，他不覺得有這種數字存在。")
                return

        print("答對了！")
        print("AI總共猜了{}次。".format(self.step))

if __name__ == "__main__":
    game = C_guess()
    game.play()