# coding:utf-8
print("2019/10/30")
print("作者：电脑初哥")
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import requests
import re

def download():
    starUrl = "http://www.uustv.com/"
    #获取用户输入
    name = entry.get()
    #去空格
    name = name.strip()
    if name == "":
        messagebox.showinfo("提示","请输入姓名")
    else:
        pass
    # 模拟网页发送数据
    data ={
        'word':name,
        'sizes':60,
        'fonts':'jfcs.ttf',
        'fontcolor':"#000000"
    }
    result =requests.post(starUrl,data=data)
    #获取网页源码
    result.encoding = "utf8"
    html= result.text
    #print(html)
    reg ='<div class="tu">﻿<img src="(.*?)"/></div>'
    imagePath =re.findall(reg,html)
    imgUrl = starUrl+ imagePath[0]

    #获取图片内容
    response = requests.get(imgUrl).content

    with open("{}.gif".format(name),"wb")as f:
        f.write(response)

        #显示图片
        bm=ImageTk.PhotoImage(file ="{}.gif".format(name))
        label2=Label(root,image=bm)
        label2.bm=bm
        label2.grid(row=2,columnspan=2)




#创建窗口
root = Tk()
#标题
root.title("签名设计")
#窗口大小
root.geometry("660x300+500+300")
#标签控件
label= Label(root,text="签名",font=("华文行楷",20),fg="red")
label.grid()
#输入框
entry=Entry(root,font=("微软雅黑",20))
entry.grid(row=0,column=1)
#点击按钮
button = Button(root,text="设计签名",font=("微软雅黑",20),command=download)
button.grid(row=0,column=2)

#作者
label= Label(root,text="作者:电脑初哥",font=("华文行楷",20))
label.grid()
label.grid(row=4,columnspan=3)



#显示窗口
root.mainloop()


