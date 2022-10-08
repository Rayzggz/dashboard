from flask import Flask
from src import data

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    dorm, non_dorm, weather = data.readData()
    with open("dorm.txt", 'w') as f:
        f.write(str(dorm))
