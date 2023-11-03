# 1.魔法方法
class Animal:
    def __init__(self, name):
        self.name = name
        print("")

    def eat(self):
        print(self.name + "要吃东西啦！")

    def drink(self):
        print(self.name + "需要喝水啦！")


cat = Animal("miaomiao")
cat.eat()
cat.drink()

# 2.????
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * x)
fig, ax = plt.subplots()
ax.plot(x, s)
ax.set(xlabel='x', ylabel='y', title='y=sin(x)')
ax.grid()
fig.savefig("sin.png")
plt.show()
