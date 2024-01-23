from flask import render_template, request, redirect
from flask import current_app as app


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        name = "Yugendra"
        subject = "MAD-01"
        list = ["A", "B", "C"]
        return render_template("home.html", name = name, subject = subject, list=list, show_list=True)
    if request.method == "POST":
        text_submitted = request.form["text_submitted"]
        print(text_submitted)
        return "form submitted"