import numpy as np
from sklearn.svm import SVR
from typing import List

from function import rastrigin_func_ndim


def vals(d:np.ndarray) -> List[float]:
    return [rastrigin_func_ndim(
        x=              x,
        y=              y,
        a=              1,
        flat=           rng,
        random_offset=  1,
        sleep=          None) for x,y in d]

rng = 5

n_add = 20
n_loops = 50
n_subloops = 10

points = rng * np.random.rand(n_add, 2) - rng / 2
vals_points = vals(points)

RNG_C = [0.01,0.1,1,10,100]
RNG_GAMMA = [0.01,0.1,1,10,100]
RNG_EPSILON = [0.001,0.01,0.1,1]

for loop in range(n_loops):

    new_points = None
    vals_new_points = None
    errors = {}
    for sl in range(n_subloops):
        new_points = rng * np.random.rand(n_add, 2) - rng / 2
        vals_new_points = vals(new_points)


        for c in RNG_C:
            for g in RNG_GAMMA:
                for e in RNG_EPSILON:

                    svr_rbf = SVR(kernel="rbf", C=c, gamma=g, epsilon=e)
                    svr_rbf.fit(points, vals_points)

                    pred = svr_rbf.predict(new_points)

                    error = sum([(a-b)**2 for a,b in zip(pred,vals_new_points)])
                    k = c,g,e
                    if k not in errors:
                        errors[k] = 0

                    errors[k] += error

    errL = [(k,v) for k,v in errors.items()]
    errL.sort(key=lambda x:x[-1])
    #print(errors)
    best = errL[0]
    c,g,e = best[0]
    err = best[1] / n_subloops
    print(f'loop {loop:3}, error: {err:.3f}, c:{c:6} g:{g:6} e:{e:6}')

    points = np.concatenate([points,new_points])
    vals_points += vals_new_points