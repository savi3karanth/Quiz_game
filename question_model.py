class Question:
    def __init__(self,q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

q1 = Question("sasasf", True)
print(q1.text)