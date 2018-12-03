#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
# A up
def changeUp_A():
    lines = ''
    with open("../conf/nginx2.conf") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            if 'server 192.168.0' in line:
                line = line.replace('server','#server')
            lines += line
    with open("../conf/nginx2.conf",'w') as fd_w:
        fd_w.write(lines)
    print "\n\nA 组 up 成功\n\n"

# A down
def changeDown_A():
    lines = ''
    with open("../conf/nginx2.conf") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            if 'server 192.168.0' in line:
                line = line.replace('#server','server')
            lines += line
    with open("../conf/nginx2.conf",'w') as fd_w:
        fd_w.write(lines)
    print "\n\nA 组 down 成功\n\n"


# B up
def changeUp_B():
    lines = ''
    with open("../conf/nginx2.conf") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            if 'server 10.0.0' in line:
                line = line.replace('server','#server')
            lines += line
    with open("../conf/nginx2.conf",'w') as fd_w:
        fd_w.write(lines)
    print "\n\nB 组 up 成功\n\n"

# B down
def changeDown_B():
    lines = ''
    with open("../conf/nginx2.conf") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            if 'server 10.0.0' in line:
                line = line.replace('#server','server')
            lines += line
    with open("../conf/nginx2.conf",'w') as fd_w:
        fd_w.write(lines)
    print "\n\nB 组 down 成功\n\n"

#倒计时
def timeOut():
    import time
    ppp = ''
    for i in range(4):
        time.sleep(0.5)
        ppp += '.'
        print  ppp

#重启服务
def nginxReload():
    print "\n重启Nginx服务"
    timeOut()
    print "\n重启Nginx服务成功\n\n"

#迭代
def iteration():
    print "\n迭代"
    timeOut()
    print "\n迭代成功\n\n"

#更新代码
def updateCode():
    print "\n更新代码"
    timeOut()
    print "\n更新代码成功\n\n"

while True:
    input_change = raw_input("欢迎使用切组迭代上线功能\nA.将A组切上去\nB.将A组切下来\nC.将B组切上去\nD.将B组切下来\nE.重启Nginx服务\nF.完成迭代\nG.更新代码\n请输入您的选择： ").lower()
    if input_change in 'abcdefgq':
        if len(input_change) > 1:
            print ("\n\n输入有误请重新输入\n退出请输入'q'\n\n ")
        elif input_change == 'q':
            break
        elif input_change == 'a':
            changeUp_A()
        elif input_change == 'b':
            changeDown_A()
        elif input_change == 'c':
            changeUp_B()
        elif input_change == 'd':
            changeDown_B()
        elif input_change == 'e':
            nginxReload()
        elif input_change == 'f':
            iteration()
        elif input_change == 'g':
            updateCode()
    else:
        print "\n输入有误，请重新输入\n"


