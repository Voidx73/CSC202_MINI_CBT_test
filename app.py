import os
from flask import Flask, render_template, request, redirect, url_for, session
from question_manager import QuestionManager
from datetime import datetime

# Random comment 1: This is a Flask application for a mini CBT test.

# This part tells Flask exactly where your folder is located on your PC
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = "csc202_secret_key"

manager = QuestionManager()

@app.route('/')
def index():
    session.clear()
    return render_template('home.html')

@app.route('/quiz/<int:page>', methods=['GET', 'POST'])
def quiz(page):
    questions = manager.get_all_questions()
    total_questions = len(questions)
    
    if page < 1 or page > total_questions:
        return redirect(url_for('quiz', page=1))
    
    if page == 1:
        session['start_time'] = datetime.now().strftime("%H:%M:%S")
        session['answers'] = {}
    
    if request.method == 'POST':
        # Save the answer for the current page
        current_q = questions[page - 1]
        user_answer = request.form.get(f"question_{current_q.id}")
        session['answers'][str(current_q.id)] = user_answer
        
        action = request.form.get('action')
        if action == 'next' and page < total_questions:
            return redirect(url_for('quiz', page=page + 1))
        elif action == 'previous' and page > 1:
            return redirect(url_for('quiz', page=page - 1))
        elif action == 'submit':
            return redirect(url_for('submit_quiz'))
    
    # GET request: show the question for this page
    current_q = questions[page - 1]
    return render_template('quiz_page.html', 
                           question=current_q, 
                           page=page, 
                           total=total_questions,
                           is_last=(page == total_questions))

@app.route('/submit', methods=['GET'])
def submit_quiz():
    questions = manager.get_all_questions()
    score = 0
    answers = session.get('answers', {})
    
    for q in questions:
        user_answer = answers.get(str(q.id))
        if user_answer == q.correct_answer:
            score += 1
            
    end_time = datetime.now().strftime("%H:%M:%S")
    
    return render_template('result.html', 
                           score=score, 
                           total=len(questions),
                           start_time=session.get('start_time'),
                           end_time=end_time)

if __name__ == '__main__':
    app.run(debug=True)