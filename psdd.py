# prepares parameters space definition dict
def get_psdd(n_dim: int, rng: float) -> dict:
    return {f'p{n}': [-rng, rng] for n in range(n_dim)}