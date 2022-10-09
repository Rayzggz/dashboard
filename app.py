from flask import Flask, render_template

from src import data, imageTest, graphs, test

app = Flask(__name__, static_folder='html',
            template_folder='html',
            static_url_path='')
app.debug = True


def processBar(content: str, prefix: str, graph: list):
    """
    process replace bar chart
    :param prefix: prefix of replacement
    :param content: content
    :param graph: graph
    :return: content
    """
    return content.replace("{{ " + prefix + "_names }}", graph[0]).replace("{{ " + prefix + "_data }}", graph[1])


def processText(content: str, prefix: str, text: str):
    """
    process replace text
    :param prefix: prefix of replacement
    :param content: content
    :param text: text
    :return: content
    """
    return content.replace("{{ " + prefix + "_data }}", text)


@app.route('/lib/custom1.js')
def js():
    file = open(app.static_folder + "/lib/custom1.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    content = processBar(content, "graph_1_a1", graphs.graph_1_a1())
    content = processBar(content, "graph_1_a2", graphs.graph_1_a2())
    content = processText(content, "graph_1_d1", graphs.graph_1_d1())
    content = processText(content, "graph_1_d2", graphs.graph_1_d2())
    content = processText(content, "graph_1_b1", graphs.graph_1_b1())
    content = processText(content, "graph_1_b2", graphs.graph_1_b2())
    return content


@app.route('/')
def indexHtml():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
    # test.dailyCostTest()
