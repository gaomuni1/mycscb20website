from flask import Flask, render_template, request, redirect, url_for     
import re
from string import digits

app = Flask(__name__)

def process_name(name):
    processed_name = re.sub(r'\d+', '', name).strip()

    if re.search(r'\d', name):
        table = str.maketrans('', '', digits)
        new_name = name.translate(table)
        return new_name.upper()
    else:
        if processed_name.isupper():
            return processed_name.lower()
        elif processed_name.islower():
            return processed_name.upper()
        else:
            return processed_name.capitalize()

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/course_team')
def course_team():
    return render_template("team.html")

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/labs')
def labs():
    return render_template("labs.html")

@app.route('/assignments')
def assignments():
    return render_template("assignments.html")

@app.route('/syllabus')
def syllabus():
    return render_template("syllabus.html")

@app.route('/piazza')
def piazza():
    return redirect('https://piazza.com/class/lqy466htv8g5xb/post/6')

@app.route('/markus')
def markus():
    return redirect('https://markus148.teach.cs.toronto.edu/2024-01/?locale=en')

@app.route('/cdf_labs')
def cdf_labs():
    return redirect('https://www.cdf.toronto.edu/')

@app.route('/calendar')
def calendar():
    return render_template("calender.html")

@app.route('/feedbacks',methods=['GET', 'POST'])
def feedbacks():
    if request.method == 'POST':
        return redirect(url_for('confirmation'))
    return render_template("feedbacks.html")
 
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/<name>')
def greet(name):
    greeting_name = process_name(name)
    return f'Welcome, {greeting_name}, to my CSCB20 website!'


    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

 
