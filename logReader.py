import logParser
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons


def plotLogData(data):

    graphs = []

    print(data)
    flip = True
    fig2 = plt.figure(constrained_layout=True)
    spec2 = gridspec.GridSpec(ncols=3, nrows=3, figure=fig2)
    # f2_ax1 = fig2.add_subplot(spec2[0, 0])
    # f2_ax1.plot([0,1,2,3])
    # plt.xlabel("Time")

    for col in range(3):
        for row in range(2):
            graphs.append(fig2.add_subplot(spec2[col, row]))

    """ graphs.append(fig2.add_subplot(spec2[0, 0]))
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    graphs[0].plot([0,1,2,3])
    graphs.append(fig2.add_subplot(spec2[0, 1]))
    plt.xlabel("Time")
    plt.ylabel("Angle")
    graphs[1].plot(data['SWLF']['timestamps'], data['SWLF']['data']['angle'])
    graphs.append(fig2.add_subplot(spec2[1, 0]))
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    graphs[2].plot(data['SWLF']['timestamps'], data['SWLF']['data']['voltage'])

    graphs.append(fig2.add_subplot(spec2[1, 1]))
    plt.xlabel("Time")
    plt.ylabel("Angle")
    graphs[3].plot(data['SWRF']['timestamps'], data['SWRF']['data']['angle'])    
    graphs.append(fig2.add_subplot(spec2[2, 0]))
    plt.xlabel("Time")
    plt.ylabel("Rotation")
    graphs[4].plot(data['SWRF']['timestamps'], data['SWRF']['data']['rot'])

    graphs.append(fig2.add_subplot(spec2[2, 1]))
    plt.xlabel("Time")
    plt.ylabel("Speed")
    graphs[5].plot(data['Intake']['timestamps'], data['Intake']['data']['speed'])    """



    axcolor = 'red'
    rax = plt.axes([0.8, 0.1, 0.15, 0.15], facecolor=axcolor)
    radio1 = RadioButtons(rax,('SWLF', 'SWRF', 'Intake'))

    def plot(plotData, label):
        keyHeader = plotData[label]['header']
        keyData = plotData[label]['data']
        for graph in graphs:
            graph.clear()
        for i in range(min(len(keyHeader), 6)):
            iHeader = keyHeader[i]
            iData = keyData[iHeader]
            print(iData)
            graphs[i].plot(plotData[label]['timestamps'], iData)
            graphs[i].set_xlabel('Time')
            graphs[i].set_ylabel(iHeader)

    

        # for i, key in enumerate(keyHeader):
            

        


    def func(label):
        print(label)
        plot(data, label)
        print('done')
        plt.show()
        # gdict = {'SWLF': 1, 'SWRF': 2, 'Intake': 3}

        # if gdict[label] == 1:
        #     plt.clf()
        #    # plt.close()
        #     f2_ax1.plot(data['SWLF']['timestamps'], data['SWLF']['data']['velocity'])
        #     f2_ax2.plot(data['SWLF']['timestamps'], data['SWLF']['data']['angle'])
        #     f2_ax3.plot(data['SWLF']['timestamps'], data['SWLF']['data']['voltage'])
        #     #plt.draw()
        #     plt.show()
        # if gdict[label] == 2:
        #     plt.clf()
        #     #plt.close()
        #     f2_ax4.plot(data['SWRF']['timestamps'], data['SWRF']['data']['angle'])  
        #     f2_ax5.plot(data['SWRF']['timestamps'], data['SWRF']['data']['rot'])
        #     #plt.draw()
        #     plt.show()
 
        # if gdict[label] == 3:
        #     plt.clf()
        #     #plt.close()
        #     f2_ax6.plot(data['Intake']['timestamps'], data['Intake']['data']['speed']) 
        #     #plt.draw()
        #     plt.show()
    radio1.on_clicked(func)
    plot(data, 'SWLF')
    plt.show()
    

    

        

    

    



nameData = logParser.parseLogFile('testLog.data')
plotLogData(nameData)
