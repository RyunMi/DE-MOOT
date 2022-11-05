import matplotlib.pyplot as plt
import pandas as pd
from math import pi
plt.style.use('science')
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'Obj 1': [1,1.1049,0.94374,0.94345],
    'Obj 4': [0.0796,0.4973,0.0702,0.31953],
    'Obj 2' : [1,1.6107,0.175,0.13266],
    'Obj 3': [1,2.1015,1.0204,0.90687],
})


# 变量类别
lei=list(df)[1:]
# 变量类别个数
Num=len(lei)

# 设置每个点的角度值
angles = [n / float(Num) * 2 * pi for n in range(Num)]
angles += angles[:1]

# 初始化极坐标网格
ax = plt.subplot(111, polar=True)

# 设置角度偏移
ax.set_theta_offset(pi/2)
# 设置顺时针还是逆时针，1或者-1
ax.set_theta_direction(-1)

# 设置x轴的标签
plt.xticks(angles[:-1],lei)

# 画标签
ax.set_rlabel_position(0)
plt.yticks([1, 2], ["$1$",'$2$'], color="black", size=15)
#plt.ylim(0, 0.068)


# 单独绘制每一组数据
xs = df.loc[0].drop('group').values.flatten().tolist()
xs +=xs[:1]
ax.plot(angles,xs,linewidth=1,linestyle='solid',label="History min",color='#ffcf7f')
ax.fill(angles,xs,alpha=0.3,color='#ffcf7f')

xs = df.loc[1].drop('group').values.flatten().tolist()
xs +=xs[:1]
ax.plot(angles,xs,linewidth=1,linestyle='solid',label="History mean",color='#c4d6a0')
ax.fill(angles,xs,alpha=0.3,color='#c4d6a0')

xs = df.loc[2].drop('group').values.flatten().tolist()
xs +=xs[:1]
ax.plot(angles,xs,linewidth=1,linestyle='solid',label="Predict 50",color='#aacbd5')
ax.fill(angles,xs,alpha=0.3,color='#aacbd5')


xs = df.loc[3].drop('group').values.flatten().tolist()
xs +=xs[:1]
ax.plot(angles,xs,linewidth=1,linestyle='solid',label="Predict 402",color='#da968f')
ax.fill(angles,xs,alpha=0.4,color='#da968f')

# 添加图例
plt.legend(fontsize=20,loc='upper right',bbox_to_anchor=(0, 0.3))

plt.show()