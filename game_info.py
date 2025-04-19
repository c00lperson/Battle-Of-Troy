import random

class GameStats:
    def __init__(self):
        start_val = 50

        # Player and army stats start at 100
        self.player = {'HEALTH' : start_val,
                  'STRENGTH' : start_val,
                  'ARMOR' : start_val,}

        self.army = {'WARRIORS' : start_val,
                     'MORALE' : start_val,
                     'RESOURCES' : start_val}

        self.armor = {'HELMET' : False,
                      'BREASTPLATE' : False,
                      'SHIELD' : False}

        self.weapons = {'SPEAR' : False,
                        'SWORD' : False,
                        'BOW' : False}

        # Default luck is 50%, no gods in favor at game start
        self.hidden = {'luck' : 0.5,
                       'Hera' : False,
                       'Athena' : False,
                       'Thetis' : False,
                       'Zeus' : False,
                       'Hades' : False,
                       'Hermes' : False,
                       'Iris' : False,
                       'Persephone' : False,
                       'Demeter' : False,
                       'Aphrodite' : False,
                       'Apollo' : False,
                       'Poseidon' : False,
                       'Ares' : False}

    def modify_val(self, stat_type, name, val):
        if stat_type == 'player':
            self.player[name] += val
            if self.player[name] > 100:
                self.player[name] = 100
            elif self.player[name] < 0:
                self.player[name] = 0
        if stat_type == 'army':
            self.army[name] += val
            if self.army[name] > 100:
                self.army[name] = 100
            elif self.army[name] < 0:
                self.army[name] = 0

    def get_success(self, stat_type):
        vals = 0
        if stat_type == 'pure luck':
            return random.random() <= self.hidden['luck']
        elif stat_type == 'player':
            vals = sum(self.player.values())
        elif stat_type == 'army':
            vals = sum(self.army.values())
        chance = (vals * self.hidden['luck']) / 100
        return random.random() <= chance
