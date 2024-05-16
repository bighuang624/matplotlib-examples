import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import random

random.seed(123)

# font_size_global = 10
# font_size_legend = 8
# font_size_axis = 12
font_size_global = 12
font_size_legend = 10
font_size_axis = 14
plt.rcParams['font.size'] = font_size_global
# plt.rcParams["font.weight"] = "bold"
# plt.rcParams['font.sans-serif']=['Times New Roman']
plt.rcParams['font.sans-serif']=['Helvetica Neue']
# plt.rc('font',family='Times New Roman')

# plt.rcParams['font.sans-serif'] = ['Arial']  # 如果要显示中文字体,则在此处设为：SimHei
# plt.rcParams['axes.unicode_minus'] = False  # 显示负号
# plt.rcParams['xtick.direction'] = 'in'


x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

name_list = ["SD v1.5", "LoRA", "Adapter", "Prefix", "Prompt", "Res-Tuning-Bypass"]
sd_time = [2.51, 5.06, 7.61, 10.18, 12.73, 15.28, 17.83, 20.38, 22.93, 25.40]
lora_time = [2.70, 5.36, 8.17, 10.82, 13.52, 16.17, 18.82, 21.47, 24.21, 26.80]
ada_time = [2.58, 5.21, 7.86, 10.43, 13.09, 15.68, 18.27, 20.86, 23.45, 25.98]
pre_time = [4.06, 8.13, 12.20, 16.27, 20.33, 24.41, 28.48, 32.56, 36.62, 41.65]
pro_time = [4.09, 8.35, 12.46, 16.55, 20.64, 24.74, 28.85, 32.93, 37.01, 42.06]
bypass_time = [2.65, 2.77, 3.02, 3.16, 3.31, 3.46, 3.60, 3.78, 4.03, 4.17]
method_list = [sd_time, lora_time, ada_time, pre_time, pro_time, bypass_time]

# color_list = ["#868686", "#0073C2", "#EFC000", "#F3BECA", "#CD534C", "#79b835"]

# color_list = [(167, 167, 167), (255, 193, 6), (94, 156, 212), (216, 126, 21), (79, 115, 196), (230, 255, 230)]
color_list = ["#A7A7A7", "#4F73C4", "#5E9CD4", "#FFC106","#D87E15",  "#79b835"]

aa = plt.figure(figsize=(5, 4), dpi=1000)
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


for i in range(len(method_list)):
    method = method_list[i]
    color = color_list[i]
    label = name_list[i]
    method = [dd + (random.random() / 2 - 1) * 0.5 for dd in method ]
    plt.plot(x_list, method, marker='o', color=color, label=label, linewidth=1.0, clip_on=False, zorder=100, markersize='5')

plt.xticks(x_list, x_list, fontsize=font_size_global)  # 默认字体大小为10
plt.yticks(fontsize=font_size_global)
# plt.title("example", fontsize=12, fontweight='bold')  # 默认字体大小为12
plt.xlabel("Number of generative tasks", fontsize=font_size_axis)
plt.ylabel("Inference time (s)", fontsize=font_size_axis)
plt.xlim(1, 10)  # 设置x轴的范围
plt.ylim(0, 45.0)

plt.legend(loc=0, numpoints=1, prop={'size': 8}, labelspacing=1.1, framealpha=0.0)  #显示各曲线的图例
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=font_size_legend, color='k')  # 设置图例字体的大小和粗细

plt.tick_params(axis='x',colors='dimgrey')
plt.tick_params(axis='y',colors='dimgrey')
# plt.xticks([])

# from matplotlib.backends.backend_pdf import PdfPages
# pdf = PdfPages('infer_gen.pdf')
# pdf.savefig(aa)

# plt.savefig('./infer_gen.svg', format='svg')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
plt.savefig('./infer_gen.png', format='png', bbox_inches='tight')
# plt.show()
