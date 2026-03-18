from models import Question

class QuestionManager:
    def __init__(self):
        # A list to store our Question objects
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """Hardcoded questions for the CBT engine."""
        q1 = Question(1, "What is the capital of Nigeria?", ["Lagos", "Kano", "Abuja", "Ibadan"], "Abuja")
        q2 = Question(2, "Which programming language is Flask built on?", ["Java", "Python", "PHP", "C++"], "Python")
        q3 = Question(3, "What does OOP stand for?", ["Office Object Programming", "Object Oriented Programming", "Only One Programming", "Ordered Object Process"], "Object Oriented Programming")
        q4 = Question(4, "What is 2 + 2?", ["3", "4", "5", "6"], "4")
        q5 = Question(5, "Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars")
        q6 = Question(6, "What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific")
        q7 = Question(7, "Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Austen", "Twain"], "Shakespeare")
        q8 = Question(8, "What is the chemical symbol for water?", ["H2O", "CO2", "O2", "NaCl"], "H2O")
        q9 = Question(9, "Which language is used for web development?", ["Python", "HTML", "Assembly", "Fortran"], "HTML")
        q10 = Question(10, "What year did World War II end?", ["1945", "1939", "1950", "1940"], "1945")
        
        self.questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
        

    def get_all_questions(self):
        return self.questions