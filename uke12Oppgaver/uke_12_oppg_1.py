import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "|c")
plt.plot(xs, ys_2, "_m")
plt.title('Eksempel 1 gjort om')
plt.xlabel('x')
plt.ylabel('y')

# savefig lagrer filene
plt.savefig("test.png")
plt.savefig("test.pdf")

# interaktivt vindu
plt.show()
