import time
from matrix import Matrix
from genetic import Genetic

matrix = Matrix()

genetic = Genetic(
    genotype_length=matrix.cities_count,
    gen_value_interval=(0, matrix.cities_count - 1),
    fitness_function=matrix.score,
    desired_fitness=1
)

start_time = time.time()

genetic.fit()

finish_time = time.time()
calculations_time = finish_time - start_time
minutes, seconds = calculations_time // 60, int(calculations_time % 60)

with open('res.txt', 'w', encoding='utf-8') as f:
    f.write(f'Время вычислений: {minutes} min {seconds} sec\n')
    f.write(f'\n')
    f.write(f'Минимальная длина пути: {matrix.right_distance} km\n')
    f.write(f'Правильный ответ: {", ".join(matrix.right_cities)}\n')
    f.write(f'\n')
    f.write(f'Лучший результат: {matrix.score(genetic.best) * 100}%\n')
    f.write(f'Длина маршрута: {matrix.path_len(genetic.best)} km\n')
    f.write(f'Лучший маршрут: {", ".join(matrix.get_names(genetic.best))}\n')
    f.write(f'\n')

