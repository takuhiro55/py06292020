
from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/search/<word>')
def search(word):
    return redirect('https://www.google.com/search?q='+word)
@app.route('/user/<name>')
def user(name):
    if name.lower() == "apple":
        return redirect('https://www.apple.com/')
    else:
        return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug = True)

