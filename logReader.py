import sys
import logParser
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons


def plotLogData(data):
    """
    Creates graphs for all recorded data headers, plots under individual key pages, changes between groupings of 6, 
    """
    graphs = []

    fig = plt.figure(constrained_layout=True)
    spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)

    for col in range(3):
        for row in range(2):
            graphs.append(fig.add_subplot(spec[col, row]))


    axcolor = 'red'
    rax = plt.axes([0.8, 0.2, 0.15, 0.15], facecolor=axcolor)
    radio1 = RadioButtons(rax, nameData.keys())

    listLabel = nameData.keys()
    label = list(listLabel)[0]
    group = 0

    def plot():
        keyHeader = nameData[label]['header']
        keyData = nameData[label]['data']
        for graph in graphs:
            graph.clear()
        for i in range(6):
            headerIndex = i + 6 * group
            if headerIndex >= len(keyHeader):
                break
            iHeader = keyHeader[headerIndex]
            iData = keyData[iHeader]
            graphs[i].plot(nameData[label]['timestamps'], iData)
            graphs[i].set_xlabel('Time')
            graphs[i].set_ylabel(iHeader)

    
    def next(event):
        nonlocal group
        group += 1
        plot()

    def prev(event):
        nonlocal group
        group = max(group - 1, 0)
        plot()

    axprev = plt.axes([0.75, 0.1, 0.1, 0.075])
    axnext = plt.axes([0.86, 0.1, 0.1, 0.075])

    bnext = Button(axnext, 'Next')
    bprev = Button(axprev, 'Previous')
    
    bnext.on_clicked(next)
    bprev.on_clicked(prev)

    def radioCallback(buttonSelection):
        nonlocal label, group
        group = 0
        label = buttonSelection
        plot()
        plt.show()
    
    radio1.on_clicked(radioCallback)
    plot()
    plt.show()
    
    

try:
    nameData = logParser.parseLogFile(sys.argv[1])
    plotLogData(nameData)
except:
    print('Error: Unable to access log file')

