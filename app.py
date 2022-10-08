from flask import Flask, render_template

from src import data

app = Flask(__name__, static_folder='src/html/',
            template_folder='src/html/',
            static_url_path='')
app.debug = True


@app.route('/')
def indexHtml():  # put application's code here
    dorm, non_dorm, weather = data.readData()
    print(dorm[1][0][-24:])
    return render_template('index.html',
                           chartData=dorm[1][1][-24:],
                           nameData=dorm[1][0][-24:])


if __name__ == '__main__':
    app.run()
    # dorm, non_dorm, weather = data.readData()
    # image.img(dorm[1][0][-24:], dorm[1][1][-24:], dorm[0][1])
