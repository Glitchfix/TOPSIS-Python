from topsis import Topsis
import numpy as np

evaluation_matrix = np.array([
    [9, 9, 5, 5, 5, 5, 9],
    [5, 5, 9, 5, 9, 9, 5],
    [2, 5, 5, 5, 2, 2, 2]
    ])

weights = [0.9, 0.7, 0.7, 0.7, 0.2, 0.2, 0.2]

criterias = np.array(np.ones(7))

t = Topsis(evaluation_matrix, weights, criterias)

t.calc()

print(t.best_distance)
print(t.worst_distance)


print(t.worst_similarity)
print(t.rank_to_worst_similarity())

print(t.best_similarity)
print(t.rank_to_best_similarity())
