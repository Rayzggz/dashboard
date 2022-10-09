from enum import Enum
import statistics
from src import uilts
import pandas as pd
import numpy as np

dorm_building_name = "Smith-Steeb Hall"
non_dorm_building_name = "Thompson, William Oxley, Memorial Library"
weather_prefix_name = "Ohio State University"


class TimeUnit(Enum):
    hour = 1
    day = 24
    year = 24 * 365

    def __int__(self):
        return self.value


class CompressMethods(Enum):
    average = 1
    median = 2
    sum = 3

    def __int__(self):
        return self.value


def processNaN(data: list):
    """
    fill NaN value in data list
    :param data: data list
    :return: data list after filled
    """
    re = data.copy()
    for i in range(0, len(data)):
        if np.isnan(data[i]):
            # if Nan is first item
            if i == 0:
                if i + 1 < len(data) and not np.isnan(data[i + 1]):
                    # use next item fill
                    re[i] = data[i + 1]
                else:
                    # use zero fill
                    re[i] = 0
            # if NaN is the last item
            elif i == len(data) - 1:
                # use previous one fill
                re[i] = re[i - 1]
            # if NaN is in mid
            else:
                # if next isn't nan
                if not np.isnan(data[i + 1]):
                    # use median fill
                    re[i] = statistics.median([data[i - 1], data[i + 1]])
                # if next is nan
                else:
                    # use zero fill
                    re[i] = 0
    return re


def compressData(data: list, method: CompressMethods):
    """
    Compress data to one value
    :param data: the list need to compress
    :param method: the method used to compress
    :return: one value that represent the data list, float
    """
    tmp = [a for a in data if a > -1]
    tmp = processNaN(tmp)
    assert len([0 for a in data if np.isnan(a)]) == 0
    if len(data) == 1:
        return data[0]
    if method == CompressMethods.average:
        return statistics.mean(tmp)
    elif method == CompressMethods.median:
        return statistics.median(tmp)
    elif method == CompressMethods.sum:
        return sum(tmp)
    else:
        raise Exception("err: compressData out")


def compressNames(names: list, ran=None, unit: TimeUnit = TimeUnit.hour, convert_name: bool = False):
    """
    compress names
    :param convert_name: auto convert name
    :param ran: range of names
    :param names: names list
    :param unit: time unit
    :return: names list after compress
    """
    if ran is None:
        ran = [0, len(names)]
    tmp = names.copy()[ran[0]:ran[1]]
    tmp.extend([-1 for _ in range(0, len(names) % unit.value)])
    re = []
    for i in range(0, len(tmp), unit.value):
        tmp = ""
        if unit == TimeUnit.hour:
            tmp = names[i]
            if convert_name:
                tmp = uilts.name4hour(tmp)
        elif unit == TimeUnit.day:
            tmp = str(names[i]).split("T")[0]
            if convert_name:
                tmp = uilts.name4day(tmp)
        elif unit == TimeUnit.year:
            tmp = str(names[i])[:4]
            if convert_name:
                tmp = uilts.name4year(tmp)
        else:
            raise Exception("TimeUnit out")
        re.append(tmp)
    return re


def washData(data: list, ran=None, method: CompressMethods = CompressMethods.average,
             unit: TimeUnit = TimeUnit.hour):
    """
    change the data unit from 1 hours to <unit> hours
    :param ran: range of data
    :param data: the data list
    :param method: the method used to compress
    :param unit: the time unit of data
    :return: data list after washing, if the data list is invalid, it should return [-1]
    """
    if ran is None:
        ran = [0, len(data)]
    assert len(data) > 0
    assert len(ran) == 2
    tmp = data.copy()[ran[0]:ran[1]]
    null_num = len([a for a in tmp if np.isnan(a)])
    if null_num > len(tmp) / 2:
        # invalid data
        return [-1]
    tmp.extend([-1 for _ in range(0, len(data) % unit.value)])
    re = []
    for i in range(0, len(tmp), unit.value):
        # wash data
        re.append(compressData(tmp[i:i + unit.value], method))
    return re


def parseData(names: list, value: dict, prefix: str):
    """
    parse data we needed from csv file(specific building)
    :param names: name list from DataFrame columns
    :param value: DataFrame
    :param prefix: data prefix
    :return: 2D list, first one is name timeStamp, second one is data, which is a nD list, and inside data, the first one is names, the remaining is value, the len of remaining should equal to len of names.
    """
    # re is names add value
    re = [["Series Name"], [value["Series Name"].tolist()]]
    for a in range(0, len(names)):
        if names[a][:len(prefix)] == prefix:
            re[0].append(str(names[a]).split(' - ')[1])
            re[1].append(value[names[a]].tolist())
    return re


def delSomeData(value: list):
    # delete 2017 content, because it starts in 1/1/2017 05
    re = []
    # 8760 hours in 2017
    for i in range(0, len(value)):
        re.append(value[i][8760 - 1 - 4:])
    return re


def readData():
    """
    read data from csv files
    eg:
    last 24 hours data for first name dorm[1][1][-24:]
    last 24 hours date name for first name dorm[1][0][-24:]
    :return: dorm_data, non_dorm_data, weather - 2D list, first one is name timeStamp, second one is data, which is a nD list, and inside data, the first one is names, the remaining is value, the len of remaining should equal to len of names.
    """
    global dorm_building_name, non_dorm_building_name
    _dorm = pd.read_csv('src/data/dorm_buildings.csv', delimiter=',')
    _non_dorm = pd.read_csv('src/data/non-dorm_buildings.csv', delimiter=',')
    _weather = pd.read_csv('src/data/weather_data.csv', delimiter=',')
    dorm_data = parseData(_dorm.columns, _dorm, dorm_building_name)
    dorm_data[1] = delSomeData(dorm_data[1])
    non_dorm_data = parseData(_non_dorm.columns, _non_dorm, non_dorm_building_name)
    non_dorm_data[1] = delSomeData(non_dorm_data[1])
    _weather = parseData(_weather.columns, _weather, weather_prefix_name)
    _weather[1] = delSomeData(_weather[1])
    return dorm_data, non_dorm_data, _weather


dorm, non_dorm, weather = readData()


def getData(data: list, prefix: str):
    """
    get data from 2D list
    :param data: 2D list
    :param prefix: name of data
    :return: data list
    """
    for i in range(0, len(data[0])):
        if data[0][i][:len(prefix)] == prefix:
            return data[1][i]
    raise Exception("prefix not found getData")


def getDailyData(dataList: list, tag: str):
    tmp = getData(dataList, tag)
    ran = [len(tmp) - 24, len(tmp)]
    re = washData(tmp, ran=ran, method=CompressMethods.sum, unit=TimeUnit.hour)
    if re != [-1]:
        names = compressNames(dataList[1][0], ran=ran, unit=TimeUnit.day, convert_name=True)
        assert len(names) == 1
        return "{value: " + str(re[0]) + ", name:'" + tag + "'},"
    return ""
