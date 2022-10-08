import pandas

dorm_building_name = "Smith-Steeb Hall"
non_dorm_building_name = "Thompson, William Oxley, Memorial Library"


def parseData(names, value, name):
    # re is names add value
    re = [[], [value["Series Name"].tolist()]]
    for a in range(0, len(names)):
        if names[a][0:len(name)] == name:
            re[0].append(str(names[a]).split(' - ')[1])
            re[1].append(value[names[a]].tolist())
    return re


def readData():
    """

    :return: dorm_data, non_dorm_data, weather - 2D list, first one is name timeStamp, second one is data, which is a nD list, and inside data, the first one is names, the remaining is value, the len of remaining should equal to len of names.
    """
    global dorm_building_name, non_dorm_building_name
    dorm = pandas.read_csv('src/data/dorm_buildings.csv', delimiter=',')
    non_dorm = pandas.read_csv('src/data/non-dorm_buildings.csv', delimiter=',')
    weather = pandas.read_csv('src/data/weather_data.csv', delimiter=',')
    dorm_data = parseData(dorm.columns, dorm, dorm_building_name)
    non_dorm_data = parseData(non_dorm.columns, non_dorm, non_dorm_building_name)
    weather = parseData(weather.columns, weather, "Ohio State University")
    return dorm_data, non_dorm_data, weather
