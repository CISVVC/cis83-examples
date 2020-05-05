class Question:
   
   def __init__(self,text,a1,a2,a3,a4,answer):
      self.text = text
      self.a1 = a1
      self.a2 = a2
      self.a3 = a3
      self.a4 = a4
      self.answer = answer

   def __str__(self):
      return self.text + "\n" + self.a1 + "\n" + self.a2 + "\n" + self.a3 + \
      "\n" + self.a4 + "\n"
   pass

class Player:
   pass
