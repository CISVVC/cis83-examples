class Character:
  
   def __init__(self,name,ability,health,manna):
      self.name = name
      self.ability = ability
      self.health = health
      self.manna = manna

   def __str__(self):
      return self.name
   
   def hit(self,char,health,manna):
      char.health = char.health - health
      char.manna = char.manna - manna

   def is_dead(self):
      return self.health <= 0


class Monster(Character):
  
   def __init__(self,name,ability,health,manna):
      Character.__init__(self,name,ability,health,manna)
if __name__ == "__main__":
   m = Monster("Medussa",100,100,100)
   print(m)

class Gorgon(Monster):

   def __init__(self,name,ability,health,manna):
      Monster.__init__(self,name,ability,health,manna)
   
   def hit(self,char,health,manna):
      print("The Gorgon hits first with snaky hair")
      super().hit(char,health,manna)

class Hero(Character):
  
   def __init__(self,name,ability,health,manna):
      Character.__init__(self,name,ability,health,manna)

if __name__ == "__main__":
   h = Hero("Perseus",100,100,100)
   print(h)
