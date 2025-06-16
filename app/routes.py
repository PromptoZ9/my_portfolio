from app import app, render
from .forms import MyForm
from flask import redirect, flash
from . import mail
from flask_mail import Message

@app.route("/email-test")
def send_mail():
    msg = Message (
        "hello", body = "hello world", recipients=['promptdummy@gmail.com']
    )
    mail.send(msg)
    return "Email Sent"

@app.route('/')
def homepage():
    return render('homepage.html')
    #return render_template('homepage.html', path = request.path,portofolios=portofolios)


@app.route("/about-me", methods = ["GET","POST"])
def about_me():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        company = form.company.data
        description = form.description.data
        print(name)
        msg = Message (
            f"{name} - {email} - {company}", body = description, recipients=['zarfan001@gmail.com']
        )
        mail.send(msg)
        flash("Email Sent! 😉")
        return redirect("/about-me")
    return render("about-me.html", form=form)

