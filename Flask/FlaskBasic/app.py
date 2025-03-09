from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def start():
    # print(render_template('start.html'))
    return render_template('start.html')


@app.route('/home')
def home():
    return render_template('home.html',name='Shubham',arr=[i for i in range(10,20)])



if __name__ == '__main__':
    app.run(use_reloader = True,debug=True)