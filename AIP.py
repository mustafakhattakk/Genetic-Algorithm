import random
import string

def generate_random_string(length):
 
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

def calculate_fitness(target, candidate):
   
    return sum(1 for t, c in zip(target, candidate) if t == c)

def select_parents(population, fitness_scores):

    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    parents = random.choices(population, probabilities, k=2)
    return parents[0], parents[1]

def crossover(parent1, parent2):
   
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(candidate, mutation_rate):
  
    mutated = ""
    for char in candidate:
        if random.random() < mutation_rate:
            mutated += random.choice(string.ascii_letters + string.digits + string.punctuation)
        else:
            mutated += char
    return mutated

def genetic_algorithm(target):
    population_size = 100
    mutation_rate = 0.05
    generations = 1000

    population = [generate_random_string(len(target)) for _ in range(population_size)]

    for generation in range(generations):
        fitness_scores = [calculate_fitness(target, candidate) for candidate in population]

        best_fitness = max(fitness_scores)
        best_index = fitness_scores.index(best_fitness)
        best_candidate = population[best_index]

        print(f"Generation {generation}: Best Candidate: {best_candidate}, Fitness Score: {best_fitness}")

        if target in population:
            print("Target found!")
            break

        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            mutated_child1 = mutate(child1, mutation_rate)
            mutated_child2 = mutate(child2, mutation_rate)
            new_population.extend([mutated_child1, mutated_child2])

        population = new_population

    else:
        print("Target not found in the given number of generations")

if __name__ == "__main__":
    target_string = "MustafaShahid"
    genetic_algorithm(target_string)
