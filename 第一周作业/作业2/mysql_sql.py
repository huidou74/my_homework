#/usr/bin/python
#-*- coding:utf-8 -*-
zd = {'id':0,'name':1,'age':2,'class':3}

while True:
    new_string = raw_input('请输入要操作的SQL语句: ')
    if new_string:
        if new_string.lower() == 'q':
                break
        a = new_string.split()[0].lower()
        b = new_string.split()[1].lower()
        c = new_string.split()[2].lower()
        d = new_string.split()[3].lower()
#    e = new_string.split()[4].lower()
#    f = new_string.split()[5].lower()
    else :
         print ("输入不能为空！")
         break
    if a == 'select':
        if b == '*':
            if (c == 'from') and (d == 'mysql'):
                with open("mysql") as s_fd:
                    while True:
                        line = s_fd.readline()
                        if not line:
                            break
                        print line,
        elif b:
            v = zd.get(b)
            if v:
                if (c == 'from') and (d == 'mysql'):
                    print "-----%s-----" % b   
                    with open("mysql") as s_fd:
                        while True:
                            line = s_fd.readline().split()
                            if not line:
                                break
                            print line[v]
            if not v:
                n_b = b.split(',')
#                n_b.sort()
                for i in n_b:
                    new = zd.get(i)
                    if (c == 'from') and (d == 'mysql'):
                        print "-----%s-----" % i
                        with open("mysql") as s_fd:
                            while True:
                                line = s_fd.readline().split()[new:(new+1)]
                                if not line:
                                    break
                                print line
            else:
                print ("\nsql语法输入错误,请重新输入!\n")
        else :
            print ("\n输入有误，请重新输入!\n")
    elif a == 'update':
        e = new_string.split()[4].lower()
        f = new_string.split()[5].lower()
        if  (b == 'mysql') and (c == 'set') and (e == 'where'):
            n_d1 = d.split("=")[0].lower()  #字段
            n_d2 = d.split("=")[1].lower()  #字段对应的值
            n_f = f.split("=")[1].lower()   #id 的值
            v = zd.get(n_d1)    #值
            with open("mysql") as fd:
                while True:
                    line = fd.readlines()
                    if not line:
                        break
                    aa = line                  #将返回的列表存入变量
                    a = line.pop(int(n_f))     #弹出ID的值
            print "-----> %s" % a
            n = list(a.split())                #弹出一行的字符串
            del n[int(v)]                      #删除对应索引,需要上面get对应的值
            if n_d1 == 'age':
                n_d2 = n_d2[1:-1]
                n.insert(v,str(n_d2))
            else:
                n.insert(v,str(n_d2))           #根据索引,再插入新的值
            nn = '         '.join(n )           #转成字符串,加空格对其表单
            aa.insert(int(n_f),(str(nn)+'\n'))     #往变量里,插入新值
            print "-----> %s" % nn
            with open("mysql","w") as dd_df:    #最后再写入文件
                for i in aa:                          #利用刚存的列表变量,因为是覆盖,所以用遍历去写
                    dd_df.write(i)
            print ("\n内容已更新,请重新查询\n")
        else :
            print ("\nsql语法错误,请重新输入!\n")    
    elif a == 'delete':
        e = new_string.split()[4]
        if (b == 'from') and (c == 'mysql') and (d == 'where'):
            n_e = e.split("=")[1]              #取id的值,现在还是字符串       
            with open("mysql") as d_df:
                while True:
                    lines = d_df.readlines()
                    if not lines:
                        break
                    d_lines = lines
            del d_lines[int(n_e)]
            with open("mysql",'w') as w_df:
                for i in d_lines:
                    w_df.write(i)
            print ("\n所选ID内容字段已删除,请重新查询!\n")
    else :
        print ("输入语法错误,请重新输入!\n\n温馨提示 :\n本脚本暂只支持,查,更,删!\n") 
