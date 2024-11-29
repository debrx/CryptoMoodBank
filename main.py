from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

def index():
   return render_template("base.html", data = "")


@app.route('/login')

def login():
   return render_template("login.html", data = "")

if __name__=='__main__':
   app.run(debug=True)