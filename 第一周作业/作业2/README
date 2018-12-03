作业2
模拟mysql 查询语句

要有 select update  delete 的功能

需要输入对应字段

select        *                from          table_name;
DELETE     FROM       mysql          WHERE id=1
update     mysql        set               age="21"          where       id=3;
a               b                c                      d                       e           f


然后再查字典，
zd = {'id':0,'name':1,'age':2,'class':3}

select
查表最简单，只要输入对应字段我就输出


update
因为输入过长 ，所以加多字段，e,f
判断对应的字段，返回值暂存
 将返回整个列表存入变量
 弹出ID的值
再弹出一行的字符串
删除对应索引,需要上面get对应的值
根据索引,再插入新的值
转成字符串,加空格对其表单
往变量里,插入新值
最后再写入文件
用刚存的列表变量,因为是覆盖,所以用遍历去写



delete
取id的值,现在还是字符串
找到该列表然后先del再insert  可以指定索引
用刚存的列表变量,因为是覆盖,所以用遍历去写入文件












先创建mysql 数据

mysql> create table mysql(
    -> id INT NOT NULL AUTO_INCREMENT,
    -> name VARCHAR(100) NOT NULL,
    -> age VARCHAR(100) NOT NULL,
    -> class VARCHAR(100) NOT NULL,
    -> PRIMARY KEY ( id )
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;

mysql> desc mysql;    #查看结构
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(100) | NO   |     | NULL    |                |
| age   | varchar(100) | NO   |     | NULL    |                |
| class | varchar(100) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+



insert into mysql (name,age,class) values ("zhang3","25","python1班");
insert into mysql (name,age,class) values ("li4","23","python1班");
insert into mysql (name,age,class) values ("wang5","24","python2班");
insert into mysql (name,age,class) values ("zhu6","21","python1班");
insert into mysql (name,age,class) values ("zhao7","27","python1班");
insert into mysql (name,age,class) values ("liu8","29","python2班");
insert into mysql (name,age,class) values ("song2","25","python1班");




DELETE FROM table_name [WHERE Clause]
DELETE FROM mysql WHERE id=1;






































