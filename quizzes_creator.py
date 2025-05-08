# This is a program that creates quizzes
import emoji
with open("quiz_creator_questions.txt", "a") as file: # This will open the file and add the users input without deleting the old content
    
    while True: 
        quiz_question = input(emoji.emojize("Enter a question:thinking_face:: ")) #Ask the user the questions they want to input
        if not quiz_question.lower().startswith("question:"):
                quiz_question = "Question: " + quiz_question
                
        # These are the choices or possible answers to the question
        letter_a = input(emoji.emojize("Enter letter a :red_apple:: ")).strip()
        letter_b = input(emoji.emojize("Enter letter b :boy:: ")).strip()
        letter_c = input(emoji.emojize("Enter letter c :cow:: ")).strip()
        letter_d = input(emoji.emojize("Enter letter d :dog:: ")).strip()
        
        while True: # This is a nested loop to validate correct answer
            correct_ans = input(emoji.emojize("What letter is the correct answer?:thinking_face: ")).strip().lower()
            if correct_ans in ['a', 'b', 'c', 'd']:
                break  # Exit loop
            else:
                print(emoji.emojize("Invalid.:police_car_light: ")) # The input shoould be a, b, c, d only
        

        file_save = input(f"Do you want to save this question? (yes/no): ").strip().lower()
        if file_save in ["yes", "y"]:
            file.write(quiz_question + "\n")     # It will write the quiz question to a file         
            file.write("a) " + letter_a + "\n")
            file.write("b) " + letter_b + "\n")
            file.write("c) " + letter_c + "\n")
            file.write("d) " + letter_d + "\n")
            file.write("Answer: " + correct_ans + "\n")
            file.write("\n")
            print(emoji.emojize("Question saved!:grinning_face_with_smiling_eyes:\n"))
        else:
            print(emoji.emojize("Question not saved.:frowning_face:\n"))
                
        another_ques = input("Do you want to add another question? (yes/no): ").strip().lower()   # Ask user if they want to add another questions
        if another_ques in ["no", "n"]:
            print(emoji.emojize("Thank you for using Quiz Creator.:waving_hand:"))  # Exiting the program
            break
