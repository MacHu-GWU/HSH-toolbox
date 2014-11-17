##encoding=utf8

from HSH.RobotHand.macro import *

def UT_keyboard_command():
    '''测试键盘命令'''
    Up(dl = 1)
    Down(dl = 1)
    Left(dl = 1)
    Right(dl = 1)
    
def UT_mouse_command():
    '''测试鼠标命令'''
    print Screen_size()
    print WhereXY()
    
Delay(1)
UT_keyboard_command()
UT_mouse_command()