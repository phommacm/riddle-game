from flask import Flask, render_template, request

app = Flask(__name__)

# Displaying the main page with the riddle
@app.route('/', methods=['GET'])
def index():
    riddle = "Qu'est-ce qui est jaune et qui attend ?"
    return render_template('index.html', riddle=riddle)

# Form submission
@app.route('/submit', methods=['POST'])
def submit_answer():
    user_answer = request.form.get('answer')
    correct_answer = "Jonathan"

    if user_answer.lower() == correct_answer.lower():
        result = "Bravo, c'est la bonne réponse !"
    else:
        result = "Désolé, ce n'est pas la bonne réponse. Essayez à nouveau !"

    return render_template('index.html', riddle="Qu'est-ce qui est jaune et qui attend ?", result=result)

if __name__ == '__main__':
    app.run(debug=True)
