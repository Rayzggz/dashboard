from flask import Flask, render_template

from src import data, imageTest, graphs

app = Flask(__name__, static_folder='html',
            template_folder='html',
            static_url_path='')
app.debug = True


@app.route('/lib/custom1.js')
def js():
    file = open(app.static_folder + "/lib/custom1.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    n, d = graphs.graph_1_a1()
    content = content.replace("{{ graph_1_a1_names }}", n)
    content = content.replace("{{ graph_1_a1_data }}", d)
    return content


@app.route('/')
def indexHtml():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    # app.run()
    graphs.graph_1_a1()
