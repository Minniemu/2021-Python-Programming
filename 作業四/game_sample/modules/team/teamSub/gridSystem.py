class GridSystem():
    def __init__(self, game):
        self.game = game
    
    def start(self):
        while True:
            print("冒險團目前擁有的成員有：", self.game.characterList)
            print("請輸入成員的編號(最左邊為0)，輸入-1退出")
            idx = input()
            if idx == "-1":
                break
            elif idx.isdigit():
                """TODO: Finish the logic here.
                查詢冒險團中對應index成員的詳細資料。"""
            else:
                print("輸入不為整數，請重新輸入")