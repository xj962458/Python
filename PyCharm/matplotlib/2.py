import matplotlib.pyplot as pltdatas=[1,2,3,4,5]squares=[1,4,9,16,25]plt.plot(datas,squares,linewidth=5) #设置线条宽度#设置中文乱码问题plt.rcParams['font.sans-serif'] = ['SimHei']#设置图标标题，并在坐标轴上添加标签plt.title('折线图',fontsize=24)plt.xlabel('x轴',fontsize=14)plt.ylabel('y轴',fontsize=14)plt.show()