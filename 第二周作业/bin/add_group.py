#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c

def add_a():
    all_lines_first = all_lines_end = lines = ''   #初始化
    with open("../conf/nginx.conf") as fd:
        while True:
            line = fd.readline()               #读取行 赋予变量
            if 'server 192.168.0.1:8080 weight=100;' in line:   #截取到指定位置跳出
                break
            if 'server 10.0.0.' in line:    #判断一下节点行
                lines += line               #将是这个节点的行保存到一个变量里
            all_lines_first += line     #将需要的行保存到 first变量里
    nums = lines.count('\n')          #判断有多少个IP
    av = '\t\tserver 10.0.0.' + str(nums+1) + ':8080 weight=100;\n'    #自动加一个IP
    with open("../conf/nginx.conf") as fd_new:
        lines_end = fd_new.readlines()
        lines_end_index = lines_end.index('\t\tserver 192.168.0.1:8080 weight=100; \t\t#-->B\xe7\xbb\x84\n')  # 取指定节点的行
        lines = lines_end[lines_end_index:-1]  # 用索引的方式，从这个点 一直读到结尾
        for i in lines:
            all_lines_end += i  # 写入变量暂存
        all_lines = all_lines_first + av + all_lines_end
#    print all_lines
    with open("../conf/nginx.conf", 'w') as fd_w:
        fd_w.write(all_lines)
    print "\n添加成功！\n添加IP为： "+ av



def add_b():
    all_lines_first = all_lines_end = lines = ''
    with open("../conf/nginx.conf") as fd:
        while True:                      #读取行 赋予变量
            line = fd.readline()
            if '    }   ' in line:   #截取到指定位置跳出
                break
            if 'server 192.168.0.' in line:    #判断一下节点行
                lines += line               #将是这个节点的行保存到一个变量里
            all_lines_first += line     #将需要的行保存到 first变量里
    nums = lines.count('\n')            #判断有多少个IP
    av = '\t\tserver 192.168.0.' + str(nums+1) + ':8080 weight=100;\n'    #自动加一个IP
    with open("../conf/nginx.conf") as fd_new:
        lines_end = fd_new.readlines()
        lines_end_index = lines_end.index('    }   \n')  # 取指定节点的行
        lines = lines_end[lines_end_index:-1]  # 用索引的方式，从这个点 一直读到结尾
        for i in lines:
            all_lines_end += i  # 写入变量暂存
        all_lines = all_lines_first + av + all_lines_end
#    print all_lines
    with open("../conf/nginx.conf", 'w') as fd_w:
        fd_w.write(all_lines)
    print "\n添加成功！\n添加IP为： " + av


#add_a()

#add_b()
