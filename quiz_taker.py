import tkinter as tk
import random

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
        self.app_window_title("Quiz Taker App")
        self.quiz_questions = quiz_questions
        self_current_questions_index = 0  # keep track of current question
        self.total_score = 0 # track score
        self.selected_option = tk.StringVar()  #store answer

        self.question_txt_label = tk.Label(
            app_window, text="", wraplength=400, # if text is long, it will wrap to a new line after 400 px
            font=("Arial", 14, "bold") # font, size, and style for label text
        )
        self.question_txt_label.pack(pady=20) # provide padding

        self.answer_option_buttons = [] # empty list that hold choices buttons
        for option_index in range(4): 
            option_button = tk.Radiobutton(
                app_window, text="", variable=self.selected_option, value="", #link all radio buttons to one variable
                font=("Arial", 12), anchor='w', justify='left' # font style and size for buttons
            )
            option_button.pack(fill='x', padx=20, pady=2) # place buttons in window with spacing
            self.answer_option_buttons.append(option_button)

        self.answer_feedback_label = tk.Label(  # label for feedback
            app_window, text="", font=("Arial", 12)
        )
        self.answer_feedback_label.pack()

        self.submit_button = tk.Button( #submit button
            app_window, text="Submit", command=self.submit_answer,
            font=('Arial', 12)  # font size and style
        )
        self.submit_button.pack(pady=20)  
        self.final_result_label = tk.Label(
            app_window, text="", font=("Arial", 16, "bold")
        )
        self.final_result_label.pack(pady=10) # display final score
    
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
        self.final_result_label.config(
            text=(f"Your score: {self.total_score}/{len(self.quiz_questions)}")
        )

