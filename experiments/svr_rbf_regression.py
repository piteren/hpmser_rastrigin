import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
import time


def func(x):
    return np.sin(x).ravel()


x = np.sort(20 * np.random.rand(10, 1), axis=0)
y = func(x)

svr_rbf = SVR(
    kernel=     "rbf",
    C=          100,    # 0.001 - 100, controls error
    gamma=      0.1,    # 0.001 - 100, controls shape of decision boundary, larger for more complex
    epsilon=    0.01,   # threshold for what is considered an acceptable error rate in the training data
)

s_time = time.time()
svr_rbf.fit(x, y)
print(f'RBF took {time.time()-s_time:.4f}s')

xn = np.sort(20 * np.random.rand(300, 1), axis=0)

plt.clf()
plt.plot(xn, svr_rbf.predict(xn), label="RBF_xn")
plt.scatter(x, y,
            facecolor=  "none",
            edgecolor=  "k",
            s=          50,
            label=      "training data")
plt.scatter(xn, func(xn),
            facecolor=  "none",
            edgecolor=  "m",
            s=          50,
            label=      "true")
plt.legend()
plt.show()
