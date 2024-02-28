# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:28:03 2021

@author: 舒晋
"""

from tkinter import *
from tkinter.ttk import *


class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('706常用石油单位换算器')
        self.root.geometry('1100x620')
        
        self.para()
        self.menu()
        self.layout()
        
        self.root.mainloop()
# =============================================================================
# 参数函数    
# =============================================================================
    def para(self):       
        self.oil_name=['长度','压力','产量','密度','粘度','温度']
        self.oil_value=[[DoubleVar(),DoubleVar(),DoubleVar()],
                        [DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()],
                        [DoubleVar(),DoubleVar(),DoubleVar()],
                        [DoubleVar(),DoubleVar(),DoubleVar()],
                        [DoubleVar(),DoubleVar(),DoubleVar()],
                        [DoubleVar(),DoubleVar(),DoubleVar()],
                        [DoubleVar(),DoubleVar(),DoubleVar()]]
        self.oil_unit=[['m','ft','μm'],
                       ['MPa','KPa','Pa','mPa','psi','atm(标准大气压）','bar','米水柱'],
                       ['stb/d','m3/d','t/d'],
                       ['g/cm^3','kg/m^3','lam(lb)/ft3'],
                       ['cP','Pa.s','mPa.s'],
                       ['℃','F','K']]
# =============================================================================
# 菜单栏函数         
# =============================================================================
    def menu(self):
        self.menubar=Menu(self.root)
        
        self.menubar.add_command(label='归零',command=self.zero)
        self.menubar.add_command(label='退出',command=self.root.destroy)
        
        self.root.config(menu=self.menubar)
# =============================================================================
# 布局函数    
# =============================================================================
    def layout(self):
        #变量名布局
        self.Lf=[]
        E=[]
        for i in range(10):
            try:
                self.lf=LabelFrame(self.root,text=self.oil_name[i])
                self.Lf.append(self.lf)
                if i<2:
                    self.Lf[i].grid(row=i,column=0,padx=10,pady=10,sticky=W)
                if 2<=i<4:
                    self.Lf[i].grid(row=i-2,column=1,padx=10,pady=10,sticky=W)
                if 4<=i<6:
                    self.Lf[i].grid(row=i-4,column=2,padx=10,pady=10,sticky=W)
            except:
                continue
        #输入框布局
        E=[]
        for i in range(10):
            e0=[]
            for j in range(10):
                try:
                    e0.append(Entry(self.Lf[i],textvariable=self.oil_value[i][j]))
                except:
                    continue
            E.append(e0)
        
        for i in range(10):
            for j in range(10):
                try:
                    E[i][j].grid(row=j,column=0)
                except:
                    continue
        #单位布局
        for i in range(10):
            for j in range(10):
                try:
                    self.lb=Label(self.Lf[i],text=self.oil_unit[i][j])
                    self.lb.grid(row=j,column=1,padx=10,pady=10,sticky=W)
                except:
                    continue
        #按钮布局
        btn=[[]]*6
        btn[0]=Button(self.Lf[0],text='计算',command=self.cal_len)
        btn[1]=Button(self.Lf[1],text='计算',command=self.cal_p)
        btn[2]=Button(self.Lf[2],text='计算',command=self.cal_q)
        btn[3]=Button(self.Lf[3],text='计算',command=self.cal_ro)
        btn[4]=Button(self.Lf[4],text='计算',command=self.cal_u)
        btn[5]=Button(self.Lf[5],text='计算',command=self.cal_t)
        for i in range(6):
            btn[i].grid(row=0,column=3,padx=10,pady=10,sticky=W)
        
                    
        
# =============================================================================
# 归零函数
# =============================================================================
    def zero(self):
        for i in range(10):
            for j in range(10):
                try:
                    self.oil_value[i][j].set(0)
                except:
                    continue
# =============================================================================
# 长度计算函数
# =============================================================================
    def cal_len(self):
        for i in range(10):
            try:
                if self.oil_value[0][i].get()!=0:
                    length=self.oil_value[0][i].get()
                    print(length)
                    if i==0:
                        length=length
                    if i==1:
                        length=length/3.2808
                    if i==2:
                        length=length*1e-6
                    break
                else:
                    length=0
            except:
                continue
                
        print(length)
        self.oil_value[0][0].set(length)
        self.oil_value[0][1].set(3.2808*length)
        self.oil_value[0][2].set(10**6*length)
            
            
# =============================================================================
# 压力计算函数
# =============================================================================
    def cal_p(self):
        for i in range(10):
            try:
                if self.oil_value[1][i].get()!=0:
                    pressure=self.oil_value[1][i].get()
                    print(pressure)
                    if i==0:
                        pressure=pressure*1e6
                    if i==1:
                        pressure=pressure*1e3
                    if i==2:
                        pressure=pressure
                    if i==3:
                        pressure=pressure*1e-3
                    if i==4:
                        pressure=pressure/145*1e6
                    if i==5:
                        pressure=pressure/9.8692*1e6
                    if i==6:
                        pressure=pressure*1e6/10
                    if i==7:
                        pressure=pressure*1e6/101.972

                    break
                else:
                    pressure=0
            except:
                continue
                
        print(pressure)
        self.oil_value[1][0].set(pressure/1e6)
        self.oil_value[1][1].set(pressure/1e3)
        self.oil_value[1][2].set(pressure)
        self.oil_value[1][3].set(pressure*1e3)
        self.oil_value[1][4].set(pressure*145/1e6)
        self.oil_value[1][5].set(pressure/1e6*9.8692)
        self.oil_value[1][6].set(pressure/1e6*10)
        self.oil_value[1][7].set(pressure/1e6*101.972)
        
# =============================================================================
# 产量计算函数
# =============================================================================
    def cal_q(self):
        for i in range(10):
            try:
                if self.oil_value[2][i].get()!=0:
                    q=self.oil_value[2][i].get()
                    print(q)
                    if i==0:
                        q=q*0.159
                    if i==1:
                        q=q
                    if i==2:
                        q=q*1.1357


                    break
                else:
                    q=0
            except:
                continue
                
        print(q)
        self.oil_value[2][0].set(q/0.159)
        self.oil_value[2][1].set(q)
        self.oil_value[2][2].set(q/1.1357)

# =============================================================================
# 密度计算函数   
# =============================================================================
    def cal_ro(self):
        for i in range(10):
            try:
                if self.oil_value[3][i].get()!=0:
                    ro=self.oil_value[3][i].get()
                    print(ro)
                    if i==0:
                        ro=ro*1000
                    if i==1:
                        ro=ro
                    if i==2:
                        ro=ro*16.02
                    break
                else:
                    ro=0
            except:
                continue
                
        print(ro)
        self.oil_value[3][0].set(ro/1000)
        self.oil_value[3][1].set(ro)
        self.oil_value[3][2].set(ro/16.02)
    
# =============================================================================
# 粘度计算函数
# =============================================================================
    def cal_u(self):
        for i in range(10):
            try:
                if self.oil_value[4][i].get()!=0:
                    u=self.oil_value[4][i].get()
                    print(u)
                    if i==0:
                        u=u
                    if i==1:
                        u=u*1000
                    if i==2:
                        u=u
                    break
                else:
                    u=0
            except:
                continue
                
        print(u)
        self.oil_value[4][0].set(u)
        self.oil_value[4][1].set(u/1000)
        self.oil_value[4][2].set(u)

# =============================================================================
# 粘度计算函数
# =============================================================================
    def cal_t(self):
        for i in range(10):
            try:
                if self.oil_value[5][i].get()!=0:
                    t=self.oil_value[5][i].get()
                    print(t)
                    if i==0:
                        t=t
                    if i==1:
                        t=t-273.15
                    if i==2:
                        t=(t-32)/1.8
                    break
                else:
                    t=0
            except:
                continue
                
        print(t)
        self.oil_value[5][0].set(t)
        self.oil_value[5][1].set(t+273.15)
        self.oil_value[5][2].set(32+t*1.8)        

if __name__=='__main__':
    main=main()

