from pypaq.lipytools.decorators import timing

nums = [1]*10000
rep = 10000

@timing
def test_tuple():
    for _ in range(rep):
        t = [(n,) for n in nums]

@timing
def test_list():
    for _ in range(rep):
        t = [[n,] for n in nums]

test_tuple()
test_list()