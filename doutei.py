import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def csv2ndarray(csv, line_num): #csvと列番号を指定
    #csvからndarray型に変換
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])

    # 100行間隔で間引き
    cut_csv = csvdata[1::100]
    # csvから読んだデータをnumpyの行列に入れる
    array = cut_csv.values
    # print(array)
    # 配列の平坦化
    data = array.T[0]
    # print(data)
    return data

#回帰分析
def regression(x, y, n): #xを引数としたyのn次多項式
    z = np.polyfit(x, y, n) #最小二乗法近似計算
    p = np.poly1d(z) #多項式のオブジェクト生成
    print(z)  # 係数表示．[傾き，切片]
    return p

def linspace(x):
    return np.linspace(min(x), max(x), 500)

# グラフ表示
def graph(x_raw, y_raw, x_acc, y_tor):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 14
    plt.rcParams["axes.linewidth"] = 1.5

    plt.scatter(x_raw, y_raw, label="Raw")
    plt.plot(x_acc, y_tor(x_acc), c="red", label="Liner approximation")
    plt.ylim(min(y_raw), max(y_raw))
    plt.xlabel("Acceleration", fontname = 'Times New Roman')
    plt.ylabel("Torque", fontname = 'Times New Roman')
    plt.legend()
    plt.savefig('y_doutei.png') #PNGファイル生成
    plt.show()