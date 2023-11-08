import numpy as np

data = np.array([
  [[65, 70], [56, 80], [78, 68], [90, 85], [60, 75]],
  [[70, 75], [54, 88], [82, 64], [88, 83], [58, 78]],
  [[67, 72], [52, 82], [80, 66], [86, 80], [59, 74]]
])

print("Data shape:", data.shape)
print("クラスごとの科目別平均点:", np.mean(data, axis=1))
print("全クラスの番号３番の学生で２科目目の最高得点:", np.max(data[:, 2, 1]))
print("全クラスの各科目の最高得点と最低得点の差:", np.max(np.max(data, axis = 1), axis = 0) - np.min(np.min(data, axis = 1), axis = 0))
print("各クラスの１科目目が８０点以上の人数:", np.sum(data[:, :, 0] > 80, axis = 1))
print("２科目の合計得点が１３５点を超えている人数:", np.sum((data[:, :, 0] + data[:, :, 1]) > 135))
#print("全生徒の１科目目と２科目目の相関係数:", )
