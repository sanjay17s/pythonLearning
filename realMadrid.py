class club:
    '''a class representing different football clubs in the world'''
    def __init__(self,name,league):
        self.name = name
        self.league = league
        self.sport = 'football'
        self.manager = 'default'

    def description(self):
        print(f"{self.name.title()} plays {self.sport} in {self.league}")


class madrid(club):

    def __init__(self, name, league):
        super().__init__(name, league)
        

    def managerInfo(self):
        print(f"{self.manager} is the manager")


realMardid = madrid('real','la liga')
realMardid.manager = 'carlo ancelotti'
realMardid.managerInfo()
