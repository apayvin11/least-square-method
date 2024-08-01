import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

# origin points
x = [1950, 1960, 1970, 1980, 1990, 2000, 2015]
y = [32, 85, 115, 130, 130, 96, 107]
size = len(x)

print("\t t\t\t Y(t)")
for num in range(len(x)):
    print("\t", x[num], "\t", y[num])

colors = list(matplotlib.colors.CSS4_COLORS)
x_plot = []
size_x_plot = x[-1] - x[0]
x_plot.append(x[0])
for i in range(size_x_plot):
    x_plot.append(x_plot[-1] + 1)

for p in range(2,11):
    cf_mnk = np.polyfit(x, y, p)
    f_plot = []
    for i in range(size_x_plot + 1):
        temp = 0
        for j in range(p+1):
            temp += x_plot[i] ** (p - j) * cf_mnk[j]
        f_plot.append(temp)
    label = "p = " + str(p)
    plt.plot(x_plot, f_plot, color=colors[p*5], label=label)

plt.scatter(x, y, marker = 'o',color = 'green', s = 80 ,label = 'origin points')
plt.legend(loc = 8)    # set legend location
plt.show()