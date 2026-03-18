class Question:
    # Random comment 4: This class represents a quiz question.
    def __init__(self, id, text, options, correct_answer):
        self.id = id
        self.text = text
        self.options = options  # This will be a list of strings
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        """Returns True if the user's answer matches the correct one."""
        return user_answer == self.correct_answer