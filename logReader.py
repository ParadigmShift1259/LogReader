import logParser
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plotLogData(data):
    fig2 = plt.figure(constrained_layout=True)
    spec2 = gridspec.GridSpec(ncols=2, nrows=3, figure=fig2)
    f2_ax1 = fig2.add_subplot(spec2[0, 0])
    f2_ax1.plot([0,1,2,3])
    f2_ax2 = fig2.add_subplot(spec2[0, 1])
    
    f2_ax3 = fig2.add_subplot(spec2[1, 0])
    f2_ax4 = fig2.add_subplot(spec2[1, 1])
    fig2.add_subplot(spec2[2,0])
    plt.show()


nameData = logParser.parseLogFile('testLog.data')
plotLogData(nameData)
