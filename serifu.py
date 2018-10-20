import os
import pickle
import random
from janome.tokenizer import Tokenizer


class SerifuGenerator(object):
    tokenizer = False
    model = {}
    use_model = {}

    def __init__(self, target):
        self.set_model(target)

    def set_model(self, target):
        if os.path.exists('pickle_model/'+target):
            with open('pickle_model/'+target, mode='rb') as f:
                self.model = pickle.load(f)
        else:
            self.update_model_save(target)

    def update_model_save(self, target):
        self.update_model(target)
        with open('pickle_model/'+target, mode='wb') as f:
            pickle.dump(self.model, f)

    def update_model(self, target):
        self.model = {'serifu_start': [], 'serifu_end': []}
        if not os.path.exists('model/'+target):
            with open('model/'+target, mode='w', encoding='utf-8') as f:
                f.write("")
        with open('model/'+target, mode='r', encoding='utf-8') as f:
            for line in f:
                self.add_model(line)

    def add_model(self, serifu):
        tokenizer = self.get_tokenizer()
        tokens = tokenizer.tokenize(serifu)
        if tokens:
            words = self.get_word_list(tokens)
            before_word = 'serifu_start'
            for word in words:
                if before_word not in self.model:
                    self.model[before_word] = []
                self.model[before_word] += [word]
                before_word = word
            self.model["serifu_end"] +=[word]

    def get_serifu(self):
        serifu = ''
        self.use_model = self.model
        last_word = 'serifu_start'
        while(last_word and (len(serifu) < 20 or last_word not in self.model['serifu_end'])):
            last_word = self.next_word(last_word)
            if last_word:
                serifu += last_word
        return serifu

    def get_word_list(self, tokens):
        words = []
        for token in tokens:
            if len(words) > 0 and (
                '助詞' in token.part_of_speech or
                '記号' in token.part_of_speech or
                '接頭詞' in token.part_of_speech or
                token.surface == "ー"
            ):
                words[-1] += token.surface
            else:
                words += [token.surface]
        return words

    def next_word(self, word):
        if word in self.use_model:
            next_words = self.model[word]
            return random.choice(next_words) if next_words else ""
        return False

    def get_tokenizer(self):
        if not self.tokenizer:
            self.tokenizer = Tokenizer()
        return self.tokenizer
