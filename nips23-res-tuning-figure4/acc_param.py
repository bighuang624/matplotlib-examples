import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import random

font_size_global = 12
font_size_legend = 10
font_size_axis = 14
plt.rcParams['font.size'] = font_size_global
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.sans-serif']=['Helvetica Neue']
# plt.rc('font',family='Times New Roman')

# plt.rcParams['font.sans-serif'] = ['Arial']  # 如果要显示中文字体,则在此处设为：SimHei
# plt.rcParams['axes.unicode_minus'] = False  # 显示负号
# plt.rcParams['xtick.direction'] = 'in'

name_list = ["Linear", "Adapter", "VPT-Deep", "SSF", "NOAH", "Res-Tuning", "Full"]
# x_list = [0.04, 1.82, 0.60, 0.24, 0.42, 0.55, 2]
# x_list_axis = [0.04, 1.82, 0.60, 0.24, 0.42, 0.55, 3]
# x_list_axis = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5]
# x_list_axis_name = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5]
# x_list_axis_name = [0.04, 1.82, 0.60, 0.24, 0.42, 0.55, 85.84]


x_list = [0.04, 0.78, 0.60, 0.24, 0.42, 0.55, 1.5]
x_list_axis = [0, 0.15, 0.3, 0.45, 0.6, 0.8, 1.5]
x_list_axis_name = [0, 0.15, 0.3, 0.45, 0.6, 2.0, 85.54]

y_list = [52.94, 56.35, 69.43, 73.10, 73.25, 74.30, 65.57] # arxiv


color_list = ["#A7A7A7", "#4F73C4", "#5E9CD4", "#FFC106","#D87E15",  "#79b835", "#CD534C"]

plt.figure(figsize=(5, 4), dpi=1000)
plt.grid(linestyle="-", color='lightgray', zorder=0)  # 设置背景网格线为虚线
ax = plt.gca()
# ax.spines['top'].set_visible(False)  # 去掉上边框
# ax.spines['right'].set_visible(False)  # 去掉右边框
ax.spines['bottom'].set_color('lightgray')
ax.spines['left'].set_color('lightgray')
ax.spines['top'].set_color('lightgray')
ax.spines['right'].set_color('lightgray')
ax.xaxis.label.set_color('dimgrey')
ax.yaxis.label.set_color('dimgrey')

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
# ax.xaxis.set_ticks_position('bottom')#令x轴为底边缘
# ax.yaxis.set_ticks_position('left')#令y轴为左边缘
# ax.spines['bottom'].set_position(('data',0))#将底边缘放到 y轴数据0的位置
# ax.spines['left'].set_position(('data',1))#将左边缘放到 x轴数据-5的位置


for i, (x, y) in enumerate(zip(x_list, y_list)):
    color = color_list[i]
    label = name_list[i]
    plt.scatter(x, y, s=500, color=color, edgecolors="none", clip_on=False, zorder=100,)
    # plt.annotate(label, xy=(x, y), xytext=(x - 0.2, y - 3))
    # plt.scatter(x, y)
    print(x, y)


plt.xticks(x_list_axis, x_list_axis_name, fontsize=font_size_global)  # 默认字体大小为10
plt.yticks(fontsize=font_size_global)
# plt.title("example", fontsize=12, fontweight='bold')  # 默认字体大小为12
plt.xlabel("Param. (M)", fontsize=font_size_axis)
plt.ylabel("Top-1 Acc. (%)", fontsize=font_size_axis)
plt.xlim(0, 1.5)  # 设置x轴的范围
plt.ylim(50, 80)
#
plt.legend(loc=1, numpoints=1, prop={'size': 8}, labelspacing=1.1, framealpha=0.0)  #显示各曲线的图例
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=font_size_legend, color='k')  # 设置图例字体的大小和粗细

plt.tick_params(axis='x',colors='dimgrey')
plt.tick_params(axis='y',colors='dimgrey')
# plt.xticks([])

# plt.savefig('./infer_dis.svg', format='svg')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
# plt.savefig('./acc_param.png', format='png', bbox_inches='tight', )
plt.savefig('./acc_param_arxiv.png', format='png', bbox_inches='tight', )
# plt.show()