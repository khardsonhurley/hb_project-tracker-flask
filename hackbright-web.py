from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)
app.secret_key = "SECRET!"


@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html", first=first, last=last, github=github, grades=grades)
    return html

@app.route("/student_add")
def student_add():
    """Add a student."""

    return render_template("student_add.html")

@app.route("/complete_add", methods=["POST"])
def complete_add():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)
    
    return render_template("complete_add.html",first=first_name, last=last_name, github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
