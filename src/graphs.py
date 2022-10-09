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
    ran = [len(data.dorm[1][0]) - 24 * 2, len(data.dorm[1][0])]
    re = cost.getDailyCost(data.dorm, 0)
    re2 = cost.getDailyCost(data.dorm, 1)
    names = data.compressNames(data.dorm[1][0], ran=ran, unit=data.TimeUnit.day, convert_name=True)
    assert len(names) == 2
    return [str(names), str([re, re2])]


def graph_1_b1():
    """
    draw graph 1 b1
    :return: None
    """
    re = "["
    re += data.getDailyData(data.dorm, "Steam")
    re += data.getDailyData(data.dorm, "Electricity")
    re += data.getDailyData(data.dorm, "Chilled Water")
    re += data.getDailyData(data.dorm, "Hot Water")
    re += data.getDailyData(data.dorm, "Natural Gas")
    return re[:-1] + "]"


def graph_1_b2():
    """
    draw graph 1 b2
    :return: None
    """
    re = "["
    re += cost.getDailyCostForPie(data.dorm, "Steam", 0)
    re += cost.getDailyCostForPie(data.dorm, "Electricity", 0)
    re += cost.getDailyCostForPie(data.dorm, "Chilled Water", 0)
    re += cost.getDailyCostForPie(data.dorm, "Hot Water", 0)
    re += cost.getDailyCostForPie(data.dorm, "Natural Gas", 0)
    return re[:-1] + "]"


def graph_1_d1():
    """
    draw graph 1 d1
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    ran = [len(tmp) - 24, len(tmp)]
    re = data.washData(tmp, ran=ran, method=data.CompressMethods.sum, unit=data.TimeUnit.day)
    assert len(re) == 1
    return str(re[0])


def graph_1_d2():
    """
    draw graph 1 d2
    :return: None
    """
    re = cost.getDailyCost(data.dorm, 0)
    return str(re)
