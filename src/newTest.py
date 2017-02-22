import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def scatter_plot_with_correlation_line(x, y, graph_filepath):
    '''
    http://stackoverflow.com/a/34571821/395857
    x does not have to be ordered.
    '''
    # Scatter plot

    plt.scatter(x, y)

    # Add correlation line
    axes = plt.gca()
    m, b = np.polyfit(x, y, 1)
    X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
    plt.plot(X_plot, m*X_plot + b, '-')
    plt.show()
    # Save figure
    # plt.savefig(graph_filepath, dpi=300, format='png', bbox_inches='tight')

def main():
    # Data

    # Plot
    indata = pd.read_csv('/Users/Pagliacci/Desktop/simu.csv', index_col=0)
    indata['error'] = np.log(np.log(indata['error']))
    indata = indata[indata['error'] != -np.inf]
    x = indata['z']
    y = indata['error']

    scatter_plot_with_correlation_line(x, y, 'scatter_plot.png')

if __name__ == "__main__":
    main()
    #cProfile.run('main()') # if you want to do some profiling