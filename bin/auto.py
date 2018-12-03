#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c

# a,b  为 A组
# c,d  为 B组
# a -- c  为 up     切上去
# b -- d  为 dump   切下去

# AB组 自动迭代 操作 -->  先将A组切下去，然后保证B组是在线的。然后重启服务-->更新代码-->再把A组上线-->再重启服务-----> 迭代----->
#                       -->把B组切下去，保证A组是在线的。重启服务-->更新代码-->再把A组上线-->再重启服务---> 完成



def change_up(input_z):
    lines = ''
    with open("../conf/nginx.conf") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            if input_z in line:
                line = line.replace('#server', 'server')
                print line,
            lines += line
    with open("../conf/nginx.conf", 'w') as fd_w:
        fd_w.write(lines)
    return 1


def change_down(input_z):
    lines = ''
    with open("../conf/nginx.conf") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            if input_z in line:
                line = line.replace('server', '#server')
                print line,
            lines += line
    with open("../conf/nginx.conf", 'w') as fd_w:
        fd_w.write(lines)

