from flask import Flask, render_template

from src import data

app = Flask(__name__, static_folder='html',
            template_folder='html',
            static_url_path='')
app.debug = True


@app.route('/lib/custom.js')
def js():
    dorm, non_dorm, weather = data.readData()
    file = open(app.static_folder + "/lib/custom.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    return content


@app.route('/')
def indexHtml():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
