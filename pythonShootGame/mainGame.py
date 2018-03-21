# # -*- coding:utf-8 -*-
# import py#game
# from sys import exit
# from pygame.locals import *
#
# SCREEN_WIDTH = 480
# SCREEN_HEIGHT = 800
#
# # 初始化游戏
# pygame.init()
# screen = pygame.display.set_mode(SCREEN_WIDTH,SCREEN_HEIGHT)
# pygame.display.set_caption('飞机大战')
#
# # 载入背景图
# background = pygame.image.load('resources/image/background.png')
#
# while 1:
#     # 绘制背景
#     screen.fill(0)
#     screen.bilt(background, (0, 0))
#
#     # 更新屏幕
#     pygame.display.update()
#
#     # 处理游戏退出
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()


# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object
#
# b = 5
# my_line = line_conf()
# print(repr(my_line))
# print(my_line.__closure__)
# # print(my_line.__closure__[0].cell_contents)
#
# def line_conf(a, b):
#     def line(x):
#         return a*x + b
#     return line
#
# line1 = line_conf(3, 2)
# line2 = line_conf(4, 5)
# print(line1(5))


def decorator(f):
    def new_F(a,b):
        print('input',a,b)
        return a,b
    return new_F

def square_sun(a, b):
    return a**2 + b**2

@decorator
def square_substract(a, b):
    return a**2 - b**2

print square_substract(5,4)

