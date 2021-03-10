# TOPSIS-Python

[![Linkedin Badge](https://img.shields.io/badge/-Shivanjan%20Chakravorty-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/shivanjan/)](https://www.linkedin.com/in/shivanjan/) [![Gmail Badge](https://img.shields.io/badge/-schakravorty846-c14438?style=plastic&logo=Gmail&logoColor=white&link=mailto:schakravorty846@gmail.com)](mailto:schakravorty846@gmail.com) [![Github Badge](https://img.shields.io/github/followers/Glitchfix?label=Glitchfix&logo=github&style=plastic)](https://github.com/Glitchfix)

Source code for TOPSIS optimization algorithm in python.

TOPSIS is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion. An assumption of TOPSIS is that the criteria are monotonically increasing or decreasing. Normalisation is usually required as the parameters or criteria are often of incongruous dimensions in multi-criteria problems. Compensatory methods such as TOPSIS allow trade-offs between criteria, where a poor result in one criterion can be negated by a good result in another criterion. This provides a more realistic form of modelling than non-compensatory methods, which include or exclude alternative solutions based on hard cut-offs. An example of application on nuclear power plants is provided in.


### Sample usage

```py
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


```

```sh
[2 1 3]
[2 3 1]
```

##### Resources: 
[WikiPedia](https://en.wikipedia.org/wiki/TOPSIS)
[sample solution](http://www.jiem.org/index.php/jiem/article/view/573/498)
