from topsis import Topsis
import numpy as np

evaluation_matrix = np.array([
    [9, 9, 9, 9, 9, 9, 9],
    [9, 9, 5, 5, 5, 5, 9],
    [5, 5, 9, 5, 9, 9, 5],
    [2, 5, 5, 5, 2, 2, 2]
])

weights = [5, 5, 5, 5, 9, 0, 0]

criterias = np.array([1, 1, 1, 1, 1, 0, 0])
# np.ones(7) -> [1, 1, 1, 1, 1, 1, 1]

t = Topsis(evaluation_matrix, weights, criterias)

t.calc()

print("best_distance\t", t.best_distance)
print("worst_distance\t", t.worst_distance)

# print("weighted_normalized",t.weighted_normalized)

print("worst_similarity\t", t.worst_similarity)
print("rank_to_worst_similarity\t", t.rank_to_worst_similarity())

print("best_similarity\t", t.best_similarity)
print("rank_to_best_similarity\t", t.rank_to_best_similarity())
