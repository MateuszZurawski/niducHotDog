import matplotlib.pyplot as plt
import numpy as np # != p
from parameters import COLORS

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Installation cost', 'Service cost', 'Parts cost'
sizes = [30000, 1590, 3216]


def save_or_show(plt, save_to):
    if save_to:
        plt.savefig(save_to, dpi=220)
        print(f'saved {save_to}')
    else:
        plt.show()



def make_pie_plot(labels, sizes, save_to=None):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90, colors=COLORS)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    save_or_show(plt, save_to)


def make_line_plot(x, y, save_to=None):
    if x:
        plt.plot(x, y)
    else:
        plt.plot(y)
    
    save_or_show(plt, save_to)

# EXAMPLE
'''
make_line_plot(
    [1,2,3], [[3,2,1],
              [3.2,1.9,1.5],
              [3.1,2.2,1.2]]
)
'''


def make_stack_plot(x, y_series, labels, save_to=None):
    fig, ax = plt.subplots()
    plt.stackplot(x, y_series, labels=labels)
    ax.legend(loc='upper left')
    save_or_show(plt, save_to)


# EXAMPLE
'''
make_stack_plot(
    [1,2,3,4,5,6,7],
    [
        [3,1,6,3,7,8,2],
        [7,5,9,3,1,4,7],
        [9,8,7,6,5,4,3]
    ],
    ['Deficyt Bączka', 'Deficyt Marka', 'Deficyt Żurawia']
)

'''


# TODO
def make_table_plot():

    data = [[ 30000, 60000,  50000, 10000],
            [ 4000, 8000,  2000,  4000],
            [8000, 16000, 3000, 6000]]

    columns = ('1 cheap elevator', '2 cheap elevators', '1 pro elevator', '2 pro elevators')
    rows = ['Installation', 'Service costs', 'Repair costs']

    values = np.arange(0, 2500, 500)
    value_increment = 10

    # Get some pastel shades for the colors
    colors = COLORS #plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))

    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    cell_text.reverse()

    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                        rowLabels=rows,
                        rowColours=colors,
                        colLabels=columns,
                        loc='bottom')

    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)

    plt.ylabel("Loss in ${0}'s".format(value_increment))
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title('Loss by Disaster')

    plt.show()