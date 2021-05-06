class TeamAssembleSystem():
    def __init__(self, game):
        self.game = game

    def start(self):
        while True:
            print("目前在小隊內的成員為：", self.game.teamList)
            print("輸入1以查詢小隊內成員的詳細資料。")
            print("輸入2以將隊員移出小隊。")
            print("輸入3以將冒險團的成員加入小隊。")
            print("輸入4以計算你小隊的總戰力。")
            print("輸入-1退出")
            n = input()
            if n == "-1":
                break
            elif n == "1":
                self.query()
            elif n == "2":
                self.remove()
            elif n == "3":
                self.join()
            elif n == "4":
                self.analysis()
            else:
                print("輸入不正確，請重新輸入")
    
    def query(self):
        """TODO: Finish the logic here.
        查詢小隊內成員的詳細資料。"""
        pass
    
    def remove(self):
        """TODO: Finish the logic here.
        將隊員移出小隊。"""
        pass
    
    def join(self):
        """TODO: Finish the logic here.
        將冒險團的成員加入小隊。"""
        pass

    def analysis(self):
        """計算小隊的總戰力。"""
        hp = 0
        attack = 0
        defense = 0
        for m in self.game.teamList:
            hp += m["hp"]
            attack += m["attack"]
            defense += m["defense"]

        print("====================\nhp: {}\nattack: {}\ndefense: {}\n====================".format(hp, attack, defense))