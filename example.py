from topsis import Topsis
import numpy as np

evaluation_matrix = np.array([
    [1,2,3,4],
    [4,3,2,1],
    [3,3,3,3],
])

weights = [5, 5, 9, 0]

'''
if higher value is preferred - True
if lower value is preferred - False
'''
criterias = np.array([True, True, True, True])

t = Topsis(evaluation_matrix, weights, criterias)

t.calc()

print("best_distance\t", t.best_distance)
print("worst_distance\t", t.worst_distance)

# print("weighted_normalized",t.weighted_normalized)

print("worst_similarity\t", t.worst_similarity)
print("rank_to_worst_similarity\t", t.rank_to_worst_similarity())

print("best_similarity\t", t.best_similarity)
print("rank_to_best_similarity\t", t.rank_to_best_similarity())
