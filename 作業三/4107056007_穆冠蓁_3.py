#99_expansion
import random

class Ninety_nine:
    """NOTE: YOU SHOULD ONLY ADD YOUR CODE IN THIS SCOPE"""
    class Card:
        def __init__(self, color, number):
            self.color = color      # color = "R" or "B"
            self.number = number    # number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        def __repr__(self):
            return self.color+self.number   # RA, B8, R10, etc.

    pokers = []
    hands = []
    discards = []
    sea = 30        # 99 to win

    def __init__(self):
        numberList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # For simpler design, we only use RED and BLACK to seperate the card.
        for c in ["R", "R", "B", "B"]:
            for n in numberList:
                self.discards.append(self.Card(c, n))
        # The list discards will be a list of 26 red Cards and 26 black Cards

        self.shuffle()  # Check the function shuffle. 
        """TODO: FINISH THE LOGIC HERE.
        You need to let the player draw 5 cards, and let the game start."""
        self.draw(5)
        self.start()
        #print(self.hands)
            

    def shuffle(self):
        # This function will return discards to pokers and shuffle
        self.pokers = self.discards[:]
        random.shuffle(self.pokers)
        self.discards.clear()

    def draw(self, count):
        # count indicates how many cards do you want to draw
        for _ in range(count):
            if len(self.pokers) == 0:
                # return discards to pokers and shuffle
                self.shuffle()
            # draw 1 no matter shuffled or not
            self.hands.append(self.pokers.pop(0))

    def handSize(self):
        return len(self.hands)

    def play(self, idx):
        playCard = self.hands.pop(idx)
        number = 0
        if playCard.number == "A":
            number = 1
            for i in self.hands:
                self.discards.append(i)
            count = len(self.hands)
            self.hands.clear()
            self.draw(count)
            
        elif playCard.number == "J":
            number = 11
            for i in self.hands:
                self.discards.append(i)
            self.hands.clear()
            self.draw(5)
            
        elif playCard.number == "Q":
            if playCard.color == "R":
                self.sea += 20
            else :
                self.sea -= 20
            self.discards.append(playCard)
            self.draw(1)
        elif playCard.number == "K":
            self.discards.append(playCard)
            self.draw(2)
            
        else:
            number = int(playCard.number)
            if playCard.color == "R":
                self.sea += int(number)
            else :
                self.sea -= int(number)
            self.discards.append(playCard)
            self.draw(1)
        """
        TODO: FINISH THE LOGIC HERE
        playCard is the card played. It's a card object. Thus, it has the attributes color and number.
        playCard.number will belong to the set {"A","2","3",...,"K"}
        playCard.color will be "R" or "B"
        There are three things to do:
            1. The effect of the card need to be calculate. (For example: you played card R7, the sea should be added with 7)
            2. playCard need to be discarded.
            3. Draw 1 card.
        """

    def start(self):
        while self.sea > 0 and self.sea < 99:
            print("sea:", self.sea)
            print("your hands", self.hands)
            idx = int(input("Enter the number of the card you want to play. 0 for the far left one. "))
            if idx not in range(self.handSize()):
                print("Wrong number.")
            else:
                self.play(idx)
        print("sea:", self.sea)
        if self.sea != 99:
            print("You lose!")
        else:
            print("You win!")

if __name__ == "__main__":
    """NOTE: YOU SHOULD NOT MODIFY ANYTHING HERE."""
    game = Ninety_nine()