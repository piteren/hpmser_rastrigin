from hpmser.search_function import hpmser

from psdd import get_psdd
from function import rastrigin_func_ndim, func_exception



if __name__ == '__main__':

    n_dim = 2
    param_range = 2
    add_exceptions = True

    hpmser(
        func=           func_exception if add_exceptions else rastrigin_func_ndim,
        func_psdd=      get_psdd(n_dim=n_dim, rng=param_range),
        func_const=     {'sleep':None},
        devices=        [None]*20,
        n_loops=        500,
        plot_axes=      ['p1','p2'])
