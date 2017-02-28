
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.status = "normal"

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.status = "normal"
        self.evade = 0
        self.defense = 0


    def print_status(self):
        #prevent money from dropping below 0
        if (self.coins <= 0):
            self.coins = 0
        print "%s has %d health, %d coins, %d power and, ***status is %s***" % (self.name, self.health, self.coins, self.power, self.status)

    def affliction(self):
        if self.status == "poisoned":
            self.health -= 10
            print "You are poisoned! you lost %d points of health in your poisoning!" % (10)
        elif self.status == "burned":
            self.power = self.power/2
            self.health -= 12
            print "You are burning! your power has been cut in half to %d and you lost %d points of health in your burn!" % (self.power, 15)
        elif self.status == "paralysis":
            self.power = 0
            print "You are paralyzed! you have no strength this turn!!!"
        else:
            print "Your status is normal"
            return

    def attack(self, enemy):
        if not self.alive():
            return
        self.affliction()
        if not(self.status == "paralysis"):
            print "%s attacks %s" % (self.name, enemy.name)
            criticalHit = self.power
        if (random.randint(1,100)/10 <= 2):
            print "**CRITICAL HIT**"
            criticalHit = self.power * 2
        enemy.receive_damage(criticalHit)
        time.sleep(1.5)

    def receive_damage(self, points):
        evasion = self.evade * 5
        if (random.randint(evasion,100) <= evasion):
            print "the enemy's attack missed!"
        self.health -= (points - self.defense)
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        if (self.coins >= item.cost):
            self.coins -= item.cost
            item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'Token Goblin'
        self.health = 6
        self.power = 2

    def reward(self):
        if (self.health >= 0):
            return 5
        else:
            return 0

class Wizard(Character):
    def __init__(self):
        self.name = 'TrickRoom Wizard'
        self.health = 8
        self.power = 1

    def reward(self):
        if (self.health >= 0):
            return 6
        else:
            return 0
    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'Clumsy Medic'
        self.health = 25
        self.power = 1

    def reward(self):
        if (self.health >= 0):
            return 1
        else:
            print "the medic stole an extra 20 coins from you as you ran to pay for student loans!"
            return -20

    def receive_damage(self, points):

        restore = 5
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if (random.randint(1,100)/10 <= 2):
            self.health += restore
            print "The %s restored its health by %d points! its health is now %d" % (self.name, restore, self.health)
        if self.health <= 0:
            print "%s is dead." % self.name

    def mistakeHeal(self,enemy):
        if (random.randint(0,3) == 0):
            print "The medic messed up his spell!!"
            time.sleep(1.5)
            print "%s healed a bit of their health and was cleared of any status!" % enemy.name
            enemy.health += 10
            enemy.status = "normal"
            return True
        return False

    def attack(self, enemy):
        if not self.alive():
            return

        messedUp = self.mistakeHeal(enemy)

        if not messedUp:
            print "%s attacks %s" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
            time.sleep(1.5)

class Shadow(Character):
    def __init__(self):
        self.name = 'The Talkative Greedy Shadow'
        self.health = 1
        self.power = random.randint(0,3)
        self.evade = 11
        self.coins = 30

    def reward(self):
        if (self.health >= 0):
            return 100
        else:
            return 0

    def coinLoss(self, enemy):
        if (random.randint(1,5) == 1):
            print "%s's dark magic suddenly backfired!" % self.name
            time.sleep(1)
            print "..."
            time.sleep(1)
            print "..."
            time.sleep(1)
            print "..."
            print "%s managed to take back all %d coins from %s!" % (enemy.name, self.coins, self.name)
            enemy.coins += self.coins
            self.coins = 0

        else:
            self.coins += 10
            enemy.coins -= 5
            print "%s stole 5 coins from you! it doubled its earnings from theft with dark magic" % self.name
            time.sleep(.5)
        print "%s now has %d coins" % (self.name, self.coins)
        print "%s now has %d coins" % (enemy.name, enemy.coins)

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        self.coinLoss(enemy)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        if (self.evade % 10 == 0):
            self.health -= points
            if self.health <= 0:
                print "%s is dead." % self.name
        else:
            print "Shadow takes a good look at you as it jukes your attack!"
            time.sleep(1)
            if (random.randint(1,6) == 1):
                print "Shadow replies: Thy hath know'st not the power tis Darknessss..."
            elif (random.randint(1,6) == 2):
                print "Thats a nice case case of coin you got there..."
                time.sleep(1)
                print "Shadow was distracted while it counted its coins!"
            else:
                print "Shadow replies: this battle will be a suitable grave for you..."
        self.evade += 1


class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 1
        self.power = 3

    def reward(self):
        return 0


    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s mutters: I...shall never die.." % self.name

    def alive(self):
        return True

class Jelly(Character):
    def __init__(self):
        self.name = 'The Toxic Sentient Neighborhood Jelly'
        self.health = 35
        self.power = 7

    def reward(self):
        if (self.health >= 0):
            return 15
        else:
            return 0

    def attack(self,enemy):
        if not self.alive():
            return

        if ((random.randint(0,2) == 0 and enemy.status == "normal") or enemy.status == "poisoned"):
            enemy.status = "poisoned"
            print "%s attacks %s" % (self.name, enemy.name)
            time.sleep(1)

        enemy.receive_damage(self.power)
        time.sleep(1.5)



class Pyromancer(Character):
    def __init__(self):
        self.name = "The Sickly Deadeye Pyromancer"
        self.health = 6
        self.power = 1

    def reward(self):
        if (self.health >= 0):
            return 1
        else:
            return 0

    def attack(self,enemy):
        if not self.alive():
            return
        enemy.status = "burned"
        print "%s attacks %s" % (self.name, enemy.name)
        time.sleep(1)

        enemy.receive_damage(self.power)
        time.sleep(1.5)





class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee from monster"
            print "4. end the game"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass

            elif input == 3:
                print "You ran away from this enemy!"
                time.sleep(1.5)
                print "But you lost 10 coins, tripped and lost 5 health while running"
                hero.coins -= 10
                if (hero.coins <= 0):
                    hero.coins = 0
                hero.health -= 5
                break
            elif input == 4:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            if not enemy.alive():
                print "You defeated the %s" % enemy.name
                print "You gained a reward of %d coins" % enemy.reward()
                hero.coins += enemy.reward()
            return True
        else:
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 10
        print "%s's health increased to %d." % (character.name, character.health)

class SuperTonic(Tonic):
    cost = 10
    name = 'supertonic'
    def apply(self, character):
        character.health += 15
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Shroud(object):
    cost = 20
    name = 'shroud'
    def apply(self, hero):
        hero.evade += 2
        print "%s's evasion increased to %d." % (hero.name, hero.evade)

class BurnHeal(object):
    cost = 35
    name = 'burn heal'
    def apply(self, character):
        if (character.status == 'burned'):
            character.status = 'normal'
        else:
            print "It had no effect"
        print "%s's status is ." % (character.name, character.status)

class Antidote(object):
    cost = 30
    name = 'antidote'
    def apply(self, character):
        if (character.status == 'poisoned'):
            character.status = 'normal'
        else:
            print "It had no effect"
        print "%s's status is ." % (character.name, character.status)

class Shield(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.defense += 2
        print "%s's power increased to %d." % (hero.name, hero.defense)


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [SuperTonic, Tonic, Sword, Shield, Shroud, Antidote, BurnHeal]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [ Shadow(), Wizard(), Medic(), Jelly(), Pyromancer(), Goblin(), Zombie()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
