print("")
print("welcome to Quiz")
print("There are 10 questions\n")

def ask_question(question , answer):
    score = 0
    
    for qno in range(1 , 11):
        print(f"Q{qno}. {question[qno - 1]}")
        
        ans = input(f"Enter correct answer: ")
        

        if ans.lower() == answer[qno - 1]:
            print("Correct answer!")
            score += 1
            print(f"Current score: {score}")
            print(" ")
            print(" ")

        else:
            print("wrong answer")
            print(f"Correct answer: {answer[qno - 1]}")
            print(" ")
            print(" ")


questions = ["What is the capital of India?" , "Which planet is called the Red Planet?" , "Who wrote the play Romeo and Juliet?" , "What is the largest mammal in the world?" , "Which gas do plants absorb from the atmosphere?" , "Who discovered gravity after seeing a falling apple?" , "What is the square root of 144?" ,"Which country has the most population in 2026?" , "Which element has the chemical symbol Au?" , "Who developed the Theory of Relativity?"]
correct_answers = ["delhi" , "mars" , "william shakespeare" , "blue whale" , "carbon dioxide" , "isaac newton"  ,"12" , "india" , "gold" , "einstin"]

ask_question(questions , correct_answers)
