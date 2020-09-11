import time
import numpy as np
import sys


# Delay Printing

def delay_print(s):
    # print one character at a time

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, name, types, moves, EVs, health='=========='):
        # We are creating this class to give all the characteristics to a pokemon by taking variables
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['Attack']
        self.defense = EVs['Defense']
        self.health = health
        self.bars = 20

    def fight(self, pokemon2):
        pokemon2.bars = 20
        # We are creating a function to fight between 2 pokemons
        # First we print fight information
        print("-----POKEMON BATTLE IS ABOUT TO BEGIN-----")
        print(f"\n{self.name}")
        print("Type/", self.types)
        print("Attack/", self.attack)
        print("Defense/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        # Now Second Pokemon Information
        print(f"\n{pokemon2.name}")
        print("Type/", pokemon2.types)
        print("Attack/", pokemon2.attack)
        print("Defense/", pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([pokemon2.attack, pokemon2.defense])))

        time.sleep(2)
        # Now type disadvantage consideration
        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.types == k:
                # If both are same type
                if pokemon2.types == k:
                    string_1_attack = "It is not effective...."
                    string_2_attack = "It is not effective...."
                # If Pokemon2 is stronger
                if pokemon2.types == version[(i + 1) % 3]:
                    pokemon2.attack *= 1
                    pokemon2.defense *= 1
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "It is not effective"
                    string_2_attack = "It is super effective"

                # If Pokemon1 is stronger
                if pokemon2.types == version[(i + 2) % 3]:
                    pokemon2.attack /= 1
                    pokemon2.defense /= 1
                    self.attack *= 2
                    self.defense *= 2
                    string_1_attack = 'It is Super Effective!'
                    string_2_attack = 'It is not Effective '

        # Now actual fighting
        # We need to continue this loop until any of the pokemon faints
        while (self.bars > 0) and (pokemon2.bars > 0):
            # print health of 2 pokemons first
            print(f"\n{self.name}\t\tHEALTH\t\n{self.health}")
            print(f"\n{pokemon2.name}\t\tHEALTH\t\n{pokemon2.health}\n")
            # for pokemon 2 to faint from pokemon 1
            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"{self.name} used {self.moves[index - 1]}!\n")
            time.sleep(1)
            delay_print(string_1_attack)

            # We need to determine damage for pokemons
            pokemon2.bars -= self.attack
            pokemon2.health = ""
            # Add back bars and add defense boost
            for j in range(int(pokemon2.bars + .1 * pokemon2.defense)):
                pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\nHEALTH\t\n{self.health}")
            print(f"\n{pokemon2.name}\t\nHEALTH\t\n{pokemon2.health}\n")
            time.sleep(.5)

            # check to see if pokemon2 is fainted
            if pokemon2.bars <= 0:
                delay_print("\n...." + pokemon2.name + ' is fainted....')
                break

            # pokemon2 turn to faint pokemon 1
            print(f"Go {pokemon2.name}!")
            for i, x in enumerate(pokemon2.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"{pokemon2.name} used {pokemon2.moves[index - 1]}!\n")
            time.sleep(1)
            delay_print(string_2_attack)

            # We need to determine damage for pokemons
            self.bars -= pokemon2.attack
            self.health = ""
            # Add back bars and add defense boost
            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"\n{pokemon2.name}\t\tHEALTH\t\n{pokemon2.health}")
            print(f"\n{self.name}\t\tHEALTH\t\n{self.health}\n")
            time.sleep(.5)

            # check to see if pokemon 1 is fainted
            if self.bars <= 0:
                delay_print("\n...." + self.name + ' is fainted....')
                break


if __name__ == '__main__':

    # create pokemon object of every pokemon you want to add
    Charizard = Pokemon('Charizard', 'Fire', ['FlameThrower', 'Blast Burn', 'Aerial Ace', 'Thunder Punch'],
                        {'Attack': 15, 'Defense': 15})
    Blastoise = Pokemon('Blastoise', 'Water', ['HydroPump', 'SkullBash', 'Surf', 'Ice Beam'],
                        {'Attack': 15, 'Defense': 15})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Frenzy Plant', 'Solar Beam', 'Poison Jab', 'Razor Leaf'],
                       {'Attack': 15, 'Defense': 15})

    Venusaur.fight(Venusaur)
