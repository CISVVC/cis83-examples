from characters import Monster,Hero,Gorgon

from random import randint

def roll(sides):
   return randint(1,sides)

if __name__ == "__main__":
   monster = Gorgon("Medussa","stone gaze",100,100)
   hero = Hero("Perseus","winged sandals",100,100)
   print(str(monster) + " vs. " + str(hero))
#  roll for the hero
   
   count = 0
   while not hero.is_dead() and not monster.is_dead():
      health = roll(12)
      manna = roll(12)
      hero.hit(monster,health,manna)
      if monster.is_dead():
        print("Hooray the monster is dead after ",count," rolls")
      health = roll(12)
      manna = roll(12)
      monster.hit(hero,health,manna)
      if hero.is_dead():
        print("Boo hoo the hero is dead after ",count," rolls")
      count += 1


