# TOPSIS-Python

[![Linkedin Badge](https://img.shields.io/badge/-Shivanjan%20Chakravorty-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/shivanjan/)](https://www.linkedin.com/in/shivanjan/) [![Gmail Badge](https://img.shields.io/badge/-schakravorty846-c14438?style=plastic&logo=Gmail&logoColor=white&link=mailto:schakravorty846@gmail.com)](mailto:schakravorty846@gmail.com) [![Github Badge](https://img.shields.io/github/followers/Glitchfix?label=Glitchfix&logo=github&style=plastic)](https://github.com/Glitchfix)

Source code for TOPSIS optimization algorithm in python.

TOPSIS is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion. An assumption of TOPSIS is that the criteria are monotonically increasing or decreasing. Normalisation is usually required as the parameters or criteria are often of incongruous dimensions in multi-criteria problems. Compensatory methods such as TOPSIS allow trade-offs between criteria, where a poor result in one criterion can be negated by a good result in another criterion. This provides a more realistic form of modelling than non-compensatory methods, which include or exclude alternative solutions based on hard cut-offs. An example of application on nuclear power plants is provided in.


### Sample usage

```py
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

```

```sh
\~ python3 example.py
Step 1
 [[1. 2. 3. 4.]
 [4. 3. 2. 1.]
 [3. 3. 3. 3.]]

Step 2
 [[0.19611614 0.42640143 0.63960215 0.78446454]
 [0.78446454 0.63960215 0.42640143 0.19611614]
 [0.58834841 0.63960215 0.63960215 0.58834841]]

Step 3
 [[0.05160951 0.1122109  0.30296944 0.        ]
 [0.20643804 0.16831636 0.20197963 0.        ]
 [0.15482853 0.16831636 0.30296944 0.        ]]

Step 4
 [0.05160951 0.1122109  0.20197963 0.        ] [0.20643804 0.16831636 0.30296944 0.        ]

[[0.05160951 0.1122109  0.30296944 0.        ]
 [0.20643804 0.16831636 0.20197963 0.        ]
 [0.15482853 0.16831636 0.30296944 0.        ]]
Step 5
 [0.10098981 0.16468058 0.15492233] [0.16468058 0.10098981 0.05160951]

Step 6
 [0.38013198 0.61986802 0.75011355] [0.61986802 0.38013198 0.24988645]

best_distance    [0.16468058 0.10098981 0.05160951]
worst_distance   [0.10098981 0.16468058 0.15492233]
worst_similarity         [0.38013198 0.61986802 0.75011355]
rank_to_worst_similarity         [1 2 3]
best_similarity  [0.61986802 0.38013198 0.24988645]
rank_to_best_similarity  [3 2 1]
```

##### Resources: 
[WikiPedia](https://en.wikipedia.org/wiki/TOPSIS)
[sample solution](http://www.jiem.org/index.php/jiem/article/view/573/498)
