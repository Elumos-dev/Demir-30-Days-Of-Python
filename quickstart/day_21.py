# Day 21: classes and objects


class Player:
    team = 'Free agent'                    # class default, shared by every object

    def __init__(self, name, goals=0):     # runs once when you create an object
        self.name = name                   # self = the object being built
        self.goals = goals
        self.log = []

    def score(self, n=1):                  # method = function that lives in the class
        self.goals += n
        self.log.append(n)

    def info(self):
        return f'{self.name}: {self.goals} goals ({self.team})'


class Keeper(Player):                      # inheritance: Keeper gets everything Player has
    def __init__(self, name, saves=0):
        super().__init__(name)             # run the parent's __init__ first
        self.saves = saves

    def info(self):                        # override: same name replaces the parent's version
        return super().info() + f', {self.saves} saves'


p = Player('Sam')                          # create an object
p.score(2)
p.score()
p.team = 'City FC'                         # change a default for this object only
print(p.info(), p.log)
print(Keeper('Lee', saves=5).info())
