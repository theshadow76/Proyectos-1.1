import numpy as np

a = np.array([1, 3,4, 5, 6, 3, 5, 3, 5])
print(a)

b = np.random.random((1, 100, 14))
print(b)

np.savetxt("myArrayOne.csv", a)
np.loadtxt("myArrayOne.csv")

np.savetxt("alexNoSe.csv", b)