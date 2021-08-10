from ptools.pms.hpmser import hpmser_GX

from psdd import get_psdd
from function import rastrigin_func_ndim



if __name__ == '__main__':

    psdd = get_psdd(n_dim=2, rng=0.7)
    print(psdd)

    hpmser_GX(
        func=           rastrigin_func_ndim,
        psd=            psdd,
        devices=        [None]*3,
        #preferred_axes= ['p1','p2'],
        verb=           1)
