import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog,messagebox

FONTSTYLE = ["常规","斜体","粗体","粗偏斜体"]
FONTSIZE = ['8','9','10','11','12','16','18','20','22','24','26','28','36','48','72','一号','小一','二号','小二','三号','小三','四号','小四']
FONTSURL = r"C:\\Windows\\Fonts"
def getfonts():
    result = []
    fonts = os.listdir(FONTSURL)
    for item in fonts:
        if item.endswith(".ttf"):
            font =item[:-4]
            result.append(font)
    return result
class Mydialog(tk.Toplevel):
    """
    自定义字体窗口
    """
    def __init__(self,mainwin):
        super().__init__()
        self.mainwin = mainwin
        # self.resizable(0,0)
        self.createface()
    def createface(self):
        l1 = tk.Label(self,text="字体(F):")
        l1.grid(row=0,column=0)
        l2 = tk.Label(self,text="字形(Y):")
        l2.grid(row=0,column=1)
        l3 = tk.Label(self,text="大小(S):")
        l3.grid(row=0,column=2)

        e1 = tk.Entry(self,width=15)
        e1.grid(row=1,column=0)
        e1.insert(tk.END,'幼圆')
        e2 = tk.Entry(self,width=12)
        e2.grid(row=1,column=1)
        e2.insert(tk.END,'常规')
        e3 = tk.Entry(self,width=8)
        e3.insert(tk.END,'四号')
        e3.grid(row=1,column=2)
        self.e1=e1
        self.e2=e2
        self.e3=e3
        f1 = tk.Frame(self)
        f1.grid(row=2,column=0)
        f2 = tk.Frame(self)
        f2.grid(row=2,column=1)
        f3 = tk.Frame(self)
        f3.grid(row=2,column=2)

        lis1 = tk.Listbox(f1,width=15)
        lis2 = tk.Listbox(f2,width=12)
        lis3 = tk.Listbox(f3,width=8)
        self.lis1 = lis1
        lis1.bind("<Double-Button-1>",self.fn1)
        self.lis2 = lis2
        lis2.bind("<Double-Button-1>",self.fn2)
        self.lis3 = lis3
        lis3.bind("<Double-Button-1>",self.fn3)
        s1 = tk.Scrollbar(f1,command=lis1.yview)
        s2 = tk.Scrollbar(f2)
        s3 = tk.Scrollbar(f3,command=lis3.yview)

        lis1.pack(side=tk.LEFT,pady=10)
        lis1.config({
            'yscrollcommand':s1.set      #内容与滚动条联动 
        })
        s1.pack(side=tk.RIGHT,fill=tk.Y)
        for item in getfonts():
            lis1.insert(tk.END,item)
        lis2.pack(side=tk.LEFT,pady=10)
        s2.pack(side=tk.RIGHT,fill=tk.Y)
        for item in FONTSTYLE:
            lis2.insert(tk.END,item)
        lis3.pack(side=tk.LEFT,pady=10)
        lis3.config({
            'yscrollcommand':s3.set
        })
        s3.pack(side=tk.RIGHT,fill=tk.Y)
        for item in FONTSIZE:
            lis3.insert(tk.END,item)
        l4 = tk.LabelFrame(self,text="示例",width=100,height=50)
        l4.grid(row=3,column=1,columnspan=2)
        shili = tk.Label(l4,text="微软中文软件",font=("",20),width=15,height=3)
        shili.grid(row=0,column=0)
        f4 = tk.Frame(self,width=130,height=50)
        f4.grid(row=4,column=1,rowspan=3)
        jiaoben = tk.Label(f4,text="脚本(R)")
        jiaoben.place(relx=0.05,rely=0)
        lis4 = ttk.Combobox(f4)
        lis4.config({
            "width":23,
            'values':('中文BG2312')
        })
        lis4.place(relx=0.05,rely=0.55)
        lis4.insert(tk.END,"中文 BG2312")
        submit = tk.Button(self,text="确认",width=10,command=self.setfont)
        submit.grid(row=8,column=0,columnspan=3,pady=20)
        reset = tk.Button(self,text="取消",width=10,command=self.destroy)
        reset.grid(row=8,column=2,padx=20)
        le = tk.Label(self,text="显示更多字体",fg="blue")
        le.place(relx=0.02,rely=0.92)
    def fn1(self,e):
        index = e.widget.curselection()[0]
        val = e.widget.get(index)
        self.e1.delete(0,'end')
        self.e1.insert(tk.END,val)
    def fn2(self,e):
        index = e.widget.curselection()[0]
        val = e.widget.get(index)
        self.e2.delete(0,'end')
        self.e2.insert(tk.END,val)
    def fn3(self,e):
        index = e.widget.curselection()[0]
        val = e.widget.get(index)
        self.e3.delete(0,'end')
        self.e3.insert(tk.END,val)
    def setfont(self):
        font_family = self.e1.get()
        font_style = self.e2.get()
        font_size = self.e3.get()
        if font_style=="粗体":
            font_style="bold"
        elif font_style=="斜体":
            font_style="italic"
        elif font_style=="常规":
            font_style="normal"
        elif font_style=="粗偏斜体":
            font_style="bold italic"
        else:
            font_style=" "
        self.mainwin.t.config({
            "font":(font_family,font_size,font_style)
        })

