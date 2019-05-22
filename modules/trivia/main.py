from  trivia import Question
from  trivia import Player


questions = [
   Question("Question 0 text","q0 option 1","q0 option 2","q0 option 3","q0 option 4",1),
   Question("Question 1 text","q1 option 1","q1 option 2","q1 option 3","q1 option 4",2),
   Question("Question 2 text","q2 option 1","q2 option 2","q2 option 3","q2 option 4",3),
   Question("Question 3 text","q3 option 1","option 2","option 3","q3 option 4",0),
   Question("Question 4 text","option 1","option 2","option 3","option 4",1),
   Question("Question 5 text","option 1","option 2","option 3","option 4",2),
   Question("Question 6 text","option 1","option 2","option 3","option 4",3),
   Question("Question 7 text","option 1","option 2","option 3","option 4",4),
   Question("Question 8 text","option 1","option 2","option 3","option 4",0),
   Question("Question 9 text","option 1","option 2","option 3","option 4",1)
]

player1 = Player("Jack")
player2 = Player("Jill")

# do player 1's questions
for question in range(5):
# display the question
# get answer from player 1
# check the answer using Questions checkAnswer method
#   if the answer is correct
#     player1 gets a point 

for question in range(5,10):
# display the question
# get answer from player 2
# check the answer using Questions checkAnswer method
#   if the answer is correct
#     player1 gets a point 

if player1.points > player2.points:
# player1 wins
elif player1.points < player2.points:
# player2 wins
else
# tie
