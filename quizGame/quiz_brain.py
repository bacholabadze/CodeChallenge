class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 1
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number-1 < len(self.question_list)

    def check_answer(self, ans):
        if ans.lower() == self.question_list[self.question_number - 1].answer.lower():
            self.score += 10
            print(f"Correct! Your current score is {self.score}")
        elif ans == '':
            self.score -= 2
            print(f"You skipped the question! Your current score is {self.score}")
        else:
            self.score -= 5
            print(f"Wrong! Your current score is {self.score}")

    def next_question(self):
        current_question = self.question_list[self.question_number - 1]
        answer = input(f"{self.question_number}) {current_question.text} (True/False):")
        self.check_answer(answer)
        self.question_number += 1
