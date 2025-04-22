from flask import Flask, render_template, request, redirect, url_for 
from app.forms import MyForm 

app = Flask(__name__)


def render(template: str,**kwargs):
    kwargs["path"] = request.path
    return render_template(template, **kwargs)


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
        return redirect("/about-me")
    return render('about-me.html', form=form)
