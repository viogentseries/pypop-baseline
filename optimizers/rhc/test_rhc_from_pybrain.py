import time
import numpy as np

from base_functions import ellipsoid, rosenbrock, rastrigin
from pybrain.optimization import HillClimber as HC
for f in [ellipsoid, rosenbrock, rastrigin]:
    print('*' * 7 + ' ' + f.__name__ + ' ' + '*' * 7)
    solver = HC(f, 4 * np.ones((1000,)), minimize=True, maxEvaluations=2e6, verbose=True)
    start_time = time.time()
    solver.learn()
    print("Runtime: {:7.5e}".format(time.time() - start_time))
