from enum import Enum
import statistics

import pandas as pd
import numpy as np

dorm_building_name = "Smith-Steeb Hall"
non_dorm_building_name = "Thompson, William Oxley, Memorial Library"
weather_prefix_name = "Ohio State University"


class TimeUnit(Enum):
    hour = 1
    day = 24
    year = 24 * 365


class CompressMethods(Enum):
    average = 1
    median = 2
    sum = 3


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
    :return: one value that represent the data list
    """
    tmp = [a for a in data if a > -1]
    tmp = processNaN(tmp)
    assert len([0 for a in data if np.isnan(a)]) == 0
    if method == CompressMethods.average:
        return statistics.mean(tmp)
    elif method == CompressMethods.median:
        return statistics.median(tmp)
    elif method == CompressMethods.sum:
        return sum(tmp)
    else:
        print("err: compressData out")
        raise Exception()


def compressNames(names: list, unit: TimeUnit):
    tmp = names.copy()
    tmp.extend([-1 for _ in range(0, len(names) % unit.value())])
    re = []
    for i in range(0, len(tmp), step=unit.value()):
        if unit == TimeUnit.hour:
            re.extend(names[i])
        elif unit == TimeUnit.day:
            re.extend(str(names[i]).split("T")[0])
        elif unit == TimeUnit.year:
            re.extend(str(names[i])[:4])
        else:
            raise Exception("TimeUnit out")
    return re


def washData(data: list, ran=None, method: CompressMethods = CompressMethods.average,
             unit: TimeUnit = TimeUnit.day):
    """
    change the data unit from 1 hours to <unit> hours
    :param ran: range of data
    :param data: the data list
    :param method: the method used to compress
    :param unit: the time unit of data
    :return: data list after washing, if the data list is invalid, it should return [-1]
    """
    if ran is None:
        ran = [-1, -1]
    assert len(data) > 0
    assert len(ran) == 2
    null_num = len([a for a in data if np.isnan(a)])
    if null_num < len(data) / 2:
        # invalid data
        return [-1]
    tmp = data.copy()[ran[0]:ran[1]]
    tmp.extend([-1 for _ in range(0, len(data) % unit.value())])
    re = []
    for i in range(0, len(tmp), step=unit.value()):
        # wash data
        re.extend(compressData(tmp[i:i + unit.value()], method))
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
    re = [[], [value["Series Name"].tolist()]]
    for a in range(0, len(names)):
        if names[a][0:len(prefix)] == prefix:
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
    print(dorm_data[0])
    return dorm_data, non_dorm_data, _weather


dorm, non_dorm, weather = readData()
