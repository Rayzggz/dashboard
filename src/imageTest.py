from matplotlib import pyplot as plt


def draw_bar(x: list, y: list):
    """
    Draw bar chart
    :param x: x axis
    :param y: y axis
    :return: None
    """
    plt.bar(x, y)
    plt.show()
