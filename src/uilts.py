from src import data


def name4hour(name: str):
    """
    get the hour of name
    :param name: name
    :return: hour
    """
    return int(name.split("T")[1].split(":")[0])


def name4day(name: str):
    """
    get the day of name
    :param name: name
    :return: day
    """
    return int(name.split("T")[0].split("-")[2])


def name4month(name: str):
    """
    get the month of name
    :param name: name
    :return: month
    """
    return int(name.split("T")[0].split("-")[1])


def name4year(name: str):
    """
    get the year of name
    :param name: name
    :return: year
    """
    return int(name.split("T")[0].split("-")[0])


def postProcess(dataF: float):
    return '{:,}'.format(round(dataF, data.round_num))
