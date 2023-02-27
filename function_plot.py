import time
from hpmser.search_results import SRL
from pypaq.pms.paspa import PaSpa
from tqdm import tqdm

from function import STOCHASTIC_SCALE, rastrigin_func_ndim
from psdd import get_psdd


# plots some samples of func
def plot_func(
        ndim: int=  2,
        rng: float= 1.0,
        sscl=       STOCHASTIC_SCALE,
        n_samples=  3000):

    psdd = get_psdd(ndim, rng)
    paspa = PaSpa(psdd=psdd)
    srl = SRL(paspa=paspa, name=f'srl_{ndim}_{rng}_{sscl}')

    points = [paspa.sample_point_GX() for _ in range(n_samples)]
    for pt in tqdm(points): srl.add_result(
        point=  pt,
        score=  rastrigin_func_ndim(
            **pt,
            sscl=   sscl,
            sleep=  0),
        force_no_update=True)

    #srl.print_distances()

    s_time = time.time()
    print('sorting...', end='')
    srl.smooth_and_sort()
    print(f', finished! ({time.time()-s_time:.1f}s)')

    srl.plot()


if __name__ == '__main__':

    # base 2dim examples
    #plot_func(ndim=2, rng=0.5,  sscl=0,     n_samples=100)
    #plot_func(ndim=2, rng=0.5,  sscl=50,    n_samples=100)
    #plot_func(ndim=2, rng=0.5,  sscl=30,    n_samples=500)
    #plot_func(ndim=2, rng=2.0,  sscl=30,    n_samples=100)
    #plot_func(ndim=2, rng=2.0,  sscl=30,    n_samples=1000)
    #plot_func(ndim=2, rng=2.0,  sscl=0,     n_samples=1000)

    # more dims
    #plot_func(ndim=2, rng=0.7, sscl=0,      n_samples=3000)
    #plot_func(ndim=3, rng=0.7, sscl=0,      n_samples=3000)
    #plot_func(ndim=5, rng=0.7, sscl=0,      n_samples=3000)

    plot_func(ndim=2, rng=5.0, sscl=0,      n_samples=3000)