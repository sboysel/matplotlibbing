"""
https://matplotlib.org/stable/tutorials/introductory/lifecycle.html
https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html
https://matplotlib.org/stable/tutorials/colors/colors.html
"""
import numpy as np
import matplotlib.pyplot as plt

n = 1000

e = np.random.normal(size=n)
x = np.random.normal(size=n)
d_d = np.random.binomial(n=2, p=0.5, size=n)
d_c = np.random.uniform(0, 2, size=n)
y = 1.5 * x + e


"""
Scatter plot (discrete class)
"""
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, s=1, c=d_d, cmap=plt.get_cmap('viridis'))
# legend: colors for d
legend1 = ax.legend(*scatter.legend_elements(),
                    loc='lower right', title='class')
ax.add_artist(legend1)
ax.set_xlabel('x')
ax.set_ylabel('y')

# plt.show()
plt.savefig('pdf/scatter_discrete.pdf')

"""
Scatter plot (continuous class)
"""
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, s=1, c=d_c, cmap=plt.get_cmap('viridis'))
# # legend: colors for d
# legend1 = ax.legend(*scatter.legend_elements(),
#                     loc='lower right', title='class')
fig.colorbar(scatter, label='class')
ax.set_xlabel('x')
ax.set_ylabel('y')

# plt.show()
plt.savefig('pdf/scatter_continuous.pdf')
