import numpy as np
from pypaq.lipytools.plots import three_dim
from sklearn.svm import SVR

from function import rastrigin_func_ndim


n_samples = 20
rng = 5

d = rng * np.random.rand(n_samples, 2) - rng / 2
val = [rastrigin_func_ndim(
        x=              x,
        y=              y,
        a=              1,
        flat=           rng,
        random_offset=  1,
        sleep=          None) for x,y in d]

tri = np.asarray([(x,y,v) for (x,y),v in zip(d,val)])

three_dim(tri)

svr_rbf = SVR(
    kernel=     "rbf",
    C=          0.01,   # 10^-3 - 10^3, regularization, controls error with margin, lower C -> larger margin, more support vectors, longer fitting time
    gamma=      1,      # 10^-3 - 10^3, controls shape of decision boundary, larger for more complex
    epsilon=    0.01,   # threshold for what is considered an acceptable error rate in the training data
)

svr_rbf.fit(d,val)

d = rng * np.random.rand(2000, 2) - rng / 2
val = svr_rbf.predict(d)

tri = np.asarray([(x,y,v) for (x,y),v in zip(d,val)])
three_dim(tri)