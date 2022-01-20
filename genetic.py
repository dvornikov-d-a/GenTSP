import random
import copy


class Genetic:
    def __init__(self, genotype_length, gen_value_interval, fitness_function, desired_fitness,
                 population_size=1000, survivals_fraction=0.8, mutation_chance=0.05,
                 max_step=10000):
        self._genotype_length = genotype_length
        self._gen_value_interval = gen_value_interval
        self._fitness_function = fitness_function
        self._desired_fitness = desired_fitness
        self._population_size = population_size
        self._survivals_count = int(survivals_fraction * self._population_size)
        self._reproduction_size = self._population_size - self._survivals_count
        self._odd_miscarriage = True if self._reproduction_size % 2 != 0 else False
        self._doubles_number = int((self._reproduction_size + int(self._odd_miscarriage)) / 2)
        self._sep_index = int(self._genotype_length / 2)
        self._mutation_count = int(mutation_chance * self._population_size)
        self._population = []
        self._max_step = max_step
        self._best = {
            'genotype': tuple([-1 for i in range(self._genotype_length)]),
            'fitness': -1
        }

    @property
    def best(self):
        return self._best['genotype']

    def fit(self):
        self._generate_start_population()
        step = 0
        while self._best['fitness'] < self._desired_fitness and step < self._max_step:
            self._select()
            self._reproduce()
            self._mutate()
            self._check_fitness()
            step += 1

    def _check_fitness(self):
        for individual in self._population:
            if individual['fitness'] > self._best['fitness']:
                self._best['genotype'] = individual['genotype']
                self._best['fitness'] = individual['fitness']

    def _generate_start_population(self):
        self._population.clear()
        for i in range(self._population_size):
            genotype = [j for j in range(self._genotype_length)]
            random.shuffle(genotype)
            individual = {
                'genotype': tuple(genotype),
                'fitness': self._fitness_function(tuple(genotype))
            }
            self._population.append(individual)

    # Турнирная селекция (отбор)
    def _select(self):
        olds = copy.deepcopy(self._population)
        olds.sort(key=lambda x: x['fitness'])
        self._population.clear()
        for i in range(self._survivals_count):
            self._population.append(olds.pop())
            # random.shuffle(olds)
            # one, two = olds.pop(), olds.pop()
            # if one['fitness'] > two['fitness']:
            #     self._population.append(one)
            #     olds.append(two)
            # else:
            #     self._population.append(two)
            #     olds.append(one)

    def _cross(self, two_genotypes, main_parent_index, secondary_parent_index):
        genotype = []
        for gen in two_genotypes[main_parent_index][:self._sep_index]:
            genotype.append(gen)
        for gen in two_genotypes[secondary_parent_index][:]:
            if gen not in genotype:
                genotype.append(gen)
        return tuple(genotype)

    def _reproduce(self):
        for i in range(self._doubles_number):
            # Стохастическое размножение
            parents_genotypes = [parent['genotype'] for parent in random.choices(self._population, k=2)]
            for first in (True, False):
                genotype = self._cross(parents_genotypes, int(not first), int(first))
                child = {
                    'genotype': genotype,
                    'fitness': self._fitness_function(genotype)
                }
                self._population.append(child)
        if self._odd_miscarriage:
            self._population.pop()

    def _swap(self, mutant_index):
        gen_index = random.randint(1, self._genotype_length - 1)
        genotype = list(self._population[mutant_index]['genotype'])
        tmp = genotype[gen_index - 1]
        genotype[gen_index - 1] = genotype[gen_index]
        genotype[gen_index] = tmp
        self._population[mutant_index]['genotype'] = genotype
        self._population[mutant_index]['fitness'] = self._fitness_function(genotype)

    def _mutate(self):
        for i in range(self._mutation_count):
            # Случайная мутация
            # mutant_index = random.randint(0, self._population_size - 1)

            # Мутация наименее приспособленных
            mutant_index = 0
            for j, individual in enumerate(self._population[1:]):
                if individual['fitness'] < self._population[mutant_index]['fitness']:
                    mutant_index = j
            self._swap(mutant_index)
