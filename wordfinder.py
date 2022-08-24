"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, file):
        self.words = self.get_words(file)
        self.word_count = self.get_word_count(self.words)
    
    def __repr__(self):
        return f'Words: {self.words}, Word Count: {self.word_count}'
        
    def get_word_count(self, words):
        return len(words)

    def get_words(self, file):
        file = open(file, 'r')
        words = file.read().splitlines()
        return words

    def random(self):
        index = random.randint(1, self.word_count)
        return self.words[index]

class SpecialWordFinder(WordFinder):
    
    def __init__(self, file):
        super().__init__(file)
        self.filtered_words = self.get_filtered_words()
    
    def get_filtered_words(self):
        filtered_words = []
        for word in self.words:
            if  (not word.startswith('#') and len(word) != 0):
                filtered_words.append(word)
        return filtered_words

    def random(self):
        index = random.randint(1, len(self.filtered_words))
        return self.filtered_words[index]




