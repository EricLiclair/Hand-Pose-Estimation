class SignLanguageTranslator:
    def __init__(self, default_text):
        self.default_text = default_text
        self.text = default_text
        self.queue_size = 5
        self.broken_correct_queue = []

    def append_broken_sentence(self, broken):
        if len(self.broken_correct_queue) == self.queue_size:
            self.remove_oldest_pair()
        self.broken_correct_queue.append((broken, None))
        self.update_text()

    def append_correct_sentence(self, correct):
        if not self.broken_correct_queue:
            return  
        self.broken_correct_queue[-1] = (self.broken_correct_queue[-1][0], correct)
        self.update_text()

    def remove_oldest_pair(self):
        self.broken_correct_queue.pop(0)

    def update_text(self):
        self.text = self.default_text
        for pair in self.broken_correct_queue:
            if pair[0] is not None and pair[1] is not None:
                self.text += f"\nBroken: {pair[0]}\nCorrect: {pair[1]}"
            elif pair[0] is not None:
                self.text += f"\nBroken: {pair[0]}"
            elif pair[1] is not None:
                self.text += f"\nCorrect: {pair[1]}"


default_text = "System: You are an AI Sign Language Translator. You are given sentences which are inferred from a vision model capturing words for signs. Expect the sentences to be broken. Your task is to transform the input sentences to the nearest correct output sentence. Even if the input sentence is grammatically incorrect, try to convey the most prominent response."

translator = SignLanguageTranslator(default_text)

 
broken1 = "hi i shubham1"
translator.append_broken_sentence(broken1)
    
    
    
correct1 = "Hi i am Shubham1"
translator.append_correct_sentence(correct1)
    
print(translator.text)