class Dayin(tk.Toplevel):
    def __init__(self,win):
        super().__init__()
        self.win = win
        self.resizable(0,0)
        self.createface()
    def createface(self):
        f = tk.Frame(self,bg="#ccc",width=400,height=450)
        f.pack()
        l1 = tk.Label(self,text="常规",bg="#fff",width=6)
        l1.place(x=10,y=10)
        f1 = tk.Frame(f,bg="#fff",width=380,height=430)
        f1.place(relx=0.02,rely=0.02)
        l2 = tk.Label(self,text="选择打印机")
        l2.place(x=30,y=30)
        lis = tk.Listbox(self,width=30,height=4)
        for item in ['Fax','Microsoft Print to PDF','Microsoft XPS Document writer','Send To oneNoto 2016']:
            lis.insert(tk.END,item)
        lis.place(x=30,y=50)
        l3 = tk.Label(self,text="状态:",bg="#fff")
        l3.place(x=30,y=150)
        l3 = tk.Label(self,text="位置:",bg="#fff")
        l3.place(x=30,y=180)
        l3 = tk.Label(self,text="备注:",bg="#fff")
        l3.place(x=30,y=210)
        chose = tk.Checkbutton(self,text="打印到文件",bg="#fff")
        chose.place(x=200,y=150)
        btn1 = tk.Button(self,text="首选项(R)")
        btn1.place(x=310,y=150)
        btn2 = tk.Button(self,text="查找打印机(D)")
        btn2.place(x=285,y=210)
        l4 = tk.Label(self,text="页面范围",bg="#fff")
        l4.place(x=30,y=245)
        f2 = tk.Frame(self,bg="#fff",width=200,height=130)
        f2.place(x=30,y=270)
        check1 = tk.Checkbutton(f2,text="全部(L)",bg="#fff")
        check1.grid(row=0,column=0,pady=5)
        check2 = tk.Checkbutton(f2,text="选定范围(T)",bg="#fff")
        check2.grid(row=1,column=0,pady=5)
        check3 = tk.Checkbutton(f2,text="当前页面(U)",bg="#fff")
        check3.grid(row=1,column=2,pady=5)
        check4 = tk.Checkbutton(f2,text="页码(G)",bg="#fff")
        check4.grid(row=2,column=0,pady=5)
        f3 = tk.Frame(self,bg="#fff",width=130,height=130)
        f3.place(x=245,y=270)
        l5 = tk.Label(f3,text="份数(C):",bg="#fff")
        l5.place(relx=0.05,rely=0.1)
        sp = tk.Spinbox(f3)
        sp.config({
            'from_':0,
            'to':100,
            'width':5,
        })
        sp.place(relx=0.6,rely=0.1)
        check5 = tk.Checkbutton(f3,text="自动分页(O)",bg="#fff")
        check5.place(relx=0.05,rely=0.35)
        btn3 = tk.Button(self,text="打印(P)",width=8)
        btn3.place(relx=0.35,rely=0.85)
        btn4 = tk.Button(self,text="取消",width=8,command=self.destroy)
        btn4.place(relx=0.55,rely=0.85)
        btn5 = tk.Button(self,text="应用(A)",width=8)
        btn5.place(relx=0.75,rely=0.85)
