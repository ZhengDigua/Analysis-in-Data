import numpy
from scipy.signal import savgol_filter
import os

"""
 * Savitzky-Golay平滑滤波函数
 * data - list格式的1×n纬数据
 * window_size - 拟合的窗口大小
 * rank - 拟合多项式阶次
 * ndata - 修正后的值
"""
def savgol(data, window_size, rank):
    m = (window_size - 1) / 2
    odata = data[:]
    # 处理边缘数据，首尾增加m个首尾项
    for i in range(m):
        odata.insert(0,odata[0])
        odata.insert(len(odata),odata[len(odata)-1])
    # 创建X矩阵
    x = create_x(m, rank)
    # 计算加权系数矩阵B
    b = (x * (x.T * x).I) * x.T
    a0 = b[m]
    a0 = a0.T
    # 计算平滑修正后的值
    ndata = []
    for i in range(len(data)):
        y = [odata[i + j] for j in range(window_size)]
        y1 = np.mat(y) * a0
        y1 = float(y1)
        ndata.append;

def readTxtFile(filepath):
    files = os.listdir(filepath);
    for file in files:
        if file[-8:] == "ndvi.txt":
            day = [];
            ndvis = [];
            print(file);
            file_path = os.path.join(filepath,file);
            with open(file_path, "r") as f:
                for line in f.readlines():
                    data = line.split( );
                    print(data)
                    if float(data[1]) != -9999.0:
                        day.append(data[0]);
                        ndvis.append(float(data[1]));
            ndvi_sg = savgol_filter(ndvis, 7, 2);
            ndvi_sg2 = savgol_filter(ndvi_sg, 7, 2);
            ndvi_sg3 = savgol_filter(ndvi_sg2,7,2);
            ndvi_sg4 = savgol_filter(ndvi_sg3,7,2);
            ndvi_sg5 = savgol_filter(ndvi_sg4,7,2);
            ndvi_sg6 = savgol_filter(ndvi_sg5, 7, 2);
            output = file[:-8] + "ndvi_sg.txt";
            with open(output, "w") as w:
                for i in range(0, len(ndvi_sg)):
                    str = day[i] + "\t" + format(ndvi_sg[i], '10.5f') + "\n";
                    w.write(str);
            output = file[:-8] + "ndvi_sg2.txt";
            with open(output, "w") as w:
                for i in range(0, len(ndvi_sg2)):
                    str = day[i] + "\t" + format(ndvi_sg2[i], '10.5f') + "\n";
                    w.write(str);
            output = file[:-8] + "ndvi_sg3.txt";
            with open(output, "w") as w:
                for i in range(0, len(ndvi_sg3)):
                    str = day[i] + "\t" + format(ndvi_sg3[i], '10.5f') + "\n";
                    w.write(str);
            output = file[:-8] + "ndvi_sg4.txt";
            with open(output, "w") as w:
                for i in range(0, len(ndvi_sg4)):
                    str = day[i] + "\t" + format(ndvi_sg4[i], '10.5f') + "\n";
                    w.write(str);
            output = file[:-8] + "ndvi_sg5.txt";
            with open(output, "w") as w:
                for i in range(0, len(ndvi_sg5)):
                    str = day[i] + "\t" + format(ndvi_sg5[i], '10.5f') + "\n";
                    w.write(str);
            output = file[:-8] + "ndvi_sg6.txt";
            with open(output, "w") as w:
                for i in range(0, len(ndvi_sg6)):
                    str = day[i] + "\t" + format(ndvi_sg6[i], '10.5f') + "\n";
                    w.write(str);

def getTestTxtFile(filepath):
    files = os.listdir(filepath);
    for file in files:
        if file[:4] == "ndvi":
            day = [];
            ndvis = [];
            print(file);
            file_path = os.path.join(filepath,file);
            with open(file_path, "r") as f:
                for line in f.readlines():
                    data = line.split( );
                    if float(data[1]) != -9999.0:
                        day.append(data[0]);
                        ndvis.append(float(data[1]));
            ndvi_sg = savgol_filter(ndvis, 7, 2);
            ndvi_sg2 = savgol_filter(ndvi_sg, 7, 2);
            ndvi_sg3 = savgol_filter(ndvi_sg2,7,2);
            ndvi_sg4 = savgol_filter(ndvi_sg3,7,2);

            output = file[5:-4] + "_ndvi_sg4.txt";
            with open(output, "w") as w:
                for i in range(0, len(ndvi_sg4)):
                    str = day[i] + "\t" + format(ndvi_sg4[i], '10.5f') + "\n";
                    print(str);
                    w.write(str);

if __name__ == '__main__':
    getTestTxtFile("D:\\测试_NDVI");
    #readTxtFile("D:\\test_NDVI");
    print("It's OK!");