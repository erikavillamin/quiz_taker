import tkinter as tk
import random

background_color = "#FFFFFF"  # white
text_color = "#000000"    # black
accent_color = "#FF8C00"    # orange

file_name = "quiz_creator_questions.txt"
with open(file_name, 'r') as file: # open and read file
    questions = file.read().strip()
    blocks = questions.split('\n\n') # question is separated by a blank line

quiz = [] 
for block in blocks: # it is a loop over each question block
    lines = block.strip().split('\n')  #this will split the block into separate lines

    question_line = lines[0].replace("Question: ", "").strip() 
    choices_line = lines[1:5]  # four lines after question

    answer_line = lines[5]  #ensure the line for answer is correctly formatted 
    if not answer_line.lower().startswith('answer: '): # the line should start with answer, skip if not
        print("Invalid", answer_line)
        continue
    quiz_answer = answer_line.replace("Answer: ", "").strip().upper() # the answer is stored as a single uppercase letter as correct answer

    quiz.append({
        'question': question_line,
        'choices' : choices_line,
        'answer' : quiz_answer
    })

random.shuffle(quiz)
class QuizTakerApp:   # define class
    def __init__(self, app_window, quiz_questions):  # initialize
        self.app_window = app_window
        self.app_window.title("Quiz Taker App")
        self.app_window.configure(bg=background_color)
        self.quiz_questions = quiz_questions
        self.current_question_index = 0  # keep track of current question
        self.total_score = 0 # track score
        self.selected_option = tk.StringVar()  #store answer

        self.question_text_label = tk.Label(
            app_window, text="", wraplength=400, # if text is long, it will wrap to a new line after 400 px
            font=("Arial", 14, "bold"), bg=background_color, fg=accent_color # font, size, and style for label text
        )
        self.question_text_label.pack(pady=20) # provide padding

        self.answer_option_buttons = [] # empty list that hold choices buttons
        for option_index in range(4): 
            option_button = tk.Radiobutton(
                app_window, text="", variable=self.selected_option, value="", #link all radio buttons to one variable
                font=("Arial", 12), anchor='w', justify='left', # font style and size for buttons
                bg=background_color, fg=text_color, selectcolor=background_color,
                activeforeground=accent_color
            )
            option_button.pack(fill='x', padx=20, pady=2) # place buttons in window with spacing
            self.answer_option_buttons.append(option_button)

        self.answer_feedback_label = tk.Label(  # label for feedback
            app_window, text="", font=("Arial", 12),
            bg=background_color, fg=text_color
        )
        self.answer_feedback_label.pack()

        self.submit_button = tk.Button( #submit button
            app_window, text="Submit", command=self.submit_answer,
            font=('Arial', 12), bg=accent_color, fg=background_color, activebackground="#ffa733"  # font size and style
        )
        self.submit_button.pack(pady=20)  
        self.final_result_label = tk.Label(
            app_window, text="", font=("Arial", 16, "bold"),
            bg=background_color, fg=accent_color
        )
        self.final_result_label.pack(pady=10) # display final score

        self.display_next_question()
    
    def display_next_question(self): # display next questions and choices
        self.answer_feedback_label.config(text="")
        if self.current_question_index >= len(self.quiz_questions):
            self.display_final_score()
            return
        self.selected_option.set(None) # clears selected option before display next question
        current_question = self.quiz_questions[self.current_question_index]
        self.question_text_label.config(
            text=(f"Q{self.current_question_index + 1}: {current_question['question']}")
        ) 
        for button_index, choice in enumerate(current_question['choices']): # update each ansswer option button with corresponding choices
            choice_value = choice[0].upper()
            self.answer_option_buttons[button_index].config(
                text=choice, value=choice_value, state=tk.NORMAL
            )
    def submit_answer(self):  # submit answer
        user_answer = self.selected_option.get()
        correct_answer = self.quiz_questions[self.current_question_index]['answer']

        if user_answer == correct_answer: # check 
            self.total_score += 1
        self.current_question_index += 1
        self.display_next_question()

    def display_final_score(self):  # display result
        self.question_text_label.config(text="Quiz Finished!")
        for button in self.answer_option_buttons:
            button.pack_forget()
        self.submit_button.pack_forget()
        self.answer_feedback_label.pack_forget()

        total_questions = len(self.quiz_questions)
        percentage = (self.total_score / total_questions) * 100

        if percentage >= 80:
            feedback_text = "Excellent work!"
            score_color = "#28a745" #green
        elif percentage >= 50:
            feedback_text = "Good job!"
            score_color = "#FFA500" #orange
        else:
            feedback_text = "Better luck next time!"
            score_color = "#FF4C4C" #red
        
        result_frame = tk.Frame(self.app_window, bg=background_color, bd=2, relief="ridge")
        result_frame.pack(pady=20, padx=30)

        result_label = tk.Label(
             result_frame,
             text=f"Your Score: {self.total_score}/{total_questions} ({int(percentage)}%)\n{feedback_text}",
             font=("Arial", 16, "bold"),
             fg=score_color,
             bg=background_color,
             justify="center"
        )      
        result_label.pack(padx=20, pady=20)
        
        restart_button = tk.Button(     # restart
            self.app_window,
            text="Retake Quiz",
            font=('Arial', 12),
            bg=accent_color,
            fg=background_color,
            activebackground="#ffa733",
            command=self.restart_quiz
        )
        restart_button.pack(pady=10)
        
    def restart_quiz(self):
        self.current_question_index = 0
        self.total_score = 0
        for widget in self.app_window.winfo_children():
            widget.destroy()
        self.__init__(self.app_window, self.quiz_questions)

app_window = tk.Tk()
app_window.geometry("500x450")
app = QuizTakerApp(app_window, quiz)
app_window.mainloop()

