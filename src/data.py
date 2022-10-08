from enum import Enum
import statistics

import pandas as pd
import numpy as np

dorm_building_name = "Smith-Steeb Hall"
non_dorm_building_name = "Thompson, William Oxley, Memorial Library"
weather_prefix_name = "Ohio State University"


class CompressMethods(Enum):
    average = 1
    median = 2


def processNaN(data: list):
    """
    fill NaN value in data list
    :param data: data list
    :return: data list after filled
    """
    re = data[:]
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
    else:
        print("err: compressData out")
        raise Exception()


def washData(data: list, method: CompressMethods = CompressMethods.average, unit: int = 1):
    """
    change the data unit from 1 hours to <unit> hours
    :param data: the data list
    :param method: the method used to compress
    :param unit: the time unit of data
    :return: data list after washing, if the data list is invalid, it should return [-1]
    """
    assert unit > 0
    assert len(data) > 0
    null_num = len([a for a in data if np.isnan(a)])
    if null_num < len(data) / 2:
        # invalid data
        return [-1]
    tmp = data[:]
    tmp.extend([-1 for _ in range(0, len(data) % unit)])
    re = []
    for i in range(0, len(tmp), step=unit):
        # wash data
        re.extend(compressData(tmp[i:i + unit], method))
    return re


def parseData(names: list, value: dict, prefix: str):
    """

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


def readData():
    """
    read data from csv files
    eg:
    last 24 hours data for first name dorm[1][1][-24:]
    last 24 hours date name for first name dorm[1][0][-24:]
    :return: dorm_data, non_dorm_data, weather - 2D list, first one is name timeStamp, second one is data, which is a nD list, and inside data, the first one is names, the remaining is value, the len of remaining should equal to len of names.
    """
    global dorm_building_name, non_dorm_building_name
    dorm = pd.read_csv('src/data/dorm_buildings.csv', delimiter=',')
    non_dorm = pd.read_csv('src/data/non-dorm_buildings.csv', delimiter=',')
    weather = pd.read_csv('src/data/weather_data.csv', delimiter=',')
    dorm_data = parseData(dorm.columns, dorm, dorm_building_name)
    non_dorm_data = parseData(non_dorm.columns, non_dorm, non_dorm_building_name)
    weather = parseData(weather.columns, weather, weather_prefix_name)
    return dorm_data, non_dorm_data, weather
