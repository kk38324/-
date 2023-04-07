import xlrd,random  #引入第三方库xlrd(1.2.0)和random库
def function():     #定义一个函数：取其中一行不包含第一个元素形成列表，取其中不为空的一个元素并打印
    g=row[pos:]
    global f        #定义f为全局变量
    f=random.choice(g)
    while(f==""):
        f=random.choice(g)

path=input("请输入文件路径：")          
a = xlrd.open_workbook(filename=path)   #获取文件路径
b=a.sheet_names()                       #获取文件所有分页的名字
sheetName=input("请输入选择的班级：")
c=b.index(sheetName)                    
table=a.sheets()[c]                     #获取对应的分页表格
group=input("请输入想要获得的组别（第几组\所有组）：")
pos=eval(input("请输入组别的列数："))

if group != "所有组":  
    for i in range(table.nrows):
        row=table.row_values(i)     #取每一行元素形成row列表
        if row[pos-1] == group:     #判断每一行列表第一个元素与输入的内容是否相同
            function()
            print("随机结果是：",f)
elif group == "所有组":
    col=table.col_values(pos-1)     #取需要判定的元素所在列的列表
    x=len(col)                      #求列表内元素个数作为循环次数
    for i in range(x):
        row=table.row_values(i)
        if col[i]!="":              #判断列列表中的元素是否为空
            row=table.row_values(i)
            function()
            x=col[i]
            y=x[1]                  #获取目标在哪一组
            print("第{}组，随机结果是：{}".format(y,f))
       

       


