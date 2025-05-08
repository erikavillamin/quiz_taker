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
score = 0
for question_index, question in enumerate(quiz, 1):  # for loop through each question
    print(f"\nQuestion {question_index}: {question['question']}")  # print question
    for choice in question['choices']:  # print choices
        print(choice)
    
    user_answer = input("Your answer: ").strip().upper()  # get user's answer
    if user_answer == question['answer']:  # check if user's answer is correct
        print("Correct!")  
        score += 1  # increment score for right answer
    else:
        print(f"Wrong. Correct answer: {question['answer']}") 

print(f"\nQuiz Finished! Your score: {score}/{len(quiz)}")  # print final score


 