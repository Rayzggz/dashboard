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
    """
    post process the data
    :param dataF:
    :return:
    """
    return '{:,}'.format(round(dataF, data.round_num))


def nullCheck4Bar():
    """
    if you get the bar failed because get null from washData, use this and return 0 to ensure the program can run
    :return:
    """
    print("ERR: null")
    return ["[0]", "[0]"]


def nullCheck4Text():
    """
    if you get the text failed because get null from washData, use this and return '0' to ensure the program can run
    :return:
    """
    print("Err: null")
    return "0"


def err(text: str):
    """
    print error out, user can self-define this one
    :param text: output text
    :return:
    """
    print("Err: " + text)
