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
class quiz_taker_app:   # define class
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

