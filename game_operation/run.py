import random as r

class GameLoop:

    def __init__(self, players, mon_board, risk_board):
        self.players = r.sample(players)
        self.dead_players = []
        self.mon_board = mon_board
        self.risk_board = risk_board

    def play(self):
        while not game_over(self.players):
            # self.game_board.display()
            # print("{}'s move: ".format(self.active_player.shape))
            self.mon_phase(self.players, self.mon_board, self.risk_board)
            self.risk_phase(self.players, self.risk_board)
        self.print_end_game()

    def mon_phase(self, players, mon_board, risk_board):
        for i in range(3):
            for player in players:
                player.mon_turn(mon_board, risk_board)

    def risk_phase(self, players, risk_board):
        for player in players:
            player.reinforce_order(risk_board)
        self.reinforce(players)
        for player in players:
            player.attack_orders(risk_board)
        self.attack(players)
        for player in players:
            player.fortify_orders(risk_board)
        self.fortify(players)

    def print_end_game(self):
        print("game over, {}'s won.".format(self.players[0]))




class Game:

    # This class holds the entire game process. It deals with the decks of cards, the players of the game,
    # and the phases of the turns that players take. All it needs as an input is a number of players
    # (in the form of a string). In the init function you will find lists containing the monsters, buildings,
    # and spells for the game.

    def __init__(self, players, chance, com_chest):
        """

        :param number: The number of players
        """










