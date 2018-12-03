#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
import manual
import auto
import add_group
while True:
    input_auto = raw_input("欢迎使用切组迭代上线功能\n\n1. 手动完成所有操作\n2. 自动完成所有操作\n3. 选择组，自动添加组内成员IP\n请选择 :  ").lower()
    if input_auto in '123q':
        if input_auto == '1':
            while True:
                input_change = raw_input(
                    "欢迎使用切组迭代上线功能\n-------手动操作-------\nA.将A组切上去\nB.将A组切下来\nC.将B组切上去\nD.将B组切下来\nE.重启Nginx服务\nF.完成迭代\nG.更新代码\n输入'q'返回上级目录\n请输入您的选择： ").lower()
                if input_change in 'abcdefgq':
                    if len(input_change) > 1:
                        print ("\n\n输入有误请重新输入\n退出请输入'q'\n\n ")
                    elif input_change == 'q':
                        break
                    elif input_change == 'a':
                        manual.changeUp_A()
                    elif input_change == 'b':
                        manual.changeDown_A()
                    elif input_change == 'c':
                        manual.changeUp_B()
                    elif input_change == 'd':
                        manual.changeDown_B()
                    elif input_change == 'e':
                        manual.nginxReload()
                    elif input_change == 'f':
                        manual.iteration()
                    elif input_change == 'g':
                        manual.updateCode()
                else:
                    print "\n输入有误，请重新输入\n"
        elif input_auto == '2':
            print "\n全自动操作\n\n"
            input_z = 'server 10.0.0'
            print "A组 下线操作！"
            auto.change_down(input_z)        #A组切下去
            manual.nginxReload()    #重启服务
            manual.updateCode()     #更新代码
            print "A组更新完成，正在上线"
            num = auto.change_up(input_z)         #A组上线
            manual.nginxReload()    #重启服务
            if num == 1:
                input_z = 'server 192.168.0'
                print "B组 下线操作！"
                auto.change_down(input_z)      #B组切下去
                manual.nginxReload()  # 重启服务
                manual.updateCode()   # 更新代码
                print "B组更新完成，正在上线"
                auto.change_up(input_z)       #B组上线
                manual.iteration()   #完成迭代
        elif input_auto == '3':
            while True:
                input_group = raw_input("选择要自动添加IP的组：\n1. A组添加成员IP \n2. B组添加成员IP\n返回上级目录请输入'q'.").lower()
                if input_group in '12q':
                    if input_group == '1':
                        add_group.add_a()
                    elif input_group == '2':
                        add_group.add_b()
                    elif input_group == 'q':
                        break
                else :
                    print "\n输入有误，请重新输入\n"
        elif input_auto == 'q':
            break
    else:
        print "\n输入有误，请重新输入\n"

# AB组 自动迭代 操作 -->  先将A组切下去，然后保证B组是在线的。然后重启服务-->更新代码-->再把A组上线-->再重启服务-----> 迭代----->
#                       -->把B组切下去，保证A组是在线的。重启服务-->更新代码-->再把A组上线-->再重启服务---> 完成

