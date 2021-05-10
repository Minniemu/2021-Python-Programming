import random
import time

class C_TicTacToe:
    def __init__(self):
        self.board = [i for i in range(9)]
        self.botPlayer = random.sample([1, 2], k = 1)  # k是電腦玩家的數量，0或1或2
        self.placedChess = 0
    
    def print_board(self):
        print("=====================")
        for i in range(3):
            print("{}\t{}\t{}".format(self.board[i*3 + 0], self.board[i*3 + 1], self.board[i*3 + 2]))

    def isValid(self, x):
        x = str(x)
        if not str.isdigit(x):
            return False
        x = int(x)
        if x > 8 or x < 0:
            return False
        if self.board[x] == "O" or self.board[x] == "X":
            return False
        return True

    def play(self, nowPlayer, x):
        self.board[x] = "O" if nowPlayer == 1 else "X"
        self.placedChess += 1

    def isWinning(self, x):
        possible = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]     # 可能連線的組合
        for tp in possible:
            first = self.board[tp[0]]
            second = self.board[tp[1]]
            third = self.board[tp[2]]
            if first == second == third != "_":
                return True
        return False
    
    def AIThink(self, nowPlayer):
        print("AI在思考中...")
        time.sleep(1 + random.random())
        # 列出可能聽牌的組合
        possible = [(0,1), (0,2), (1,2), (3,4), (3,5), (4,5), (6,7), (7,8), (6,8),      # 橫的聽牌
                    (0,3), (0,6), (3,6), (1,4), (1,7), (4,7), (2,5), (2,8), (5,8),      # 直的聽牌
                    (0,4), (0,8), (4,8), (2,4), (2,6), (4,6),                           # 斜的聽牌
                   ]
        # 聽牌缺的那一個格子是哪格
        less = [2, 1, 0, 5, 4, 3, 8, 6, 7,
                6, 3, 0, 7, 4, 1, 8, 5, 2,
                8, 4, 0, 6, 4, 2,]

        chess = "O" if nowPlayer == 1 else "X"
        # 假如能贏，直接選擇能取得勝利的格子
        for i in range(len(possible)):
            tp = possible[i]
            tg = less[i]
            first = self.board[tp[0]]
            second = self.board[tp[1]]
            if first == second == chess:
                if self.isValid(tg):
                    return tg
        
        # 玩家符合聽牌，阻擋玩家勝利
        for i in range(len(possible)):
            tp = possible[i]
            tg = less[i]
            first = self.board[tp[0]]
            second = self.board[tp[1]]
            if first == second:
                if self.isValid(tg):
                    return tg
        
        # 否則讓想辦法讓自己聽牌，因為possible的順序所以會讓斜的優先
        for i in range(len(possible)):
            tp = possible[i]
            tg = less[i]
            first = self.board[tp[0]]
            second = self.board[tp[1]]
            if first == chess and self.isValid(tg):
                if self.isValid(tp[1]):
                    return tp[1]
            elif second == chess and self.isValid(tg):
                if self.isValid(tp[0]):
                    return tp[0]

        # 否則以中間>角>邊的順序下子
        for i in [4,0,2,6,8,1,3,5,7,]:
            if self.isValid(i):
                return i

    def start(self):
        self.print_board()

        nowPlayer = 1
        while self.placedChess < 9:
            x = -1
            if nowPlayer in self.botPlayer:
                x = str(self.AIThink(nowPlayer))
                print("AI輸入：", x)
            else:
                x = input("請輸入要下子的座標：")
            if self.isValid(x):
                x = int(x)
                self.play(nowPlayer, x)
                self.print_board()
                if self.isWinning(x):
                    print("Player", nowPlayer, "win!")
                    return
                nowPlayer = 2 if nowPlayer == 1 else 1
            else:
                print("輸入不合法。")
        print("雙方平手")

if __name__ == "__main__":
    game = C_TicTacToe()
    game.start()