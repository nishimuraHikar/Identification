import doutei

datafile = 'y_data.csv' # 加速度とトルクを含むファイル
toruque = doutei.csv2ndarray(datafile, 0) # トルク（csv0列目 
accel = doutei.csv2ndarray(datafile, 3) #加速度（csv3列目）
func = doutei.regression(accel, toruque, 1) # 回帰分析
doutei.graph(accel, toruque, doutei.linspace(accel), func) #グラフ表示 