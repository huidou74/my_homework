#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
with open('password.txt') as fd:    #初始化字典
    while True:
        line1 = fd.readline()
        if not line1:
            break
        dict1 = eval(line1)    # json字符串转为字典 赋给变量
print dict1
n = 5
while True:
    if n == 0:
        print ("\n系统回复：\n密码输入错误次数过多，系统强制退出!")    
        sys.exit()
    user = raw_input("请输入使用登陆的用户名: ")
    new_user = user.translate(None,'!@#$%^&*()_+-= \/.,?><~`')
    print ("警告:输入的用户名不能有特殊字符,否则系统自动过滤！\n")
    print ("这是您输入的用户名: " + str(new_user)+'\n')
    if new_user:   #判断是否正确输入
        if new_user == 'q':
            print ("\n系统回复：\nBey!\n")
            sys.exit()
        a = dict1.get(new_user)     #找key返回对应的值
        if a:                  #判断是否不为空
           passwd = raw_input("请输入密码: ")
           if a == passwd:         #判断是否正确
               with open('motd') as fd:    #欢迎页面
                   while True:
                       line = fd.readline()
                       if not line:
                           break
                       print line,
               while True:       #判断用户输入
                   a_user = raw_input("如果想退出请输入'q'.\n或者你可以选择注册新用户,请输入'add'.\n你的选择是? : ")
                   if_user = a_user.translate(None,'!@#$%^&*()_+-= \/.,?><~`')
                   if if_user:
                       n_a = dict1.get(if_user)
                       if n_a:
                           print ("该用户名已存在,请重新输入!")
                       else:                         
                           if if_user == 'add':          #添加用户
                              add_user = raw_input("请输入新创建的用户名: ")
                              add_u = dict1.get(add_user)
                              if add_u:
                                  print ("该用户名已存在,请重新输入!")
                              else:
                                  add_passwd = raw_input("请输入新创建用户的密码: ")
                                  dict2 = {add_user:add_passwd}        #转换为字典暂存
                                  with open("/tmp/123",'a') as n_fd:  #打开用户存储文件开始写入新建的用户
                                      n_fd.write(str(dict2)+'\n')
                                  with open("/tmp/123") as r_fd:
                                      while True:
                                          new_line = r_fd.readlines()
                                          if not new_line:
                                              break
                                          dict2 = eval(new_line[0])
                                          dict3 = eval(new_line[1])     #将字符串转为字典再合并
                                  dict2.update(dict3)                   #update dict  
                                  with open("/tmp/123",'w') as w_fd:
                                      w_line = w_fd.write(str(dict2))     #将新建的写入文件
                                  print ("\n系统回复：\n创建新用户成功!\n")
                           elif if_user == 'q':
                               print ("\n系统回复：\nBey\n!")
                               sys.exit()
                           else :
                               print ("\n系统回复：\n错误操作请重新选择!\n\n") 
                   elif if_user == 'q':
                       print ("\n系统回复：\nBey!\n")
                       sys.exit()
           	   else: 
                       print ("\n系统回复：\n错误操作请重新选择!\n\n")
           else:
               n -= 1 
               print ("\n系统回复：\n密码输入错误,重新输入!\n还剩: "+str(n)+" 机会!\n")
        else: 
            print ("\n系统回复：\n没有该用户,请重新输入!\n\n")  
    else: 
        print ("\n系统回复：\n输入不能为空! 请重新输入!\n\n")     

