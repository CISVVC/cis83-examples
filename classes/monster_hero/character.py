class Character:
  
   def __init__(self,mtype,name,ability,health,manna):
      self.mtype = mtype
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
      return self.health < 0

if __name__ == "__main__":
   monster = Character("Gorgon","Medussa","stone gaze",100,100)
   print(monster)