class Shezhi(tk.Toplevel):
    def __init__(self,win):
        super().__init__()
        self.win=win
        self.resizable(0,0)
        self.createface()
    def createface(self):
        f = tk.Frame(self,bg="#F0F0F0",width=500,height=400)
        f.pack()
        f1 = tk.Frame(f,bg="#f0f0f0",width=300,height=100)
        f1.place(x=15,y=20)
        l1 = tk.Label(self,text="纸张")
        l1.place(relx=0.05,rely=0.05)
        l2 = tk.Label(f1,text="大小(Z):")
        l2.place(relx=0.09,rely=0.3)
        l2 = tk.Label(f1,text="来源(ZS):")
        l2.place(relx=0.09,rely=0.6)
        lis1 = tk.Spinbox(f1)
        lis1 = ttk.Combobox(f1)
        lis1.config({
            'width':20,
            'values':('A4','A4 横向','A4 加大','A4 小号')
        })
        lis1.insert(tk.END,"A4")
        lis1.place(relx=0.4,rely=0.3)
        lis2=ttk.Combobox(f1)
        lis2.config({
            'width':20,
            'values':('默认')
        })
        lis2.insert(tk.END,"默认")
        lis2.place(relx=0.4,rely=0.6)
        f2 = tk.Frame(f,width=160,height=300)
        f2.place(x=320,y=20)
        yl = tk.Label(self,text="预览")
        yl.place(relx=0.65,rely=0.035)
        canvas = tk.Canvas(f2)
        canvas.config({
            'width':160,
            'height':300,
            'bg':"#999",
        })
        img1 = tk.PhotoImage(file="G:\\My File\\201809\\yulan.png",width=120,height=70)
        canvas.create_image(250,30,image=img1)
        canvas.place(x=0,y=0)
        l3 = tk.Label(self,text="方向")
        l3.place(relx=0.05,rely=0.3)
        f3 = tk.Frame(f,bg="#f0f0f0",width=95,height=100)
        f3.place(x=15,y=120)
        check1 = tk.Radiobutton(f3,text="纵向(O)",bg="#f0f0f0",variable=v1,value="纵向(O)")
        check1.place(relx=0.1,rely=0.35)
        check2 = tk.Radiobutton(f3,text="横向(A)",bg="#f0f0f0",variable=v1,value="横向(A)")
        check2.place(relx=0.1,rely=0.65)
        f4 = tk.Frame(f,bg="#f0f0f0",width=195,height=100)
        f4.place(x=115,y=120)
        l4 = tk.Label(self,text="页边距(毫米)")
        l4.place(relx=0.25,rely=0.28)
        l4_1 = tk.Label(f4,text="左(L):")
        l4_1.place(relx=0.07,rely=0.33)
        e1 = tk.Entry(f4,width=6)
        e1.insert(tk.END,'20')
        e1.place(relx=0.25,rely=0.33)
        l4_2 = tk.Label(f4,text="右(R):")
        l4_2.place(relx=0.55,rely=0.33)
        e2 = tk.Entry(f4,width=6)
        e2.insert(tk.END,'25')
        e2.place(relx=0.75,rely=0.33)
        l4_3 = tk.Label(f4,text="上(T):")
        l4_3.place(relx=0.07,rely=0.63)
        e3 = tk.Entry(f4,width=6)
        e3.insert(tk.END,'20')
        e3.place(relx=0.25,rely=0.63)
        l4_4 = tk.Label(f4,text="下(B):")
        l4_4.place(relx=0.55,rely=0.63)
        e4 = tk.Entry(f4,width=6)
        e4.insert(tk.END,'25')
        e4.place(relx=0.75,rely=0.63)
        ym = tk.Label(self,text="页眉(H):")
        ym.place(relx=0.05,rely=0.6)
        e5 = tk.Entry(self,width=30)
        e5.insert(tk.END,' &f')
        e5.place(relx=0.15,rely=0.6)
        yj = tk.Label(self,text="页眉(F):")
        yj.place(relx=0.05,rely=0.7)
        e6 = tk.Entry(self,width=30)
        e6.insert(tk.END,' 第 &p 页')
        e6.place(relx=0.15,rely=0.7)
        le = tk.Label(self,text="输入值",fg="blue")
        le.place(relx=0.15,rely=0.77)
        btn1 = tk.Button(self,text="确定",width=15)
        btn1.place(relx=0.45,rely=0.85)
        btn2 = tk.Button(self,text="取消",width=15,command=self.destroy)
        btn2.place(relx=0.73,rely=0.85)
