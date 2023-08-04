import random


class coin:
    def __init__(self, sideup="Head"):
        self.sideup = sideup

    def toss(self):
        if random.randint(0,1)==0:
            self.sideup = "Tail"
        else:
            self.sideup = "Head"


    def get_sideup(self):
        return self.sideup


coin1 = coin()
coin1.toss()
print(coin1.get_sideup())
