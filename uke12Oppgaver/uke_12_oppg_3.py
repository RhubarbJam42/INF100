import matplotlib.pyplot as plt
from math import sin


# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "|c")
plt.plot(xs, ys_2, "_r")
plt.tick_params(axis='both', which='minor', color='r')
plt.minorticks_on()
plt.title('Eksempel 1 gjort om')
plt.arrow(0, 0, 3, 0, visible=True, ls='-', color='m', width=0.04)

# savefig lagrer filene
plt.savefig("test.png")
plt.savefig("test.pdf")

# interaktivt vindu
plt.show()
