from ptools.pms.hpmser.search_function import hpmser

from psdd import get_psdd
from function import rastrigin_func_ndim



if __name__ == '__main__':

    psdd = get_psdd(n_dim=2, rng=0.7)

    #hpmser_func = hpmser_GX
    hpmser_func = hpmser_GX_OMP

    hpmser_func(
        func=           rastrigin_func_ndim,
        func_defaults=  {'sleep':None},
        psdd=           psdd,
        devices=        [None]*20,
        n_loops=        200,
        #preferred_axes= ['p1','p2'],
        verb=           2)
