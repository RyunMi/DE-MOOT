#coding=gb2312
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('science')
fig,(ax1,ax2)=plt.subplots(1,2)
A=pd.read_excel('yuce.xlsx',sheet_name='S374')
B=pd.read_excel('yuce.xlsx',sheet_name='S140')
#print(A.loc[1,:])
plt.subplot(1,2,1)
ax=plt.gca()  #gca:get current axis得到当前轴
#设置图片的右边框和上边框为不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
x=range(1,25)
for i in range(10):
    plt.plot(x,B.loc[i,:],color='#439046',linewidth=1.8)
plt.plot(x,B.loc[10,:],label='Predict Data',color='#d95319',linewidth=1.8)
plt.legend(loc='best')
plt.xlabel('Week')
plt.ylabel('Quantity',rotation='horizontal')
ax.yaxis.set_label_coords(0,1.02)
plt.title('Supplier 140',fontsize=18)
plt.subplot(1,2,2)
ax=plt.gca()  #gca:get current axis得到当前轴
#设置图片的右边框和上边框为不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
for i in range(10):
    plt.plot(x,A.loc[i,:],color='#0072bd',linewidth=1.8)
plt.plot(x,A.loc[10,:],label='Predict Data',color='#937bc6',linewidth=1.8)
plt.legend(loc='best')
plt.xlabel('Week')
plt.ylabel('Quantity',rotation='horizontal',)
ax.yaxis.set_label_coords(0,1.02)
plt.title('Supplier 374',fontsize=18)
plt.show()