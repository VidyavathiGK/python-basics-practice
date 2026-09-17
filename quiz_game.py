class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        print("--- Welcome to the Python Quiz Game! ---")
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {q.prompt}")
            user_answer = input("Your answer: ").strip().lower()
            
            if user_answer == q.answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {q.answer}")
                
        print(f"\nQuiz Over! Your final score is {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    question_prompts = [
        ("What is the extension of a Python file? (.py/.java/.cpp)", ".py"),
        ("Which keyword is used to define a function in Python? (def/function/fun)", "def"),
        ("Is Python a case-sensitive language? (yes/no)", "yes")
    ]
    
    questions = [Question(p[0], p[1]) for p in question_prompts]
    game = QuizGame(questions)
    game.run_quiz()
