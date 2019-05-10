#from  trivia import Question
#from  trivia import Player

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

questions = [Question("In the human body, what is the hallux?","Head","Nose","Foot","Big Toe",4)

]

#player1 = Player("Paul")
#player2 = Player("Zach")

for question in range(5):
   print(questions[question])
