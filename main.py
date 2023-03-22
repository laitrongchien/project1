import random 
import GeneticAlgorithm as GA 

import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt 

# parameters
numbers_of_generations = 200
population_size = 100
mutation_rate = 0.01
number_employees = 300
# number_employees = 2823
number_parents = 10

# df = pd.read_csv('sales_sample_data.csv', sep=',', encoding='latin1')
# value = df['SALES'].values
# print(value[0])

# profits = df['SALES'].values
# costs = df['QUANTITYORDERED'].values * df['PRICEEACH'].values * random.uniform(0.4, 0.6)

df = pd.read_csv('dataset.csv', sep=',', encoding='latin1')
profits = df['Profits Value']
costs = df['Expenses Value']
customers = []
contracts = []
times = []
for i in range(number_employees):
    customers.append(random.uniform(300, 500))
    contracts.append(random.uniform(90, 100))
    times.append(random.uniform(60, 90))

# profits = [1000, 950, 312, 700, 600, 428, 595, 834, 215, 164, 950, 930, 312, 650, 600, 428, 595, 834, 215, 164]
# customers = [400, 215, 338, 259, 102, 186, 172, 516, 280, 150, 275, 345, 268, 90, 126, 180, 634, 299, 308, 404]
# contracts = [90, 78, 96, 64, 32, 40, 60, 24, 86, 16, 100, 85, 25, 50, 36, 48, 70, 19, 92, 14]
# costs = [220, 105, 180, 84, 91, 50, 118, 30, 200, 45, 165, 54, 128, 67, 44, 288, 115, 158, 193, 230]
# times = [60, 100, 80, 90, 10, 50, 30, 40, 20, 70, 45, 69, 51, 98, 34, 84, 21, 99, 42, 58]


# profits = []
# costs = []
# customers = []
# contracts = []
# times = []
# for i in range (number_employees): 
#     profits.append(random.random() * 1000)
#     costs.append(random.random() * 250) 
#     customers.append(random.random() * 200)
#     contracts.append(random.random() * 50)
#     times.append(random.random() * 10)
  
# print(profits)
# print(costs)
    
# main function for genetic algorithm

best = []
def genetic_algorithm(profits_value, costs_value, customers_value, contracts_value, times_value, num_employees, pop_size, num_parents, mutation_prob, num_generations):
    # Solve the problem of selecting employees for a task in order to maximize profit and minimize cost using a genetic algorithm.
    # Generate initial population
    population = GA.generate_population(pop_size, num_employees, 0, 1)
    #print(population)
    for iteration in range(num_generations):
        # Calculate cost 
        cost = [GA.calculate_cost(chromosome, profits_value) for chromosome in population]
        # print(cost)
        best.append(max(cost))
        print('Generation: ' + str(iteration) + '-----> profits:' + str(max(cost)))
        
        # Calculate fitness of each chromosome
        fitness = [GA.calculate_fitness(chromosome, profits_value, costs_value, customers_value, contracts_value, times_value) for chromosome in population]
        # print(fitness)
       
        
        # Select the best-performing chromosomes as parents
        parents = GA.select_parents(population, fitness, num_parents)
        # Create new offspring by combining the genes of the parents
        offspring = GA.crossover(parents, pop_size - num_parents)
        # Randomly change the value of some genes in the offspring
        offspring = GA.mutation(offspring, mutation_prob, 0, 1)
        population = offspring
        # print(population)
    
    print('Best profits: ' + str(max(best)))  

def draw_profit_generations(y_list):
    x_list = np.arange(1, len(y_list)+1) 

    plt.plot(x_list, y_list)

    plt.title("Profit value through Generations")
    plt.xlabel("Generations")
    plt.ylabel("Profit Value")

    plt.show()
    
genetic_algorithm(profits, costs, customers, contracts, times, number_employees, population_size, number_parents, mutation_rate, numbers_of_generations)

draw_profit_generations(best)
