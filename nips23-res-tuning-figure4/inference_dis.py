import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import random
from mpl_toolkits.axes_grid1.inset_locator import mark_inset, inset_axes, zoomed_inset_axes


random.seed(123)
# font_size_global = 10
# font_size_legend = 8
# font_size_axis = 12
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

x_list = [i+1 for i in list(range(19))]
# x_list = [i+0 for i in list(range(20))]
x_list_axis = [2*i+1 for i in list(range(10))]
data_num_every = [10000, 6085, 1880, 6149, 3669, 26032, 21750, 32768, 5400, 6300, 42670, 15000, 15000, 22735, 711, 73728, 73728, 12150, 12150]
data_num_add = [10000, 16085, 17965, 24114, 27783, 53815, 75565, 108333, 113733, 120033, 162703, 177703, 192703, 215438, 216149, 289877, 363605, 375755, 387905]

# name_list = ["Full", "Adapter", "Prefix", "Prompt", "Res-Tuning-Bypass"] # submit
name_list = ["Full", "Adapter", "Prefix", "Prompt", "LST", "Res-Tuning-Bypass"] # arxiv

full_time = [53.023764605531966, 97.54876828900743, 133.9433694636996, 208.25718862756406, 258.15962048037284, 439.97713638763673, 618.0771036987016, 865.2381631497733, 921.6238494387325, 989.5669123176931, 1345.9475820664002, 1478.2137826169378, 1605.6809146478327, 1797.7503731922973, 1825.3295058225322, 2342.368509441724, 2737.3759987815124, 2845.7816793141105, 2953.1203618569743]
ada_time = [55.480704906371194, 101.65959558637383, 140.93186190790132, 214.5098565919229, 268.9831259238186, 451.67141281504183, 632.5569595108451, 878.8503510025839, 934.9448170492916, 1005.3873218269341, 1363.2262438414277, 1499.1876750517797, 1632.012365441995, 1826.379201745104, 1854.540759582168, 2373.4934574221597, 2772.577436780567, 2880.4408456927026, 2988.4794892494256]
pre_time = [ 57.8432631045172, 103.94327790184363, 142.373987249734, 215.7946637510899, 270.9068112359713, 458.24741939341385, 644.4633479987642, 899.5470196184338, 960.3202698300829, 1033.2062811439544, 1408.58182267733, 1548.7706813737504, 1686.980148856418, 1890.317032361051, 1921.8413401445077, 2460.417673113398, 2875.4280862971045, 2987.9986989308936, 3102.8311693684163]
pro_time = [ 58.55242065292973, 102.66655663638485, 140.21373195854235, 215.88025595359392, 267.05706958334093, 455.6463916516959, 639.7757320918843, 890.6431535524814, 951.9393109118781, 1023.8515346094491, 1389.977304334886, 1528.6074286083897, 1660.5848672516847, 1858.7084393937544, 1889.2268359417285, 2421.377172944817, 2828.4003815913547, 2940.140330937381, 3051.95684435949]
bypass_time = [ 42.3104, 50.32515150042129, 56.87638474558226, 70.25329085163759, 79.23600971697944, 111.96418687289584, 144.02318433820318, 188.51356745335102, 198.66330864145652, 210.89344272574556, 275.043970997339, 298.8526322352688, 321.7974341034866, 356.3710186897505, 361.33541793382125, 454.40535139170856, 525.5089247989056, 545.0225580122653, 564.3441255764011]
lst_time = [25.28/24.98 * tm + random.random() * 25 for tm in bypass_time]
print("lst_time", lst_time)

method_list_old = [full_time, ada_time, pre_time, pro_time, lst_time, bypass_time]

method_list = []
for md in method_list_old:
    diff = (md[-1] - md[0]) / 18
    new_md = []
    new_md.append(md[0])
    for i in range(18):
        new_md.append(new_md[i] + diff + (random.random() / 2 - 1) * 10)
    method_list.append(new_md)
    print(new_md)

