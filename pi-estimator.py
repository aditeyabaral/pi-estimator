import math
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


k = 1
sides = 6
length = 1
temp = sides


def update_side(x): return math.sqrt(2-x)
def update_k(y): return math.sqrt(2+y)
def update_angle(a): return 360/sides
def area(z): return 0.5*sides*z


def x(c): return math.cos(math.radians(c))
def y(c): return math.sin(math.radians(c))


px, py = [], []
temp = 0
fig = plt.figure()
plt.grid(True)
ax = fig.add_subplot(111)
dat = [1, 0]
Ln, = ax.plot(dat, color='black')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
plt.ion()
plt.show()

sides = 6
while True:
    while sides <= 98304:
        calc = area(length)
        print(calc)
        Ln.set_label("Sides = "+str(sides)+"\nArea = "+str(calc))
        ax.legend()
        i = 0
        angle = (360.0/sides)
        while i <= 360:
            px.append(x(i))
            py.append(y(i))
            Ln.set_ydata(py)
            Ln.set_xdata(px)
            plt.pause(0.00001)
            i += angle
        px.clear()
        py.clear()
        k = k = update_k(k)
        length = update_side(k)
        sides *= 2
    sides = 6
    k = 1
    length = 1
