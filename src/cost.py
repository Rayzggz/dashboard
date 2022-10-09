from src.data import *

price = {
    "Electricity": {"unit": 1 / 3.412, "2018": 0.0857, "2019": 0.0949, "2020": 0.0996, "2021": 0.1041, "2022": 0.1079},
    "Steam": {"unit": 1 / 1194, "2018": 17.4151, "2019": 20.0246, "2020": 21.0258, "2021": 21.9720, "2022": 27.0192},
    "Hot Water": {"unit": 1 / 100, "2018": 7.0091, "2019": 7.2778, "2020": 7.6417, "2021": 7.9856, "2022": 8.9128},
    "Chilled Water": {"unit": 1 / 1.2008, "2018": 0.2556, "2019": 0.3018, "2020": 0.3169, "2021": 0.3312,
                      "2022": 0.4041},
    "Natural Gas": {"unit": 1 / 1034, "2018": 7.4512, "2019": 8.3064, "2020": 8.7217, "2021": 9.1142, "2022": 11.3539}}


def getDailyCostForPie(target_data: list, tag: str, dayRevIndex: int):
    """

    :param target_data:
    :param tag:
    :param dayRevIndex: 0 represent today, 1 represent yesterday
    :return:
    """
    re = 0
    prefix = ["PlaceHolder", "Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    assert tag in prefix
    index = prefix.index(tag)
    tmp = washData(target_data[1][index],
                   [len(target_data[1][0]) - 24 * (dayRevIndex + 1), len(target_data[1][0]) - 24 * dayRevIndex],
                   CompressMethods.sum, TimeUnit.day)
    assert len(tmp) == 1
    year = (current_date + datetime.timedelta(days=-dayRevIndex)).year.__str__()
    return "{value: " + str(
        tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]) + ", name:'" + tag + "'},"


def getDailyCost(target_data: list, dayRevIndex: int):
    """

    :param target_data:
    :param dayRevIndex: 0 represent today, 1 represent yesterday
    :return:
    """
    re = 0
    prefix = ["PlaceHolder", "Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    for label in target_data[0]:
        index = -1
        for a in range(0, len(prefix)):
            if prefix[a] in label:
                index = a
                break
        if index == -1:
            continue
        # noinspection PyTypeChecker
        tmp = washData(target_data[1][index], [len(target_data[1][0]) - TimeUnit.day.value * (dayRevIndex + 1),
                                               len(target_data[1][0]) - TimeUnit.day.value * dayRevIndex],
                       CompressMethods.sum, TimeUnit.day)
        assert len(tmp) == 1
        year = (current_date + datetime.timedelta(days=-dayRevIndex)).year.__str__()
        re += tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]
    return re


def getMonthlyCost(target_data: list, monthRevIndex: int = 0):
    """
    Get Monthly Cost
    :param monthRevIndex: How many months before
    :param target_data:
    :return:
    """
    re = 0
    prefix = ["PlaceHolder", "Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    for label in target_data[0]:
        index = -1
        for a in range(0, len(prefix)):
            if prefix[a] in label:
                index = a
                break
        if index == -1:
            continue
        # noinspection PyTypeChecker
        tmp = washData(target_data[1][index], [len(target_data[1][0]) - TimeUnit.day.value * 30 * (monthRevIndex + 1),
                                               len(target_data[1][0]) - TimeUnit.day.value * 30 * monthRevIndex],
                       CompressMethods.sum, TimeUnit.month)
        if tmp == [-1]:
            uilts.err("washData return -1, getMonthlyCost," + str(monthRevIndex))
            continue
        assert len(tmp) == 1
        year = (current_date + datetime.timedelta(days=-30)).year.__str__()
        re += tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]
    return re


def getMonthlyCostForPie(target_data: list, tag: str):
    """
    Get Monthly Cost
    :param tag:
    :param target_data:
    :return:
    """
    re = 0
    prefix = ["PlaceHolder", "Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    assert tag in prefix
    index = prefix.index(tag)
    # noinspection PyTypeChecker
    tmp = washData(target_data[1][index], [len(target_data[1][0]) - TimeUnit.month.value, len(target_data[1][0])],
                   CompressMethods.sum, TimeUnit.month)
    if tmp == [-1]:
        uilts.err("washData return -1, getMonthlyCostForPie" + tag)
        return "{value:0, name:'" + tag + "'},"
    assert len(tmp) == 1
    year = (current_date + datetime.timedelta(days=-30)).year.__str__()
    return "{value: " + str(
        tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]) + ", name:'" + tag + "'},"

def getMonthlyCostForCategory(target_data: list, tag: str):
    """
    Get Monthly Cost
    :param tag:
    :param target_data:
    :return:
    """
    re = 0
    prefix = ["PlaceHolder", "Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    assert tag in prefix
    index = prefix.index(tag)
    # noinspection PyTypeChecker
    tmp = washData(target_data[1][index], [len(target_data[1][0]) - TimeUnit.month.value, len(target_data[1][0])],
                   CompressMethods.sum, TimeUnit.month)
    if tmp == [-1]:
        uilts.err("washData return -1, getMonthlyCostForPie" + tag)
        return "{value:0, name:'" + tag + "'},"
    assert len(tmp) == 1
    year = (current_date + datetime.timedelta(days=-30)).year.__str__()
    return tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]


def getYearlyCost(target_data: list):
    """
    Get Yearly Cost
    :param target_data:
    :return:
    """
    re = 0
    prefix = ["PlaceHolder", "Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    for label in target_data[0]:
        index = -1
        for a in range(0, len(prefix)):
            if prefix[a] in label:
                index = a
                break
        if index == -1:
            continue
        # noinspection PyTypeChecker
        tmp = washData(target_data[1][index], [len(target_data[1][0]) - TimeUnit.year.value, len(target_data[1][0])],
                       CompressMethods.sum, TimeUnit.year)
        if tmp == [-1]:
            uilts.err("washData return -1, getYearlyCost")
            continue
        assert len(tmp) == 1
        year = (current_date + datetime.timedelta(days=-365)).year.__str__()
        re += tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]
    return re


def getYearlyCostForPie(target_data: list, tag: str):
    """
    Get Yearly Cost
    :param tag:
    :param target_data:
    :return:
    """
    re = 0
    prefix = ["PlaceHolder", "Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    assert tag in prefix
    index = prefix.index(tag)
    # noinspection PyTypeChecker
    tmp = washData(target_data[1][index], [len(target_data[1][0]) - TimeUnit.year.value, len(target_data[1][0])],
                   CompressMethods.sum, TimeUnit.year)
    if tmp == [-1]:
        uilts.err("washData return -1, getYearlyCostForPie," + tag)
        return "{value:0, name:'" + tag + "'},"
    assert len(tmp) == 1
    year = (current_date + datetime.timedelta(days=-365)).year.__str__()
    return "{value: " + str(
        tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]) + ", name:'" + tag + "'},"
