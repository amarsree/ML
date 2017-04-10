import numpy as np
import matplotlib.pyplot as plt

grayhounds= 500
labs = 300

gray_heights = 28 + 4* np.random.randn(grayhounds)
lab_heights = 28 + 7* np.random.randn(labs)
plt.hist([gray_heights,lab_heights],stacked=True, color=['r','b'])
plt.show()
