# It is a way to seperate our app out. So all our views are not 
# defined it one file. It is split up nicely and organized 

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
# this function will run whenever 
# we are in our home url
def home():
    return render_template("home.html")


