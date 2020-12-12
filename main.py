import matplotlib.pyplot as plt
import numpy as np 
import Genethic
from tsp_data import Data


if __name__ == "__main__":
    data = Data()
    data = data.tsp_data
    
    starting_pop=10000
    iteration_count=500

    genethic = Genethic.GenethicTSP(data,starting_pop)
    optimum_value,general_value,node=genethic.Run(iteration_count)
    graph =[]
    for i in node:
        graph.append(data[int(i)])

    graph=np.array(graph)
    print(node)
    print(len(node))

    x,y = graph.T  

    fig, axs = plt.subplots(2)
    fig.suptitle('Berlin52 TSP Optimization Chart')    

    axs[0].set_title('Shortest Path')
    axs[0].plot(x, y, '-o')

    textstr='Optimum Value: ',int(optimum_value)
    axs[1].set(xlabel="Iteration Count",ylabel="Distance")
    axs[1].set_title('Distance by Iteriation Count')
    axs[1].text(0.69, 0.008, textstr, fontsize=10, transform=plt.gcf().transFigure)
    axs[1].plot(general_value)
    plt.show()
