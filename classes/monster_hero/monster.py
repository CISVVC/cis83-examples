class Monster:
  
   #'type':'Gorgon','name':'Medusa','ability':'stone gaze','health':100,'manna':100
   def __init__(self,mtype,name,ability,health,manna):
      self.mtype = mtype
      self.name = name
      self.ability = ability
      self.health = health
      self.manna = manna

   def __str__(self):
      return self.name
