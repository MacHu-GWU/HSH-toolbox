##################################
#encoding=utf8                   #
#version =py27 only              #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

'''Usage:
from HSH.RobotHand.macro import *
'''
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

def Delay(n):
    time.sleep(n)

''' ====== Mouse Macro ====== '''
def Left_click(x, y, n = 1, dl = 0):
    '''在屏幕某点左键点击若干次
    '''
    Delay(dl)
    mouse_m.click(x, y, 1, n)

def Right_click(x, y, n = 1, dl = 0):
    '''在屏幕某点右键点击若干次
    '''
    Delay(dl)
    mouse_m.click(x, y, 2, n)

def Double_click(x, y, dl = 0):
    '''在屏幕的某点双击
    '''
    Delay(dl)
    mouse_m.click(x, y, 1, n = 2)

def Scroll_up(n, dl = 0):
    '''鼠标滚轮向上n次
    '''
    Delay(dl)
    mouse_m.scroll(vertical = n)

def Scroll_down(n, dl = 0):
    '''鼠标滚轮向下n次
    '''
    Delay(dl)
    mouse_m.scroll(vertical = -n)

def Move_to(x, y, dl = 0):
    '''鼠标移动到x, y的坐标处
    '''
    Delay(dl)
    mouse_m.move(x, y)

def Drag_and_release(start, end, dl = 0):
    '''从start的坐标处鼠标左键单击拖曳到end的坐标处
    start, end是tuple. 格式是(x, y)
    '''
    Delay(dl)
    mouse_m.press(start[0], start[1], 1)
    mouse_m.drag(end[0], end[1])
    Delay(0.1)
    mouse_m.release(end[0], end[1], 1)

def Screen_size():
    return mouse_m.screen_size()

def WhereXY():
    return mouse_m.position()

''' ====== Keyboard Macro ====== '''
'''COMBINATION组合键'''
'''Ctrl系列'''

def Ctrl_c(dl = 0):
    '''Ctrl + c 复制
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.control_key)
    keyboard_k.tap_key('c')
    keyboard_k.release_key(keyboard_k.control_key)

def Ctrl_x(dl = 0):
    '''Ctrl + x 剪切
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.control_key)
    keyboard_k.tap_key('x')
    keyboard_k.release_key(keyboard_k.control_key)
    
def Ctrl_v(dl = 0):
    '''Ctrl + v 粘贴
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.control_key)
    keyboard_k.tap_key('v')
    keyboard_k.release_key(keyboard_k.control_key)

def Ctrl_z(dl = 0):
    '''Ctrl + z 撤销上一次操作
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.control_key)
    keyboard_k.tap_key('z')
    keyboard_k.release_key(keyboard_k.control_key)
    
def Ctrl_y(dl = 0):
    '''Ctrl + y 重复上一次操作
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.control_key)
    keyboard_k.tap_key('y')
    keyboard_k.release_key(keyboard_k.control_key)

def Ctrl_a(dl = 0):
    '''Ctrl + a 全选
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.control_key)
    keyboard_k.tap_key('a')
    keyboard_k.release_key(keyboard_k.control_key)
    
def Ctrl_Fn(n, dl = 0):
    '''Ctrl + Fn1~12 组合键
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.control_key)
    keyboard_k.tap_key(keyboard_k.function_keys[n])
    keyboard_k.release_key(keyboard_k.control_key)

'''Alt系列'''
def Alt_Tab(dl = 0):
    '''Alt + Tab 组合键
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.alt_key)
    keyboard_k.tap_key(keyboard_k.tab_key)
    keyboard_k.release_key(keyboard_k.alt_key)

def Alt_Fn(n, dl = 0):
    '''Alt + Fn1~12 组合键
    '''
    Delay(dl)
    keyboard_k.press_key(keyboard_k.alt_key)
    keyboard_k.tap_key(keyboard_k.function_keys[n])
    keyboard_k.release_key(keyboard_k.alt_key)

'''SINGLE KEY单个键盘键'''

def Up(n = 1, dl = 0):
    '''上方向键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.up_key, n)
    
def Down(n = 1, dl = 0):
    '''下方向键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.down_key, n)

def Left(n = 1, dl = 0):
    '''左方向键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.left_key, n)
    
def Right(n = 1, dl = 0):
    '''右方向键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.right_key, n)

def Enter(n = 1, dl = 0):
    '''回车键/换行键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.enter_key, n)

def Delete(n = 1, dl = 0):
    '''删除键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.delete_key, n)

def Back(n = 1, dl = 0):
    '''退格键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.backspace_key, n)
    
def Space(n = 1, dl = 0):
    '''空格键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(' ', n)

def Fn(n, dl = 0):
    '''功能键n次
    '''
    Delay(dl)
    keyboard_k.tap_key(keyboard_k.function_keys[n])
    
def Char(char, n = 1, dl = 0):
    '''输入任意单字符n次，只要能在键盘上打出来的字符都可以
    '''
    if len(char) == 1:
        Delay(dl)
        keyboard_k.tap_key(char)
    else:
        raise Exception("method 'Char()' can only take one character.")

def Type_string(text, interval = 0, dl = 0):
    '''键盘输入字符串，interval是字符间输入时间间隔，单位'秒'
    '''
    Delay(dl)
    keyboard_k.type_string(text, interval)

mouse_m, keyboard_k = PyMouse(), PyKeyboard() # Define module Global variable

if __name__ == '__main__':
    Delay(1)
    '''测试键盘命令'''
#     Up(dl = 1)
#     Down(dl = 1)
#     Left(dl = 1)
#     Right(dl = 1)
    '''测试鼠标命令'''
#     print Screen_size()
#     print WhereXY()