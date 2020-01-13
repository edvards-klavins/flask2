from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def getIndex():
  return "Hi!"


@app.route('/home')
def getHome():
  return render_template('home.html')


@app.route('/about')
def getAbout():
  return render_template('about.html')





@app.route('/contact')
def contact():
  return render_template('contact.html', phone = "123")

app.run(host = '0.0.0.0', port = 8020)