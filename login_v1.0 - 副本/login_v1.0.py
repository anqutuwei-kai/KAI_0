import json
import easygui as eg
import sys
import pyarmor
import re
import time as t

try:
    title = '登录'
    msg_1 = '请输入账号及密码'
    msg_2 = '登录成功'
    msg_3 = '输入不能为空！'
    fields = ['账号：','密码：']

    file_path = r"F:\python\py项目\登录v1.0\information.json"

    user_path = open(file_path,'r')
    user_data = json.load(user_path)

    def admin_test(a):
        if user_data["user_admin_test"] == 'yes':
            print(str(a))

    admin_test(user_data)

    user_information = eg.multpasswordbox(msg_1,title,fields)
    admin_test(user_information)

    #if (user_information[0] is not None) or (user_information[1] is not None):
    #for field in user_information:
        #field.strip() == ""
        #admin_test(user_information)
    #user_information = [item for item in user_information if item.strip()]
    #admin_test(user_information)
    #for user_information_item in user_information:
    user_information_inspection_0 = user_information[0]
    user_information_inspection_1 = user_information[1]
    if (user_information_inspection_0 == None) or (user_information_inspection_1 == None):
        admin_test(user_information[0])
        admin_test(user_information[1])
        if (user_information[0] == user_data['user']) and (user_information[1] == user_data['password']):
            eg.msgbox(msg_2,title)
    else:
        eg.msgbox(msg_3,title)

except AttributeError as error:
    msg_error = '抱歉，发生了一个错误\n错误代码：1000'
    title_error = '登录（错误1000）'
    eg.msgbox(msg_error.center(80,' '),title_error)
    admin_test(error)
except IndexError as error:
    msg_error = '抱歉，发生了一个错误\n错误代码：2000'
    title_error = '登录（错误2000）'
    eg.msgbox(msg_error.center(80,' '),title_error)
    admin_test(error)
except KeyError as error:
    msg_error = '抱歉，发生了一个错误\n错误代码：3000'
    title_error = '登录（错误3000）'
    eg.msgbox(msg_error.center(80,' '),title_error)
    admin_test(error)
except NameError as error:
    msg_error = '抱歉，发生了一个错误\n错误代码：4000'
    title_error = '登录（错误4000）'
    eg.msgbox(msg_error.center(80,' '),title_error)
    admin_test(error)
except OSError as error:
    msg_error = '抱歉，发生了一个错误\n错误代码：5000'
    title_error = '登录（错误5000）'
    eg.msgbox(msg_error.center(80,' '),title_error)
    admin_test(error)
except TypeError as error:
    msg_error = '抱歉，发生了一个错误\n错误代码：6000'
    title_error = '登录（错误6000）'
    eg.msgbox(msg_error.center(80,' '),title_error)
    admin_test(error)
except SyntaxError as error:
    msg_error = '抱歉，发生了一个错误\n错误代码：7000'
    title_error = '登录（错误7000）'
    eg.msgbox(msg_error.center(80,' '),title_error)
    admin_test(error)