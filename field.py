import tkinter as tk
from time import sleep

import numpy as np

# GLOBAL

Fields = []  # 存储电场类
MinTick = 0.02


def init():
    global root, canvas
    root = tk.Tk()
    root.title("hello world")
    root.geometry("800x600")
    root.attributes('-type', 'dialog')  # 若无法运行，请注释掉此行
    canvas = tk.Canvas(root, height=600, width=800, bg="#CDC9C9")
    canvas.pack()


init()

# GLOBAL定义结束
"""
函数定义部分
"""


def _ifInField(charge, Fields=[]):  # 检测电荷是否处于电场中,务必是矩形
    effectiveField = []
    for k in Fields:
        if k.position[0][0] <= charge.position[0] <= k.position[1][0] and \
                k.position[0][1] <= charge.position[1] <= k.position[1][1]:
            effectiveField.append(k)
    return effectiveField


def _kineticEnergy(mass, velocity):
    enegry = 0.00
    for k in velocity:
        enegry += 0.5 * mass * (k ** 2)
    return enegry


class Field:  # 电场类
    def __init__(self, canvas, xB=0, yB=0, width=20, height=20,
                 type="Infinity", strength=1, direction=0):
        # 保存数据
        self.strength = np.array([strength * np.cos(np.deg2rad(direction)),
                                  strength * np.sin(np.deg2rad(direction))])  # 直接将电场强度分解
        self.type = type
        self.position = np.array([[xB, yB], [xB + width, yB + height]], dtype=np.float64)  # todo 此处要求起始值必须小于结束值，后期再添加更改
        Fields.append(self)
        # canvas.create_text(20, 20, font="SimHei", text="hello", fill="#FFFFFF")
        canvas.create_rectangle(xB, yB, xB + width, yB + height, fill="#9AFFFF")
        root.update()


class Charge():
    def __init__(self, mass=1, quantity=1, xB=0, yB=0, ):
        self.mass = mass
        self.quantity = quantity
        self.position = np.array([xB, yB], dtype=np.float64)
        self.point = canvas.create_oval(xB - 2, yB - 2, xB + 2, yB + 2, fill="#1F1E33")
        root.update()

    def setting(self, velocity=0, direction=0):
        self.velocity = np.array([velocity * np.cos(np.deg2rad(direction)),
                                  velocity * np.sin(np.deg2rad(direction))])  # 分解为水平速度和竖直速度
        self.direction = direction

    def simulate(self, _fields=Fields):
        tick = 0
        while 0 < self.position[0] < 800 and 0 < self.position[1] < 600:
            tick += 1
            effectiveFields = _ifInField(self, _fields)
            Xa = 0
            Ya = 0
            if effectiveFields != []:
                for field in effectiveFields:
                    Xa = (field.strength[0] * self.quantity) / self.mass + Xa
                    Ya = (field.strength[1] * self.quantity) / self.mass + Ya

                self.velocity[0] += Xa * MinTick;
                self.velocity[1] += Ya * MinTick
                self.position[0] = self.velocity[0] * MinTick + self.position[0]
                self.position[1] = self.velocity[1] * MinTick + self.position[1]
                print("{:^10s} ,动能：{:^10.4f}J".format(str(effectiveFields), _kineticEnergy(self.mass, self.velocity)),
                      end="\r")  # todo
                # 动画部分
                canvas.moveto(self.point, self.position[0], self.position[1])
                canvas.create_oval(self.position[0], self.position[1], self.position[0], self.position[1],
                                   fill="#000000")
                sleep(MinTick)
                root.update()

            else:

                self.position[0] = self.velocity[0] * MinTick + self.position[0]
                self.position[1] = self.velocity[1] * MinTick + self.position[1]
                canvas.moveto(self.point, self.position[0], self.position[1])
                canvas.create_oval(self.position[0], self.position[1], self.position[0], self.position[1],
                                   fill="#000000")
                sleep(MinTick)
                root.update()
                print("{:^10s}".format("未在任何电场内"), end="\r")

        print("\n模拟结束")


# 定义电场

fieldA = Field(xB=10, yB=10, width=200, height=200, canvas=canvas, strength=10, direction=90)
fieldB = Field(xB=120, yB=220, width=200, height=200, canvas=canvas, strength=15, direction=270)

# 定义电荷
chargeA = Charge(xB=30, yB=30, mass=1, quantity=2)
chargeA.setting(velocity=20, direction=0)
chargeA.simulate()

root.mainloop()
