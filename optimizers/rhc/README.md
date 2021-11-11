# README

## Reference

[https://github.com/pybrain/pybrain/blob/master/pybrain/optimization/hillclimber.py](https://github.com/pybrain/pybrain/blob/master/pybrain/optimization/hillclimber.py)

Schaul, T., Bayer, J., Wierstra, D., Sun, Y., Felder, M., Sehnke, F., Rückstieß, T. and Schmidhuber, J., 2010. PyBrain. Journal of Machine Learning Research, 11(24), pp.743-746.

## Source Code

### Python

The Python version can be downloaded from [https://github.com/pybrain/pybrain/blob/master/pybrain/optimization/hillclimber.py](https://github.com/pybrain/pybrain/blob/master/pybrain/optimization/hillclimber.py).

### Repeatability

For making comparisons, we need to use the code, as represented in the same folder.

The following result is obtained on the **Ellipsoid** benchmark function:

```python
best_so_far_y: 3.8060228e7
n_function_evaluations: about 2000000
Runtime: 3.04709e2
```


The following result is obtained on the **Rosenbrock** benchmark function:

```python
best_so_far_y: 3.8060228e7
n_function_evaluations: about 2000000
Runtime: 3.04709e2
```


The following result is obtained on the **Rastrigin** benchmark function:

```python
best_so_far_y: 9.959e3
n_function_evaluations: about 2000000
Runtime:2.33276e+02
```

## Open-Source Python Implementation in ```PyPop```

[https://github.com/Evolutionary-Intelligence/pypop/blob/main/optimizers/rs/rhc.py](https://github.com/Evolutionary-Intelligence/pypop/blob/main/optimizers/rs/rhc.py)

For making fair comparisons, we need to use the code with the same hyper-parameter settings, as represented in the same folder.

### Repeatability

Owing to their difference on random number generation (RNG), we do NOT expect the exactly same optimization result even on the same function.
As a compromise, we focus more on the *magnitude* similarity. That is, two different implementations should generate as the same magnitude as possible, even under randomness.

The following result is obtained on the **Ellipsoid** benchmark function:

```python
best_so_far_y: 3.9791342e7
n_function_evaluations: about 2000000
Runtime: 1.84341e2
```


The following result is obtained on the **Rosenbrock** benchmark function:

```python
best_so_far_y: 2.9621e4
n_function_evaluations: about 2000000
Runtime: 2.12897e2
```


The following result is obtained on the **Rastrigin** benchmark function:

```python
best_so_far_y: 9.817e3
n_function_evaluations: about 2000000
Runtime:5.12971e2
```

Luckily, we observe the almostly same results!
