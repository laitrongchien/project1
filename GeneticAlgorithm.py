import random
import numpy as np

def generate_population(size, length, lower_bound, upper_bound):
    # Khởi tạo dân số bẵng chuỗi bit nhị phân với mỗi bit đại diện cho giải pháp chọn nhân viên cho KPI
    population = []
    for i in range(size):
        chromosome = [random.randint(lower_bound, upper_bound) for j in range(length)]
        population.append(chromosome)
    return population

def calculate_cost(chromosome, profits):
    profit = 0
    for i, gene in enumerate(chromosome):
        profit += gene * profits[i]
    return profit

def calculate_fitness(chromosome, profits, costs, customers, contracts, times):
    # Tính toán hàm fitness 
    profit = 0 # Khởi tạo profit = 0
    cost = 0 # Khởi tạo cost = 0
    customer = 0 
    contract = 0
    time = 0
    
    for i, gene in enumerate(chromosome):
        profit += gene * profits[i]
        cost += gene * costs[i]
        customer += gene * customers[i]
        contract += gene * contracts[i]
        time += gene * times[i]
    # fitness = profit - cost
    fitness = profit * 10 + customer + contract - cost * 8 - time
    return fitness

# print('2')
# print(calculate_fitness([1,0,0,1], [2,3,4,5], [5,6,7,8]))

def select_parents(population, fitness, num_parents):
    # Chọn cá thể có giá trị hàm fitness cao nhất làm cha mẹ 
    fitness = np.array(fitness)
    parents = []
    for i in range(num_parents):
        parent_idx = np.argmax(fitness)
        parents.append(population[parent_idx])
        fitness[parent_idx] = -1
    return parents

def crossover(parents, offspring_size):
    # Tạo ra con mới bằng các trao đổi chéo các gen trong NST cha mẹ 
    offspring = []
    for i in range(offspring_size):
        crossover_point = random.randint(0, len(parents) - 1)
        parent1 = parents[i % len(parents)]
        parent2 = parents[(i + 1) % len(parents)]
        offspring.append(parent1[:crossover_point] + parent2[crossover_point:])
    return offspring

def mutation(offspring, mutation_prob, lower_bound, upper_bound):
    # Đột biến gen trong NST 
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if random.uniform(0, 1) < mutation_prob:
                offspring[i][j] = random.randint(lower_bound, upper_bound)
    return offspring
    

# Find the best chromosome of the generation based on the profits 
# def find_best_profit(generation):
#     profit = 0
#     profits = []
#     total = []
#     for chromosome in generation:
#         for i, gene in enumerate(chromosome):
#             profit += profits[i] * gene 
#             total.append(profit)
#     best = total[0]
#     for n in range(1, len(generation)): 
#         if best < total[n]: best = total[n]    
#     return best



