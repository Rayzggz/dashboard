import datetime

from src.data import *

current_date = datetime.datetime(2022, 10, 6)
price = {
    "Electricity": {
        "unit": 3.412,
        "2018": 0.0857,
        "2019": 0.0949,
        "2020": 0.0996,
        "2021": 0.1041,
        "2022": 0.1079
    },
    "Steam": {
        "unit": 1.154,
        "2018": 17.4151,
        "2019": 20.0246,
        "2020": 21.0258,
        "2021": 21.9720,
        "2022": 27.0192
    },
    "Hot Water": {
        "unit": 100,
        "2018": 7.0091,
        "2019": 7.2778,
        "2020": 7.6417,
        "2021": 7.9856,
        "2022": 8.9128
    },
    "Chilled Water": {
        "unit": 1.03073,
        "2018": 0.2556,
        "2019": 0.3018,
        "2020": 0.3169,
        "2021": 0.3312,
        "2022": 0.4041
    },
    "Natural Gas": {
        "unit": 0.085902,
        "2018": 7.4512,
        "2019": 8.3064,
        "2020": 8.7217,
        "2021": 9.1142,
        "2022": 11.3539
    }
}


def getDailyCost(target_data: list, dayRevIndex: int):
    re = 0
    prefix = ["Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]
    for label in target_data[0]:
        index = -1
        for a in range(0, len(prefix)):
            if prefix[a] in label:
                index = a
                break
        if index == -1:
            continue
        tmp = washData(target_data, [len(target_data) - 24 * dayRevIndex, len(target_data) - 24 * (dayRevIndex - 1)],
                       CompressMethods.sum,
                       TimeUnit.day)
        assert len(tmp) == 1
        year = (current_date + datetime.timedelta(days=-dayRevIndex)).year.__str__()
        re += tmp[0] * price[prefix[index]][year] * price[prefix[index]]["unit"]
    return re
