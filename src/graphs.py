from src import data, cost


def graph_1_a1():
    """
    draw graph 1 a1
    Daily energy consumption
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    # noinspection PyTypeChecker
    ran = [len(tmp) - data.TimeUnit.day.value, len(tmp)]
    re = data.washData(tmp, ran=ran)
    names = data.compressNames(data.dorm[1][0], ran=ran, unit=data.TimeUnit.hour, convert_name=True)
    return [str(names), str(re)]


def graph_1_a2():
    """
    draw graph 1 a2
    today cost vs yesterday cost
    :return: None
    """
    # noinspection PyTypeChecker
    ran = [len(data.dorm[1][0]) - data.TimeUnit.day.value * 2, len(data.dorm[1][0])]
    re = cost.getDailyCost(data.dorm, 0)
    re2 = cost.getDailyCost(data.dorm, 1)
    names = data.compressNames(data.dorm[1][0], ran=ran, unit=data.TimeUnit.day, convert_name=True)
    assert len(names) == 2
    return [str(names), str([re, re2])]


def graph_1_b1():
    """
    draw graph 1 b1
    Daily energy consumption categories pie chart
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
    Daily energy cost categories pie chart
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
    Daily energy consumption
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    # noinspection PyTypeChecker
    ran = [len(tmp) - data.TimeUnit.day.value, len(tmp)]
    re = data.washData(tmp, ran=ran, method=data.CompressMethods.sum, unit=data.TimeUnit.day)
    assert len(re) == 1
    return str(re[0])


def graph_1_d2():
    """
    draw graph 1 d2
    Daily cost
    :return: None
    """
    re = cost.getDailyCost(data.dorm, 0)
    return str(re)


def graph_2_d1():
    """
    draw graph 1 d1
    Monthly energy consumption
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    # noinspection PyTypeChecker
    ran = [len(tmp) - data.TimeUnit.month.value, len(tmp)]
    re = data.washData(tmp, ran=ran, method=data.CompressMethods.sum, unit=data.TimeUnit.month)
    assert len(re) == 1
    return str(re[0])


def graph_2_d2():
    """
    draw graph 1 d2
    Monthly cost
    :return: None
    """
    return str(cost.getMonthlyCost(data.dorm))


def graph_2_d3():
    """
    draw graph 1 d2
    Monthly cost per person
    :return: None
    """
    return str(cost.getMonthlyCost(data.dorm) / data.dorm_building_number_people)


def graph_2_a1():
    """
    draw graph 2 a1
    Daily energy consumption in this Month
    :return: None
    """
    tmp = data.getData(data.dorm, "Total Energy Consumption")
    # noinspection PyTypeChecker
    ran = [len(tmp) - data.TimeUnit.month.value, len(tmp)]
    re = data.washData(tmp, ran=ran, method=data.CompressMethods.average, unit=data.TimeUnit.day)
    assert len(re) == 30
    names = data.compressNames(data.dorm[1][0], ran=ran, unit=data.TimeUnit.day, convert_name=True)
    assert len(names) == 30
    return [str(names), str(re)]


def graph_2_b1():
    """
    draw graph 2 b1
    Daily energy consumption categories pie chart in this Month
    :return: None
    """
    re = "["
    re += data.getMonthlyData(data.dorm, "Steam")
    re += data.getMonthlyData(data.dorm, "Electricity")
    re += data.getMonthlyData(data.dorm, "Chilled Water")
    re += data.getMonthlyData(data.dorm, "Hot Water")
    re += data.getMonthlyData(data.dorm, "Natural Gas")
    return re[:-1] + "]"


def graph_2_b2():
    """
    draw graph 2 b2
    Monthly energy cost categories pie chart
    :return: None
    """
    re = "["
    re += cost.getMonthlyCostForPie(data.dorm, "Steam")
    re += cost.getMonthlyCostForPie(data.dorm, "Electricity")
    re += cost.getMonthlyCostForPie(data.dorm, "Chilled Water")
    re += cost.getMonthlyCostForPie(data.dorm, "Hot Water")
    re += cost.getMonthlyCostForPie(data.dorm, "Natural Gas")
    return re[:-1] + "]"
