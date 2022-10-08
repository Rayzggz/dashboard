from flask import Flask, render_template

from src import data, imageTest, graphs

app = Flask(__name__, static_folder='html',
            template_folder='html',
            static_url_path='')
app.debug = True


def processReplace(content: str, prefix: str, graph: tuple):
    """
    process replace
    :param prefix: prefix of replacement
    :param content: content
    :param graph: graph
    :return: content
    """
    return content.replace("{{ " + prefix + "_names }}", graph[0]).replace("{{ " + prefix + "_data }}", graph[1])


@app.route('/lib/custom1.js')
def js():
    file = open(app.static_folder + "/lib/custom1.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    processReplace(content, "graph_1_a1", graphs.graph_1_a1())
    processReplace(content, "graph_1_d1", graphs.graph_1_d1())
    processReplace(content, "graph_1_d2", graphs.graph_1_d2())
    return content


@app.route('/')
def indexHtml():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
    # graphs.graph_1_a1()
