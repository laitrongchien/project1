import random 
import GeneticAlgorithm as GA 

import numpy as np  
import matplotlib.pyplot as plt 

# parameters
numbers_of_generations = 50
population_size = 100
mutation_rate = 0.01
number_employees = 10
number_parents = 10
profits = [1000, 950, 312, 700, 600, 428, 595, 834, 215, 164]
customers = [400, 215, 338, 259, 102, 186, 172, 516, 280, 150]
contracts = [90, 78, 96, 64, 32, 40, 60, 24, 86, 16]
costs = [220, 105, 180, 84, 91, 50, 118, 30, 200, 45]
times = [60, 100, 80, 90, 10, 50, 30, 40, 20, 70]

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
