from ptools.pms.hpmser.search_function import hpmser

from psdd import get_psdd
from function import rastrigin_func_ndim


if __name__ == '__main__':

    psdd = get_psdd(
        n_dim=  2,
        rng=    2#0.7
    )

    hpmser(
        func=           rastrigin_func_ndim,
        func_psdd=      psdd,
        func_const=     {'sleep':None},
        devices=        [None]*20,
        n_loops=        500,
        #preferred_axes= ['p1','p2'],
        verb=           2)
