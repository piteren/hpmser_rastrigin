import numpy as np
from pypaq.pms.space.space_estimator import RBFRegressor
import time

from function import rastrigin_func_ndim


def vals(d:np.ndarray) -> np.ndarray:
    vL = [rastrigin_func_ndim(
        x=              x,
        y=              y,
        a=              1,
        flat=           rng,
        random_offset=  1.0,
        sleep=          None) for x,y in d]
    return np.asarray(vL)


if __name__ == '__main__':

    rng = 5

    n_add = 20
    n_loops = 50

    rr = RBFRegressor()

    tp = rng * np.random.rand(1000, 2) - rng / 2

    s_time = time.time()
    for loop in range(n_loops):

        new_points = rng * np.random.rand(n_add, 2) - rng / 2
        vals_new_points = vals(new_points)

        l = rr.update(X_new=new_points, y_new=vals_new_points)
        print(f'{loop:2} {l:.4f} {rr}')

    print(f'time taken: {time.time()-s_time:.1f}s')