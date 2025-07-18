import random
import re
from collections import defaultdict, Counter

class PredictiveTextGenerator:
    def __init__(self, n=3):
        self.n = n  # n-gram size
        self.ngrams = defaultdict(list)
        self.custom_words = set()

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text.split()

    def train(self, text):
        words = self.preprocess(text)
        for i in range(len(words) - self.n + 1):
            key = tuple(words[i:i + self.n - 1])
            next_word = words[i + self.n - 1]
            self.ngrams[key].append(next_word)

    def train_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
            self.train(data)

    def add_custom_word(self, word):
        self.custom_words.add(word.lower())

    def predict(self, input_text, top_k=3):
        input_words = self.preprocess(input_text)
        if len(input_words) < self.n - 1:
            return ["Type more words..."]
        
        key = tuple(input_words[-(self.n - 1):])
        next_words = self.ngrams.get(key, [])

        if not next_words and self.custom_words:
            return list(random.sample(self.custom_words, min(top_k, len(self.custom_words))))
        
        if not next_words:
            return ["No prediction found"]
        
        word_counts = Counter(next_words)
        predictions = [word for word, _ in word_counts.most_common(top_k)]
        return predictions

# ----------- Main Program -----------
if __name__ == "__main__":
    ptg = PredictiveTextGenerator(n=3)
    ptg.train_from_file("corpus.txt")

    # Add frequently used custom words
    ptg.add_custom_word("chatgpt")
    ptg.add_custom_word("machine")
    ptg.add_custom_word("learning")

    print("\n🔮 Advanced Predictive Text Generator")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter a phrase: ")
        if user_input.lower() == 'exit':
            break
        predictions = ptg.predict(user_input)
        print("→ Predictions:", ', '.join(predictions))
