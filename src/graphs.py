from src import data, imageTest, uilts, cost


def graph_1_a1():
    """
    draw graph 1 a1
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    ran = [len(tmp) - 24, len(tmp)]
    re = data.washData(tmp, ran=ran)
    names = data.compressNames(data.dorm[1][0], ran=ran, unit=data.TimeUnit.hour, convert_name=True)
    return [str(names), str(re)]


def graph_1_a2():
    """
    draw graph 1 a2
    :return: None
    """
    ran = [len(data.dorm[1][0]) - 24, len(data.dorm[1][0])]
    re = cost.getDailyCost(data.dorm, 0)
    re2 = cost.getDailyCost(data.dorm, 1)
    result = re / re2
    names = data.compressNames(data.dorm[1][0][-24:], ran=ran, unit=data.TimeUnit.hour, convert_name=True)
    assert len(names) == 1
    return [str(names), str(result)]


def graph_1_d1():
    """
    draw graph 1 d1
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    ran = [len(tmp) - 24, len(tmp)]
    re = data.washData(tmp, ran=ran, method=data.CompressMethods.sum, unit=data.TimeUnit.day)
    assert len(re) == 1
    names = data.compressNames(data.dorm[1][0], ran=ran, unit=data.TimeUnit.day, convert_name=True)
    assert len(names) == 1
    return [str(names), str(re)]


def graph_1_d2():
    """
    draw graph 1 d2
    :return: None
    """
    ran = [len(data.dorm[1][0]) - 24, len(data.dorm[1][0])]
    re = cost.getDailyCost(data.dorm, 0)
    names = data.compressNames(data.dorm[1][0], ran=ran, unit=data.TimeUnit.day, convert_name=True)
    assert len(names) == 1
    # todo
    return [str(names), "[" + str(re) + "]"]
