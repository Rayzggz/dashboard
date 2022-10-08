from src import data, imageTest, uilts


def graph_1_a1():
    """
    draw graph 1 a1
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    re1 = data.washData(tmp, ran=[len(tmp) - 24, len(tmp)])
    names = []
    for a in data.dorm[1][0][-24:]:
        print(a)
        names.append(uilts.name4hour(a))
    print(re1)
    return [names, re1]
