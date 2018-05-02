# A module to define a player

class Player:
    """A player in the game
    """

    def __init__(self, name, primary_leader="", secondary_leader=""):
        self.name = name
        self.primary_leader = primary_leader
        self.secondary_leader = secondary_leader
        self.risk_territories = []
        self.monopoly_properties = []
        self.money = 0

    def buy_troop(self, number):
        # the player purchases a troop
        pass

    def buy_property(self, property):
        # the player purchases a property
        pass
