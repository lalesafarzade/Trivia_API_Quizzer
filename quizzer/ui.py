from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#00adb5"
font_color="#126E82"
can_color="#D8E3E7"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzer")
        self.window.config(padx=30,pady=30,bg=THEME_COLOR)
        self.score_label=Label(text="Score:0",fg="#132C33",bg=THEME_COLOR,font=("Balsamiq Sans",15))
        self.score_label.grid(row=0,column=1)
        self.canvas=Canvas(width=400,height=263,bg=THEME_COLOR)  
        
        can_img=PhotoImage(file='images/canvas4.png')
        self.canvas.create_image(200,131,image=can_img)
        self.canvas.config(bg="#00adb5",highlightthickness=0,highlightcolor="#00adb5")
        self.question_text=self.canvas.create_text(200,131,width=300,text="Some Question Text",fill=font_color,font=("Balsamiq Sans",20))
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)

        


        
        self.get_next_question()
        


        self.window.mainloop()
        

    def get_next_question(self):
        self.canvas.config(bg=THEME_COLOR)
        
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.func1()[0]
            self.canvas.itemconfig(self.question_text,text=q_text)
            q_option=self.quiz.func1()[1]
            q_answer=self.quiz.func1()[2]
            
            
            self.a_button=Button(text=q_option[0],highlightthickness=10,width=20,fg=font_color,bg=can_color,font=("Balsamiq Sans",15),bd = '10', command=self.a_pressed)
            self.a_button.grid(row=2,column=0,columnspan=2, pady=15)

       
            self.b_button=Button(text=q_option[1],highlightthickness=10,width=20,fg=font_color,bg=can_color,font=("Balsamiq Sans",15),bd = '10', command=self.b_pressed)
            self.b_button.grid(row=3,column=0,columnspan=2, pady=15)

            self.c_button=Button(text=q_option[2],highlightthickness=10 ,width=20,fg=font_color,bg=can_color,font=("Balsamiq Sans",15),bd = '10', command=self.c_pressed)
            self.c_button.grid(row=4,column=0,columnspan=2, pady=15)

        
            self.d_button=Button(text=q_option[3],highlightthickness=10,width=20,fg=font_color,bg=can_color,font=("Balsamiq Sans",15),bd = '10', command=self.d_pressed)
            self.d_button.grid(row=5,column=0,columnspan=2, pady=15)

            return q_option,q_answer


        else:
            self.canvas.itemconfig(self.question_text,text=f"Your final score: {self.quiz.score}/{self.quiz.question_number}")
            self.a_button.config(state='disabled')
            self.b_button.config(state='disabled')
            self.c_button.config(state='disabled')
            self.d_button.config(state='disabled')
        

    def check_answer(self, user_answer):
        correct_answer = self.get_next_question()[1]
        if user_answer.lower() == correct_answer.lower():
            self.quiz.score += 1
            print('true',f'{self.get_next_question()[1]}',f'{user_answer}')
            return True
        else:
            print('false',f'{self.get_next_question()[1]}',f'{user_answer}')
            return False
   
    def a_pressed(self):
        q_option=self.quiz.func1()[1]
        is_right=self.check_answer(q_option[0])
        self.give_feedback(is_right)
        

    def b_pressed(self):
        q_option=self.quiz.func1()[1]
        is_right=self.check_answer(q_option[1])
        self.give_feedback(is_right)

    def c_pressed(self):
        q_option=self.quiz.func1()[1]
        is_right=self.check_answer(q_option[2])
        self.give_feedback(is_right)

    def d_pressed(self):
        q_option=self.quiz.func1()[1]
        is_right=self.check_answer(q_option[3])
        self.give_feedback(is_right)



    def give_feedback(self,is_right):
        if is_right:
            self.score_label.config(fg="green")
            self.canvas.config(bg="green")
            

        else:
            self.canvas.config(bg="red")
            self.score_label.config(fg="red")
           
          
        


        self.window.after(1000,self.get_next_question)
        self.quiz.question_number += 1

