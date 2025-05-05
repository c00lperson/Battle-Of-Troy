import random

class GameStats:
    def __init__(self):
        start_val = 100

        # Player and army stats start at 100
        self.player = {'HEALTH' : start_val,
                  'STRENGTH' : 80,
                  'ARMOR' : start_val,}

        self.army = {'WARRIORS' : start_val,
                     'MORALE' : start_val,
                     'RESOURCES' : start_val}

        self.armor = {'HELMET' : {'equipped' : False,
                                  'lvl' : 33},
                      'BREASTPLATE' : {'equipped' : False,
                                  'lvl' : 33},
                      'SHIELD' : {'equipped' : False,
                                  'lvl' : 33}}

        self.weapons = {'SPEAR' : {'equipped' : False,
                                  'skill' : 10},
                        'SWORD' : {'equipped' : False,
                                  'skill' : 10},
                        'BOW' : {'equipped' : False,
                                  'skill' : 10}}

        # Default luck is 50%, no gods in favor at game start
        self.favorable_gods = {'Hera' :False,
                               'Athena': False,
                               'Thetis': False,
                               'Hermes': False
                               }
        self.neutral_gods = {'Zeus' : False}

        self.unfavorable_gods = {'Aphrodite' : False,
                                 'Apollo' : False,
                                 'Ares' : False,
                                 'Artemis' : False
                                 }

        self.luck = 0.5

        self.armies = ['Boeotians',
                       'Minyans',
                       'Phoceans',
                       'Aetolians',
                       'Rhodians',
                       'Symians']

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

        if stat_type == 'armor':
            self.armor[name]['lvl'] += val
            if self.armor[name]['lvl'] > 100:
                self.armor[name]['lvl'] = 100
            elif self.armor[name]['lvl'] < 0:
                self.armor[name]['lvl'] = 0


    def equipment_off(self):
        for item in self.armor.keys():
            if self.armor[item]['equipped']:
                self.player['ARMOR'] -= self.armor[item]['lvl']
                self.armor[item]['equipped'] = False
                # Decrease armor quality after battle
                self.armor[item]['lvl'] -= random.randint(1, 5)
        for item in self.weapons.keys():
            if self.weapons[item]['equipped']:
                self.player['STRENGTH'] -= self.weapons[item]['skill']
                self.weapons[item]['equipped'] = False

    def get_success(self, stat_type):
        vals = 0
        chance = 0
        if stat_type == 'pure luck':
            return random.random() <= self.luck
        elif stat_type == 'player':
            vals = sum(self.player.values())
            chance = vals / 300
        elif stat_type == 'army':
            vals = sum(self.army.values())
            chance = vals / 300
        elif stat_type == 'overall':
            vals = sum(self.player.values()) + sum(self.army.values())
            chance = vals / 600

        return random.random() <= chance
