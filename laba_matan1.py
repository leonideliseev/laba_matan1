import math
import matplotlib.pyplot as plt
masx = [x for x in range(1, 101)]
masx11 = []
masx12 = []
masy11 = []
masy12 = []
a = [0 for i in range(100)]
eps1, A = 0.001, 0
for x in range(1, 101):
    y = (1 + math.sin((math.pi * x) / 2)) * x
    if y == 0:
        masy11.append(y)
        masx11.append(x)
    else:
        masy12.append(y)
        masx12.append(x)
y, x = 100000, 1
masx13 = []
masy13 = []
while abs(y - A) >= eps1:
    y = (1 + math.sin((math.pi * x) / 2)) * x
    masx13.append(x)
    masy13.append(y)
    x += 1
x -= 1
n01 = int(masy13[-1])
fig, (ax1, ax2) = plt.subplots(1, 2)
plt.suptitle("Лабораторная работа")
plt.subplot(121)
ax1.scatter(masx11, masy11, c = '#D2691E')
ax1.scatter(masx12, masy12, c = '#008000')
ax1.scatter([x], [n01], c = 'black')
ax1.plot(masx, a, c = '#0000FF')
ax1.text(60, 4, "inf = 0", c = '#0000FF')
ax1.annotate(f"n0 ({x}, {n01})", xy=(x, n01), xytext=(8, 60),
            arrowprops=dict(facecolor='yellow', shrink=1))
plt.title("график последовательности x(n)\nи отмеченный график подпоследовательности x(n) = 4*x + 3")
plt.xlabel("ось n")
plt.ylabel("значение x(n)")
plt.subplot(122)
plt.title("график подпоследовательности x(n) = n*4 + 1")
plt.xlabel("ось n")
plt.ylabel("значение x(n)")
eps2 = float(input("введите эпсилон: "))
y, x = -1, -3
masxpod = []
masypod = []
while (y < 1/eps2):
    x += 4
    masxpod.append(x)
    y = int((1 + math.sin((math.pi * x) / 2)) * x)
    masypod.append(y)
    if len(masxpod) > 15:
        masxpod.pop(0)
        masypod.pop(0)
for e in range(5):
    x += 4
    masxpod.append(x)
    y = int((1 + math.sin((math.pi * x) / 2)) * x)
    masypod.append(y)
ax2.scatter(masxpod, masypod, c='#D2691E')
ax2.plot((masxpod[0], masxpod[-1]), (1/eps2, 1/eps2))
ax2.text(masxpod[1], 1/eps2, f"эпсилон окрестность 1/E = {round(1/eps2, 1)}")
ax2.annotate(f"n0 ({masxpod[-6]}, {masypod[-6]})", xy=(masxpod[-6], masypod[-6]), xytext=(masxpod[0]+25, masypod[0]+20),
            arrowprops=dict(facecolor='yellow', shrink=1))
ax2.scatter(masxpod[-6], masypod[-6], c = 'black')
plt.show()