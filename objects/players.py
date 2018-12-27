# A module to define a player
import random as rd
from functools import partial
from objects.Menu import Menu

class Player:
    """A player in the game
    """

    def __init__(self, name, primary_leader=None, secondary_leader=None):
        self.name = name
        self.primary_leader = primary_leader
        self.secondary_leader = secondary_leader
        self.risk_territories = []
        self.monopoly_properties = []
        self.money = 1500
        self.mon_position = 0
        self.in_jail = False
        self.turns_in_jail = 0
        self.roll = 0
        self.decision = None
        self.reinforcement_order = []
        self.attack_order = []
        self.surge_order = []
        self.fortify_order = []

    def reinforce_order(self, type):
        self.order_reset()
        done = False
        while not done:
            if take_input(yes/no, "turn in cards?"):
                self.turn_in_cards()
            # Placeholder for the gui
            country = take_input(country)
            number = take_input(how_many)
            if valid_reinf(country, number):
                self.reinforcement_order.append((country, number))
            else:
                print("not a legal reinforcement")
            done = take_input(yes/no)
        for order in self.reinforcement_order:
            if self.both_utilities():
                self.money -= order[2] * 75
            else:
                self.money -= order[2] * 100

    def attack_order(self):
        self.order_reset()
        done = False
        while not done:
            # Placeholder for the gui
            attacking_country = take_input(country)
            defending_country = take_input(country)
            number = take_input(how_many)
            if valid_attack(attacking_country, defending_country, number):
                self.attack_order.append((attacking_country, defending_country, number))
            else:
                print("not a legal attack")
            done = take_input(yes/no)
        done = False
        while not done:
            if take_input(yes/no, "would you like to surge?"):
                # Placeholder for the gui
                attacking_country = take_input(country)
                defending_country = take_input(country)
                number = take_input(how_many)
                if valid_attack((attacking_country, defending_country, number)):
                    self.surge_order.append((attacking_country, defending_country, number))
                    done = True
                else:
                    print("not a legal attack")
            else:
                done = True

    def fortify_order(self):
        self.order_reset()
        done = False
        while not done:
            # Placeholder for the gui
            from_country = take_input(country)
            to_country = take_input(country)
            number = take_input(how_many)
            if valid_fortify(attacking_country, defending_country, number):
                self.fortify_order.append((attacking_country, defending_country, number))
            else:
                print("not a legal fortification")
            done = True








    def buy_property(self, property):
        # the player purchases a property
        pass

    def mon_turn(self, mon_board, num_doubles=0):
        self.pre_phase(mon_board)
        self.roll_phase(mon_board)

    def set_roll(self, roll):
        self.roll = roll

    def set_decision(self, decision):
        self.decision = decision








    def pre_phase(self, mon_board):
        while self.decision != "Roll Dice":
            pre_phase_menu = Menu(["Roll Dice", "Buy House", "Turn in Cards"], [partial(self.set_decision, "Roll Dice"),
                               partial(self.set_decision, "Buy House"), partial(self.set_decision, "Turn in Cards")])
            pre_phase_menu.menu()
            if self.decision == "Buy House":


            if self.decision == "Turn in Cards":

        self.decision = None




    def roll_phase(self, mon_board)sd
        doubles = False
        doubles_count = 0
        turn_over = False
        while not turn_over:
            roll = roll_dice(2)
            if roll[1] == roll[2]:
                doubles = True
                doubles_count += 1
                if doubles_count == 3:
                    self.go_to_jail
                    break
            mon_board.process_move(self, roll[1] + roll[2])
            if not doubles:
                turn_over = True






        self.mon_position = (self.mon_position + move) % len(mon_board.board)
        mon_board.eval_position(self.mon_position)

    def buy_houses(self):
        prop_names = []
        buy_commands = []
        for prop in self.monopoly_properties:
            if can_buy_house(prop, self):
                prop_names.append(prop.name)
                buy_commands.append(partial(put_house(prop, self)))






