from flask import Flask, render_template

from src import graphs, data

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
def page1():
    file = open(app.static_folder + "/lib/custom1.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    content = processBar(content, "graph_1_a1", graphs.graph_1_a1())
    content = processText(content, "graph_1_a2", graphs.graph_1_a2())
    content = processText(content, "graph_1_d1", graphs.graph_1_d1())
    content = processText(content, "graph_1_d2", graphs.graph_1_d2())
    content = processText(content, "graph_1_b1", graphs.graph_1_b1())
    content = processText(content, "graph_1_b2", graphs.graph_1_b2())
    return content


@app.route('/lib/custom2.js')
def page2():
    file = open(app.static_folder + "/lib/custom2.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    content = processBar(content, "graph_2_a1", graphs.graph_2_a1())
    content = processText(content, "graph_2_d1", graphs.graph_2_d1())
    content = processText(content, "graph_2_d2", graphs.graph_2_d2())
    content = processText(content, "graph_2_d3", graphs.graph_2_d3())
    content = processText(content, "graph_2_b1", graphs.graph_2_b1())
    content = processText(content, "graph_2_b2", graphs.graph_2_b2())
    return content


@app.route('/lib/custom3.js')
def page3():
    file = open(app.static_folder + "/lib/custom3.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    content = processBar(content, "graph_3_c1", graphs.graph_3_c1())
    content = processText(content, "graph_3_d2", graphs.graph_3_d2())
    content = processText(content, "graph_3_b1", graphs.graph_3_b1())
    content = processText(content, "graph_3_b2", graphs.graph_3_b2())
    content = processBar(content, "graph_3_c2", graphs.graph_3_c2())
    return content


@app.route('/lib/custom4.js')
def page4():
    file = open(app.static_folder + "/lib/custom4.js", "r", encoding="utf-8")
    content = file.read()
    file.close()
    content = processBar(content, "graph_4_c2", graphs.graph_4_c2())
    return content


@app.route('/')
def indexHtml():  # put application's code here
    return render_template('index.html', current_date=data.current_date.strftime("%m/%d/%Y"))


if __name__ == '__main__':
    app.run()
    # test.dailyCostTest()
