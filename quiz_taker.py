file_name = "quiz_creator_questions.txt"
with open(file_name, 'r') as file: # open and read file
    questions = file.read().strip()
    blocks = questions.split('\n\n') # question is separated by a blank line

quiz = [] 
for block in blocks: # it is a loop over each question block
    lines = block.strip().split('\n')  #this will split the block into separate lines

    question = lines[0].replace("Question: ", "").strip() 
    choices = lines[1:5]  # four lines after question

    answer = lines[5]  #ensure the line for answer is correctly formatted 
    if not answer.lower().startswith('answer: '): # the line should start with answer, skip if not
        print("Invalid")
        continue
    quiz_answer = answer[len('answer: '):].strip().upper  # the answer is stored as a single uppercase letter as correct answer

    quiz.append({
        'question': question,
        'choices' : choices,
        'answer' : answer
    })

score = 0
for question_index, question in enumerate(quiz, 1):  # for loop through each question
    print(f"\nQuestion {question_index}: {question['question']}")  # print question
    for choice in question['choices']:  # print choices
        print(choice)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()  # get user's answer
    if user_answer == question['answer']:  # check if user's answer is correct
        print("Correct!")  
        score += 1  # increment score for right answer
    else:
        print(f" Wrong. Correct answer: {question['answer']}") 

print(f"\n Quiz Finished! Your score: {score}/{len(quiz)}")  # print final score

 