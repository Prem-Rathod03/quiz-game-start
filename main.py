from pandas.core.array_algos.quantile import quantile_with_mask

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text= question["text"] #store the question from question_data in question_test variable
    question_answer=question["answer"] #store the answer from question_data in question_answer variable
    new_question=Question(question_text,question_answer) #this will create new object for each question and answer
    question_bank.append(new_question) #this will append all the object created in the  list of question_bank


quiz=QuizBrain(question_bank)
quiz.next_question()