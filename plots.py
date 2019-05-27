import matplotlib.pyplot as plt
import numpy as np # != p
from parameters import COLORS
import parameters

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Installation cost', 'Service cost', 'Parts cost'
sizes = [30000, 1590, 3216]


def plot_elevators(elevators, global_downtime):
    '''
    global_downtime: [1,1,1,0,0,0,1,1]
    '''

    global_downtime_journal = []
    _start = 0
    _end = 0

    for i in range(len(global_downtime)-1):
        if global_downtime[i] != global_downtime[i+1]:
            if global_downtime[i+1] == 1:
                _end = i+2
                global_downtime_journal.append([_start, _end])
            else:
                _start = i+2

    if _start > _end:
        global_downtime_journal.append([_start, parameters.LIFETIME_OF_ELEVATOR])

    
    y = 0
    plt.figure(num=None, figsize=[15, 5])

    for e in elevators:
        y+=1

        plt.text(-70, y, f'Elevator {y}', fontsize=15)

        for data in e.journal:
            plt.fill_between(data, y1=y-0.2, y2=y+0.2, color=parameters.COLORS[y])


    y+=1

    plt.fill_between([0, parameters.LIFETIME_OF_ELEVATOR], y1=y-0.2, y2=y+0.2, color='white')


    plt.text(-70, y, f'Downtime', fontsize=15)

    for data in global_downtime_journal:
        plt.fill_between(data, y1=y-0.2, y2=y+0.2, color='red')

    #plt.axes().get_yaxis().set_visible(False)
    plt.axes().get_yaxis().set_ticks([])

    plt.xlabel('Time [days]')
    plt.ylabel('Uptime of a given elevator')
    plt.show()




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



if __name__ == '__main__':

    fig = plt.figure()
    x = np.arange(10)
    y = 2.5 * np.sin(x / 20 * np.pi)
    yerr = np.linspace(0.05, 0.2, 10)

    plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')

    plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')

    plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
                label='uplims=True, lolims=True')

    upperlimits = [True, False] * 5
    lowerlimits = [False, True] * 5
    plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
                label='subsets of uplims and lolims')

    plt.legend(loc='lower right')
