questions = [
    {"prompt":"What is the capital of France?",
     "options":["A. Paris","B. London","C. Berlin","D. Madrid"],
     "answer":"A"
     },
     {"prompt":"Which Language is primarly spoken in Brazil?",
     "options":["A. Spanish","B. Portuguese","C. English","D. French"],
     "answer":"B"
     },
      {"prompt":"What is the smallest prime number?",
     "options":["A. 1","B. 2","C. 3","D. 4"],
     "answer":"B"
     },
      {"prompt":"Who wrote 'To Kill a Mockingbird'?",
     "options":["A. Harper Lee","B. Mark Twain","C. J.K.Rowling","D. Ernest Hemingway"],
     "answer":"A"
     }
]

def run_quiz(question):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer=(input("Enter your answer(A,B,C,OR D):"))
        
        if answer.upper() == question["answer"]:
            print("Correct,hooray!!\n")
            score+=1
        else:
            print("Wrong,Loser!! the correct answer was",question["answer"],"\n")
        
    print(f"You got {score} out of {len(questions)} questions correct.")  


run_quiz(questions)








