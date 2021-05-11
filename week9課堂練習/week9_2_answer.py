import week9_1_answer as tic
import week8_ans as guess

class playGround:
    def __init__(self):
        self.game1 = tic.C_TicTacToe()
        self.game2 = guess.C_guess()
        print("歡迎來到遊樂場。")
        self.start()
    
    def start(self):
        while True:
            x = input("1為井字遊戲、2為猜數字、輸入-1離開遊樂場：")
            if x == "-1":
                return
            elif x == "1":
                self.game1.start()
                self.resetGames()
            elif x == "2":
                self.game2.play()
                self.resetGames()
            else:
                print("輸入不合法。")
    
    def resetGames(self):
        """最好的作法還是各個遊戲各自處理重置，而不是這樣直接呼叫新的物件。不過為方便起見這樣設定。"""
        self.game1 = tic.C_TicTacToe()
        self.game2 = guess.C_guess()

if __name__ == "__main__":
    PG = playGround()