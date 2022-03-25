import html
import pyttsx3
import random

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        #self.question_number += 1
        q_text=html.unescape(self.current_question.text)  
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
    
        return f"Q.{self.question_number}: {q_text}" ,engine.say(f"{q_text}"),engine.runAndWait()
        
    

    def func(self):
        self.current_question = self.question_list[self.question_number]
        #self.question_number += 1
        q_text=html.unescape(self.current_question.text)
        q_option=[html.unescape(i) for i in self.current_question.false]
        q_answer=html.unescape(self.current_question.answer)
        q_option.append(q_answer)
        random.shuffle(q_option)
        return f"Q.{self.question_number+1}: {q_text}",q_option,q_answer

    def func1(self):
        self.current_question = self.question_list[self.question_number]
        #self.question_number += 1
        q_text=html.unescape(self.current_question.text)
        q_option=[html.unescape(i) for i in self.current_question.false]
        q_answer=html.unescape(self.current_question.answer)
        #random_index=random.choice([0,1,2,3])
        #q_option.insert(random_index, q_answer)
        
        return f"Q.{self.question_number+1}: {q_text}",q_option,q_answer

    
        

            

        #user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        #self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.func()[2]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('true',f'{self.func()[2]}',f'{user_answer}')
            return True
        else:
            print('false',f'{self.func()[2]}',f'{user_answer}')
            return False
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
