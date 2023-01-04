# %%

filename = 'ID.test'

class ID:
    def __init__(self, Name, Age, QQ, Email):
        self.name = Name
        self.Age = Age
        self.QQ = QQ
        self.Email = Email

    def write_record(self, str):       
        with open(filename, 'w') as file_object: 
            file_object.write(str) 
    
    def create_string(self):
        strs = str(self.name) +'\t'+ str(self.Age) +'\t'+ str(self.QQ) +'\t'+ str(self.Email)
        return strs

while True:
    print('************************')
    print('欢迎使用名片管理系统 V1.0')
    print()
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print()
    print('0. 退出系统')
    print('************************')
    
    Temp = input()
    if Temp == '1':
        Name = input("请输入姓名：") or None
        Age = input("请输入年龄：") or None
        QQ = input("请输入QQ: ") or None
        Email = input("请输入邮箱") or None

        id = ID(Name, Age, QQ, Email)
        print(id.create_string())

    elif Temp == '2':
        break
    elif Temp == '3':
        break
    elif Temp == '0':
        break
    else: 
        break
# %%