class Application(tk.Tk):
    """
    程序的功能逻辑
    """
    def __init__(self):
        super().__init__()
        self.newindex = "1.0"
        self.list1 = []
    #格式的字体设置窗口
    def ziti(self):
        mdg = Mydialog(self)
        self.win.wait_window(mdg)
    #文件下的打印窗口
    def dayin(self):
        dy = Dayin(self)
        self.win.wait_window(dy)
    #文件下的页面设置窗口
    def shezhi(self):
        sz = Shezhi(self)
        self.win.wait_window(sz)
    #文件下的新建功能
    def newfile(self):
        var = self.t.get(0.0,tk.END)
        if var:
            boo = messagebox.askyesnocancel(title="ask",message="是否保存已有数据?")
            if boo:
                filename = filedialog.asksaveasfilename()
                with open(filename,"w") as f:
                    f.write(var)
        self.t.delete(0.0,tk.END)
    #文件下的打开新文件功能
    def openfile(self):
        self.t.delete(0.0,tk.END)
        filename = filedialog.askopenfilename()
        f = open(filename,"r")
        self.t.insert(1.0,f.read())
        f.close()
        var1.set(len(self.t.get(1.0,tk.END)))
    #文件下的另存为功能
    def elsesave(self):
        var = self.t.get(0.0,tk.END)
        if var:
            filename = filedialog.asksaveasfilename()
            with open(filename,"w") as f:
                f.write(var)
        self.t.delete(0.0,tk.END)
    #编辑下的剪切功能
    def cut(self):
        self.t.event_generate("<<Cut>>")
        var1.set(len(self.t.get(1.0,tk.END)))
    #编辑下的复制功能
    def copy(self):
        self.t.event_generate("<<Copy>>")
        var1.set(len(self.t.get(1.0,tk.END)))
    #编辑下的粘贴功能
    def paste(self):
        self.t.event_generate("<<Paste>>")
        var1.set(len(self.t.get(1.0,tk.END)))
    #定义出错弹框
    def alert(self):
        tk.messagebox.showinfo(title="info",message="没有下一个了")
    #查找的窗口样式设置
    def find(self):
        ts=tk.Toplevel(self)
        ts.title("查找")
        ts.geometry("300x110+200+250")
        ts.transient(self)
        tk.Label(ts,text="查找：").grid(row=0,column=0,sticky="e")
        # v=tk.StringVar()
        e=tk.Entry(ts,width=20)
        e.grid(row=0,column=1,padx=2,pady=2,sticky="we")
        self.e=e
        # e.focus_set()
        # c=tk.IntVar()
        tk.Checkbutton(ts,text="区分大小写(c)").place(relx=0.05,rely=0.65)
        tk.Button(ts,text="查找下一个",width=10,command=window.search).place(relx=0.65,rely=0.01)
        tk.Button(ts,text="取消",width=10,command=ts.destroy).place(relx=0.65,rely=0.45)
        ll=tk.Label(ts,text="字符出现次数",width=15,bg="#ccc")
        ll.place(relx=0.05,rely=0.3)
        self.ll=ll
    #查询函数
    def search(self):
        a1 = self.e.get()
        b1 = self.t.get('1.0',tk.END)
        count = b1.count(a1)
        self.ll['text'] = "出现次数:"+str(count)
        if count==0:
            self.ll['text'] = "未查询到"
            self.ll.config(foreground="red")
        else:
            index = self.t.search(a1,self.newindex,tk.END)
            lis = index.split(".")
            row = lis[0]
            col = int(lis[1])
            self.list1.append(index)
            self.t.tag_add("match",index,row+"."+str(len(a1)+col))
            self.t.tag_config('match',background="#ccc",foreground="red")
            self.t.tag_add('tag1',1.0,row+"."+str(col))
            self.t.tag_config('tag1',background="#fff",foreground="#000")
            self.newindex = row+"."+str(len(a1)+col)
        print(self.list1)
    #当查找内容框不为空时，解除按钮的不可选状态
    def sucess(self):
        self.btn.config(state="normal",highlightcolor="blue")
        self.btn1.config(state="normal")
        self.btn2.config(state="normal")
    def empty(self):
        pass
    #替换的窗口样式设置
    def replace(self):
        ts = tk.Toplevel(self)
        ts.title("替换")
        ts.transient(self)
        ts.geometry("360x200+200+200")
        tk.Label(ts,text="查找内容(N):").place(relx=0.03,rely=0.1)
        e1=tk.Entry(ts,width=20,validate="focus",validatecommand=window.sucess,invalidcommand=window.empty)
        self.e=e1
        e1.place(relx=0.25,rely=0.11)
        ll=tk.Label(ts,text="",width=15,bg="#ccc")
        self.ll=ll
        btn = tk.Button(ts,text="查找下一个(F)",width=11,height=1,command=window.search,state="disable")
        btn.place(relx=0.7,rely=0.08)
        self.btn=btn
        tk.Label(ts,text="替换为(P):").place(relx=0.03,rely=0.3)
        e2=tk.Entry(ts,width=20)
        e2.place(relx=0.25,rely=0.3)
        self.e2=e2
        btn1 = tk.Button(ts,text="替换(R)",width=11,command=window.tihuan,state="disable")
        btn1.place(relx=0.7,rely=0.27)
        self.btn1=btn1
        btn2 = tk.Button(ts,text="全部替换(A)",width=11,state="disable")
        btn2.place(relx=0.7,rely=0.45)
        self.btn2=btn2
        btn3 = tk.Button(ts,text="取消",width=11,command=ts.destroy)
        btn3.place(relx=0.7,rely=0.64)
        tk.Checkbutton(ts,text="区分大小写(c)").place(relx=0.05,rely=0.65)
    #替换选定内容的函数
    def tihuan(self):
        a1 = self.e.get()
        a2 = self.e2.get()
        b1 = self.t.get('1.0',tk.END)
        count = b1.count(a1)
        if not count:
            self.ll['text'] = "未查询到"
            self.ll.config(foreground="red")
        else:
            index = self.t.search(a1,'1.0',tk.END)
            lis = index.split(".")
            row = lis[0]
            col = int(lis[1])
            self.t.tag_add("match",index,row+"."+str(len(a1)+col))
            self.t.delete(index,row+"."+str(len(a1)+col))
            self.t.insert(index,a2)
