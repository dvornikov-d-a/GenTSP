import random
from matrix import Matrix
from genetic import Genetic

matrix = Matrix()

genetic = Genetic(
    genotype_length=matrix.cities_count,
    gen_value_interval=(0, matrix.cities_count - 1),
    fitness_function=matrix.score,
    desired_fitness=1
)

genetic.fit()

print('Минимальный путь:', matrix.right_distance)
print('Правильный ответ:', matrix.right_cities)
print()
print('Лучший результат:', matrix.score(genetic.best))
print('Длина маршрута: ', matrix.path_len(genetic.best))
print('Лучший маршрут:', matrix.get_names(genetic.best))

