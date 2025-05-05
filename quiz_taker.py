file_name = "quiz_creator_questions.txt"
with open(file_name, 'r') as file: # open and read file
    questions = file.read().strip()
    blocks = questions.split('\n\n') # question is separated by a blank line

quiz = [] 
for block in blocks: # it is a loop over each question block
    lines = block.strip().split('\n')  #this will split the block into separate lines

    question = lines[0][len("Question: "):] # extract question
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

