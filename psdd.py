from ptools.pms.paspa import PSDD

# prepares parameters_space_definition_dict
def get_psdd(n_dim: int, rng: float) -> PSDD:
    if type(rng) is not float: rng = float(rng)
    return {f'p{n}': [-rng, rng] for n in range(n_dim)}