import re

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def get_stats(self):
        characters = len(self.text)
        words = self.text.split()
        word_count = len(words)
        
        # Count sentences using basic punctuation splitting
        sentences = [s for s in re.split(r'[.!?]+', self.text) if s.strip()]
        sentence_count = len(sentences)
        
        avg_word_length = sum(len(w) for w in words) / word_count if word_count > 0 else 0

        return {
            "characters": characters,
            "words": word_count,
            "sentences": sentence_count,
            "avg_word_length": round(avg_word_length, 2)
        }

# Example usage:
if __name__ == "__main__":
    sample_text = "Python is an amazing programming language. It is versatile and beginner-friendly!"
    analyzer = TextAnalyzer(sample_text)
    print("Text Stats:", analyzer.get_stats())
