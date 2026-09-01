class Flashcard:
    """Represents a single flashcard with a question, answer, and mastery status."""

    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer
        self.is_mastered = False

    def check_answer(self, user_response: str) -> bool:
        """Compares user input with the correct answer (case-insensitive strip)."""
        return user_response.strip().lower() == self.answer.strip().lower()


class FlashcardQuiz:
    """Manages a collection of flashcards, user interaction, and score tracking."""

    def __init__(self, topic: str):
        self.topic = topic
        self.deck = []

    def add_card(self, question: str, answer: str) -> None:
        """Adds a new flashcard to the deck."""
        self.deck.append(Flashcard(question, answer))

    def start_quiz(self) -> None:
        """Runs the interactive quiz loop through all flashcards."""
        if not self.deck:
            print(f"No flashcards available in the '{self.topic}' deck!")
            return

        score = 0
        total = len(self.deck)

        print(f"\n--- Starting Quiz: {self.topic} ({total} Questions) ---")
        for index, card in enumerate(self.deck, start=1):
            print(f"\nQuestion {index}: {card.question}")
            user_input = input("Your Answer: ").strip()

            if card.check_answer(user_input):
                print("Correct!")
                score += 1
                card.is_mastered = True
            else:
                print(f"Incorrect. The correct answer was: {card.answer}")

        self._show_summary(score, total)

    def _show_summary(self, score: int, total: int) -> None:
        """Displays performance statistics at the end of the quiz session."""
        percentage = (score / total) * 100
        print(f"\n=== Quiz Results for {self.topic} ===")
        print(f"Score: {score} / {total}")
        print(f"Accuracy: {percentage:.2f}%")
        if percentage == 100:
            print("Outstanding! You mastered every card!")
        elif percentage >= 70:
            print("Great job! Keep practicing to lock in the rest.")
        else:
            print("Good effort! Review the material and try again.")


# --- Example Usage ---
if __name__ == "__main__":
    # Create a Python fundamentals flashcard deck
    python_quiz = FlashcardQuiz("Python Basics")

    python_quiz.add_card("What keyword is used to define a function in Python?", "def")
    python_quiz.add_card("Which data type is immutable: list or tuple?", "tuple")
    python_quiz.add_card("What is the output of type(5)?", "<class 'int'>")

    # Run the interactive quiz session
    python_quiz.start_quiz()
