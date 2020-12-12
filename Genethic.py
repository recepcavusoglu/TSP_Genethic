import numpy as np
import random as rand
import operator
import math

class GenethicTSP():
    
    def __init__(self,data,pop_size):
        self.population_rate=pop_size
        self.mydata = data
   
    def binary_search(self,arr, low, high, ele): 
        while low < high: 
            mid = (low + high) // 2
            if arr[mid] == ele: 
                return mid 
            elif arr[mid] > ele: 
                high = mid 
            else: 
                low = mid + 1
        return -1
    
    def get_Small(self,arr, asize, n): 
        copy_arr = arr.copy() 
        copy_arr.sort()
        abc =[]   
        for i in range(asize): 
            if self.binary_search(copy_arr, low = 0, high = n, ele = arr[i]) > -1: 
                abc.append(arr[i])
        return(abc)

    def Create_Population(self,p_data,p_chromosom_number):
        chromosomes=[]
        for i in range(p_chromosom_number):
            temp=[]
            for j in range(1,len(p_data)):
                temp.append((j,rand.random()))
            temp.append((0,0))
            temp.sort(key=lambda x: x[1])
            temp.append((0,0))
            temp = np.array(temp)
            chromosomes.append(temp.T[0])
        return chromosomes

    def Fitness(self,p_chromosomes):
        fitness = []
        for j in range(len(p_chromosomes)):
            distance =0
            for i in range(len(p_chromosomes[j])):
                index= int(p_chromosomes[j][i])
                if i==52:
                    break
                else:
                    next_index =int(p_chromosomes[j][i+1])
                x1=self.mydata[index][0]
                y1=self.mydata[index][1]
                x2=self.mydata[next_index][0]
                y2=self.mydata[next_index][1]
                distance += math.sqrt((x2-x1)**2+(y2-y1)**2)
            fitness.append(int(distance))
        
        return fitness

    def crossover(self,parent1,parent2):
        child=[]
        childP1=[0]
        childP2=[]
        genA = int(rand.uniform(0.02,0.99)*len(parent1))
        genB = int(rand.uniform(0.02,0.99)*len(parent1))
        startGen = min(genA,genB)
        endGen = max(genA,genB)
        for i in range(startGen,endGen):
            childP1.append(parent1[i])    
        childP2=[item for item in parent2 if item not in childP1]
        child=childP1+childP2
        child.append(0)
            
        return child

    def Election(self,p_Fitness,p_electionnumber):
        asize = len(p_Fitness) 
        smallest=self.get_Small(p_Fitness, asize, p_electionnumber)
        smallest.sort()
        abc=[]
        for i in smallest:
            abc.append(p_Fitness.index(i))
        return abc

    def Create_Bests(self,p_elected,p_population):
        new_bests=[]
        for i in range(len(p_elected)):
            new_bests.append(p_population[p_elected[i]])
        return new_bests

    def Mutation(self,p_population,p_mutation_number):
        selection=[]
        for i in range(len(p_population)):
            selection.append((rand.random(),p_population[i]))
        selection.sort(key=lambda x: x[0])
        new_selection = selection[:p_mutation_number]   
        dumm=[]
        for i in new_selection:
            dumm.append(i[1])
        mutated=[]
        for i in range(len(new_selection)):
            mutation_count = rand.randint(3,20)
            mutation_part=rand.randint(1,52-mutation_count)
            partition=[]
            partition = dumm[i][mutation_part:mutation_part+mutation_count]
            partition=partition[::-1]
            start_point=mutation_part
            end_point=mutation_part+mutation_count
            dummy=[]
            for j in range(len(dumm[i])):
                if j<end_point and j>=start_point:
                    dummy.append(partition[z])
                    z+=1
                else:
                    z=0
                    dummy.append(dumm[i][j])
            mutated.append(dummy)              
        return mutated
    
    def Breed(self, p_bests):
        new_childs=[]
        for i in range(0,len(p_bests)-1,2):
            new_childs.append(self.crossover(p_bests[i],p_bests[i+1]))
        return new_childs

    def check_duplicate(self,p_list):
        hata=False
        for i in p_list:
            if len(i[0:len(i)-1]) == len(set(i[0:len(i)-1])):
                pass
            else:
                hata =True
        return hata

    def Run(self,p_iteration_count):
        population = self.Create_Population(self.mydata,self.population_rate)    
        fitness = self.Fitness(population)    
        general_value= []
        general_value.append(min(fitness))
        for i in range(p_iteration_count):
            elected = self.Election(fitness,400)

            new_bests = self.Create_Bests(elected,population)

            new_childs= self.Breed(new_bests)          

            new_rands = self.Create_Population(self.mydata,50)

            new_mutations = self.Mutation(population,100)

            new_bests_mutated = self.Mutation(new_bests,100)

            new_childs_mutated = self.Mutation(new_childs,100)
            population = new_bests+new_childs+new_rands+new_mutations+new_bests_mutated+new_childs_mutated

            fitness = self.Fitness(population)
            general_value.append(min(fitness))
            print(i,". Iteration Smallest Distance: ",min(fitness))
            indis = fitness.index(min(fitness))         
            

        optimum_value=min(general_value)
        print("Optimum Value: ",optimum_value)
        return optimum_value,general_value,population[indis]

        