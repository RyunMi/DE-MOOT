import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('science')
fig,(ax1,ax2)=plt.subplots(1,2)
S=pd.read_excel(io=r'../data/402-dataset.xlsx',sheet_name='Supply',usecols="C:IH").values
MT=np.diag(1./(pd.read_excel(io=r'../data/402-dataset.xlsx',sheet_name='Supply',usecols="B").values.flatten()))
s_374=pd.read_excel(io=r'../data/fo_result_402.xlsx',sheet_name='page_1',usecols="NK").T
s_140=pd.read_excel(io=r'../data/fo_result_402.xlsx',sheet_name='page_1',usecols="EK").T
S=np.dot(MT,S)
A=S[373,:].reshape(10,24)
B=S[139,:].reshape(10,24)
A=pd.DataFrame(A)
B=pd.DataFrame(B)
A=pd.concat([A,s_374])
B=pd.concat([B,s_140])
plt.subplot(1,2,1)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
x=range(1,25)
for i in range(10):
    plt.plot(x,B.loc[i,:],color='#439046',linewidth=1.8)
plt.plot(x,B.loc[139,:],label='Predict Data',color='#d95319',linewidth=1.8)
plt.legend(loc='best')
plt.xlabel('Week')
plt.ylabel('Quantity',rotation='horizontal')
ax.yaxis.set_label_coords(0,1.02)
plt.title('Supplier 140',fontsize=18)
plt.subplot(1,2,2)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
for i in range(10):
    plt.plot(x,A.loc[i,:],color='#0072bd',linewidth=1.8)
plt.plot(x,A.loc[373,:],label='Predict Data',color='#937bc6',linewidth=1.8)
plt.legend(loc='best')
plt.xlabel('Week')
plt.ylabel('Quantity',rotation='horizontal',)
ax.yaxis.set_label_coords(0,1.02)
plt.title('Supplier 374',fontsize=18)
plt.show()