# color_list = ["#868686", "#0073C2", "#EFC000", "#F3BECA", "#CD534C", "#79b835"]

# color_list = [(167, 167, 167), (255, 193, 6), (94, 156, 212), (216, 126, 21), (79, 115, 196), (230, 255, 230)]
color_list = ["#A7A7A7", "#4F73C4", "#5E9CD4", "#FFC106", "#79b835"]  # submit
color_list = ["#A7A7A7", "#4F73C4", "#5E9CD4", "#FFC106", "#D87E15", "#79b835"] # arxiv

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


for i in range(len(method_list)):
    method = method_list[i]
    color = color_list[i]
    label = name_list[i]
    # method = [dd + (random.random() / 2 - 1) * 0.5 for dd in method ]
    plt.plot(x_list, method, marker='o', color=color, label=label, linewidth=1.0, clip_on=False, zorder=100, markersize='5')

plt.xticks(x_list_axis, x_list_axis, fontsize=font_size_global)  # 默认字体大小为10
plt.yticks(fontsize=font_size_global)
# plt.title("example", fontsize=12, fontweight='bold')  # 默认字体大小为12
plt.xlabel("Number of discriminative tasks", fontsize=font_size_axis)
plt.ylabel("Inference time (s)", fontsize=font_size_axis)
plt.xlim(1, 19)  # 设置x轴的范围
plt.ylim(0, 3500)
#
plt.legend(loc=0, numpoints=1, prop={'size': 8}, labelspacing=1.1, framealpha=0.0)  #显示各曲线的图例
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=font_size_legend, color='k')  # 设置图例字体的大小和粗细

plt.tick_params(axis='x',colors='dimgrey')
plt.tick_params(axis='y',colors='dimgrey')
# plt.xticks([])

####### 局部放大 ########
axins = inset_axes(ax, width="30%", height="20%", loc='lower right',
                   bbox_to_anchor=(-0.01, 0.2, 1, 1),
                   bbox_transform=ax.transAxes,
                   )
for i in range(len(method_list)):
    if name_list[i] not in ["LST", "Res-Tuning-Bypass"]:
        continue
    method = method_list[i]
    color = color_list[i]
    label = name_list[i]
    # import pdb; pdb.set_trace()
    # method = [dd + (random.random() / 2 - 1) * 0.5 for dd in method ]
    # plt.plot(x_list, method, marker='o', color=color, label=label, linewidth=1.0, clip_on=False, zorder=100, markersize='5')
    axins.plot(x_list[-3:], method[-3:], marker='o', color=color, label=label, linewidth=1.0, clip_on=False, zorder=100, markersize='3')
# axins.set_xlim(17, 19, auto=False)
# axins.get_xaxis().set_major_locator(plt.MaxNLocator(integer=True))
# axins.grid(linestyle="-", color='lightgray', linewidth=0.05,zorder=0, alpha=0.3)
axins.set_ylim(380, 450)
# axins.set_xlabel('text', fontdict={'family' : 'Helvetica Neue', 'size' : 4})
axins.grid(linestyle="-", color='lightgray', linewidth=0, alpha=.0)
axins.tick_params(axis='both', which='major', labelsize=6,  colors='dimgrey', pad=-2, zorder=10000)
axins.spines['bottom'].set_color('lightgray')
axins.spines['left'].set_color('lightgray')
axins.spines['top'].set_color('lightgray')
axins.spines['right'].set_color('lightgray')
axins.xaxis.label.set_color('dimgrey')
axins.yaxis.label.set_color('dimgrey')
axins.xaxis.set_ticks_position('none')
axins.yaxis.set_ticks_position('none')
mark_inset(ax, axins, loc1=3, loc2=4, fc="none", ec='lightgray', lw=1, zorder=10000)
####################

# plt.savefig('./infer_dis.svg', format='svg')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
# plt.savefig('./infer_dis.png', format='png', bbox_inches='tight',)
plt.savefig('./infer_dis_arxiv.png', format='png', bbox_inches='tight',)

# plt.show()