import numpy as np

class Data():
    tsp_data=np.array([])

    def __init__(self):
        # Open input file
        infile = open('berlin52.tsp', 'r')

        # Read instance header
        Name = infile.readline().strip().split()[1] # NAME
        FileType = infile.readline().strip().split()[1] # TYPE
        Comment = infile.readline().strip().split()[1] # COMMENT
        Dimension = infile.readline().strip().split()[1] # DIMENSION
        EdgeWeightType = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
        infile.readline()

        # Read node list
        nodelist = []
        for i in range(0, int(Dimension)):
            x,y = infile.readline().strip().split()[1:]
            nodelist.append((int(float(x)), int(float(y))))

        # Close input file
        infile.close()
        
        
        self.tsp_data = nodelist
    

