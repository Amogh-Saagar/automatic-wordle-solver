# class checker_class:
#     def __init__(self, word, correct_word, yellow_all, yellow_hist, word_hist, all_grey):
#         self.word = word
#         self.correct_word = correct_word
#         self.yellow_all = yellow_all
#         self.yellow_hist = yellow_hist
#         self.word_hist = word_hist
#         self.grey = all_grey
#
#     def check_green(self):
#         for n, i in enumerate(self.correct_word):
#             if i != self.word[n] and i is not None:
#                 return False
#         return True
#
#     def check_yellow(self):
#         for i in self.yellow_all:
#             if i not in self.word:
#                 return False
#         for i in self.grey:
#             if i in self.word:
#                 return False
#         return True
#
#     def check_yellow_same(self):
#         for n, i in enumerate(self.yellow_hist):
#             using_word = self.word_hist[n]
#             for j in i:
#                 try:
#                     if using_word.index(j) == self.word.index(j):
#                         return False
#                 except:
#                     pass
#         return True
#
#     def run(self):
#         if self.check_yellow_same and self.check_yellow and self.check_green:
#             return True
#         else:
#             return False

class checker_class():
    def __init__(self, word, correct_word, yellow_all, yellow_hist, word_hist, grey):
        self.word = word
        self.correct_word = correct_word
        self.yellow_all = yellow_all
        self.yellow_hist = yellow_hist
        self.word_hist = word_hist
        self.grey = grey
    @property
    def check_green(self):
        for n, i in enumerate(self.correct_word):
            if i != self.word[n] and i is not None:
                return False
        return True
    @property
    def check_yellow(self):
        for i in self.yellow_all:
            if i not in self.word:
                return False
        for i in self.grey:
            if i in self.word:
                return False
        return True
    @property
    def check_yellow_same(self):
        for n, i in enumerate(self.yellow_hist):
            using_word = self.word_hist[n]
            for j in i:
                try:
                    if using_word.index(j) == self.word.index(j):
                        return False
                except:
                    pass
        return True
    def run(self):
        if self.check_yellow_same and self.check_yellow and self.check_green:
            return True
        else:
            return False