class Face():
    """
    界面部分
    """
    def __init__(self,win):
        self.win = win
        self.addMenu()
        self.textarea()
        self.addstate()
    def addMenu(self):
        #创建菜单栏
        window = self.win
        menubar = tk.Menu(window,tearoff=0)
        #文件
        filemenu = tk.Menu(window,tearoff=0)
        menubar.add_cascade(label="文件(F)",menu=filemenu)
        filemenu.add_command(label="新建(N)",command=window.newfile)
        filemenu.add_command(label="打开(O)",accelerator="Ctrl+O",command=window.openfile)
        filemenu.add_command(label="保存(S)",accelerator="Ctrl+S",)
        filemenu.add_command(label="另存为(A)",accelerator="Ctrl+shift+s",command=window.elsesave)
        filemenu.add_separator()
        filemenu.add_command(label="页面设置(U)",command=window.shezhi)
        filemenu.add_command(label="打印(P)",command=window.dayin)
        filemenu.add_separator()
        filemenu.add_command(label="退出(X)",command=window.destroy)
        #编辑
        editmenu = tk.Menu(window,tearoff=0)
        menubar.add_cascade(label="编辑(E)",menu=editmenu)
        editmenu.add_command(label="撤销(U)")
        editmenu.add_separator()
        editmenu.add_command(label="剪切(T)",accelerator="Ctrl+X",command=window.cut)
        editmenu.add_command(label="复制(C)",accelerator="Ctrl+C",command=window.copy)
        editmenu.add_command(label="粘贴(P)",accelerator="Ctrl+V",command=window.paste)
        editmenu.add_command(label="删除(L)",accelerator="Del")
        editmenu.add_separator()
        editmenu.add_command(label="查找(F)",accelerator="Ctrl+F",command=window.find)
        editmenu.add_command(label="替换(R)",accelerator="Ctrl+H",command=window.replace)
        #格式
        gsmenu = tk.Menu(window,tearoff=0)
        menubar.add_cascade(label="格式(O)",menu=gsmenu)
        gsmenu.add_checkbutton(label="自动换行(W)")
        gsmenu.add_command(label="字体(F)",command=window.ziti)
        #查看
        listmenu = tk.Menu(window,tearoff=0)
        menubar.add_cascade(label="查看(V)",menu=listmenu)
        listmenu.add_command(label="状态栏(S)",command=window.colormapwindows)
        #帮助
        helpmenu = tk.Menu(window,tearoff=0)
        menubar.add_cascade(label="帮助(H)",menu=helpmenu)
        helpmenu.add_command(label="查看帮助(H)")
        helpmenu.add_separator()
        helpmenu.add_command(label="关于记事本(A)")
        window.configure(menu=menubar)
    def addstate(self):
        window = self.win
        f = tk.Frame(window)
        f.pack(fill=tk.X)
        l = tk.Label(f,text="字数:")
        l.pack(side=tk.LEFT)
        l1 = tk.Label(f,textvariable=var1)
        l1.pack(side=tk.LEFT)
        col = tk.Label(f,text="列 ")
        col.pack(side=tk.RIGHT)
        l2 = tk.Label(f,textvariable=var2)
        l2.pack(side=tk.RIGHT)
        row = tk.Label(f,text="行 ")
        row.pack(side=tk.RIGHT)
        l2 = tk.Label(f,textvariable=var3)
        l2.pack(side=tk.RIGHT)
    def textarea(self):
        window=self.win
        f = tk.Frame(window,bg="#ccc")
        f.pack(fill=tk.BOTH,expand=1)
        t = tk.Text(f,font=("",14))
        self.t=t
        t.insert(tk.END,"hello world!")
        t.pack(fill=tk.BOTH,expand=1,side=tk.LEFT)
        s = tk.Scrollbar(f,command=t.yview)   #滚动条与内容联动
        s.pack(fill=tk.Y,side=tk.RIGHT)
        t.config({
            'yscrollcommand':s.set      #内容与滚动条联动 
        })
        self.win.t=t
        var1.set(len(t.get(1.0,tk.END)))
if __name__ == "__main__":
    window = Application()
    var1 = tk.Variable()          # 设置底部状态栏字数的变量
    var1.set(0)
    var2 = tk.Variable()           # 设置底部状态列的变量
    var2.set(10)
    var3 = tk.Variable()           # 设置底部状态栏行的变量
    var3.set(1)
    v1 = tk.Variable()           #文件下的页面设置里方向单选按钮的变量
    v1.set("纵向(O)")
    window.title("新建文本文档.txt - 记事本")
    Face(window)
    window.mainloop()