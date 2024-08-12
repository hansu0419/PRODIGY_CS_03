from flask import Flask, render_template, request
from zxcvbn import zxcvbn

app = Flask(__name__)

def passcomplexcheck(password):
    result = zxcvbn(password)

    feedback = {
        'Score': result['score'],  
        'Feedback': result['feedback']['suggestions'],
        'Crack Time': result['crack_times_display']['offline_slow_hashing_1e4_per_second']
    }

    score = result['score']
    if score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    else:
        strength = 'Weak'
    
    return feedback, strength

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title='Password Complexity Checker', result_text='', suggestions=[])

@app.route('/process', methods=['POST'])
def process():
    password = request.form['text']
    feedback, strength = passcomplexcheck(password)
    
    result_text = f"Strength: {strength}<br>Crack Time Estimate: {feedback['Crack Time']}"
    suggestions = feedback['Feedback']
    
    return render_template('index.html', title='Password Complexity Checker', result_text=result_text, suggestions=suggestions)

if __name__ == '__main__':
    app.run(port=9090)
