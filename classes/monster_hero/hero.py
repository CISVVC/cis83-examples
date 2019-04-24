class Hero:
  
   def __init__(self,mtype,name,ability,health,manna):
      self.mtype = mtype
      self.name = name
      self.ability = ability
      self.health = health
      self.manna = manna

   def __str__(self):
      return self.name
