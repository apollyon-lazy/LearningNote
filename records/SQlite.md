一个数据库(.db)文件中可以有很多个表  
每个表又有不同的字段  
根据字段可以为表添加记录
### SQlite下载
官网下载两个预编译压缩文件并解压  
安装后把安装目录添加到系统环境变量Path下  
在命令提示符下输入 sqlite3 后打开环境  
### SQlite关键词
CREATE DROP  
INSERT UPDATE DELETE SELECT
WHERE AND/OR 
LIKE(_%)/GLOB(*?)
LIMIT/OFFSET 
ORDER BY(ASC/DESC)

### SQlite管理
控制命令符下打开 sqlite3 环境；
navicat for SQlite 中可视化；
VScode 中使用高级API
### 几个常用的.命令
.open(打开或创建) 
.quit(退出sqlite3环境) 
.dump(导出.db文件为.sql文件)
.table(列出数据库中所有表)
.schema(得到表的完整信息)
### 创建删除表
创建表：
```
CREATE TABLE database_name.table_name(
   column1 datatype  PRIMARY KEY(one or more columns),
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
);
```
删除表
```
DROP TABLE database_name.table_name;
```
### 增删改查查询
插入查询
```
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);

INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);
```
查询
```
SELECT column1, column2, columnN FROM table_name;
```
更新查询
```
UPDATE table_name
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE [condition];
```
删除
```
DELETE FROM table_name
WHERE [condition];
```