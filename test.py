import numpy as np

# 建立一個 4x5 全為 0 的矩陣
result1 = np.zeros([4, 5])
print(result1)

# 建立一個 4x5 全為 1 的矩陣
result2 = np.ones([2, 3])
print(result2)

# 建立一個 1 開始，最大到 10 一次加 2 的矩陣
result3 = np.arange(1, 11, 2)
print(result3)

# 建立一個 0 到 6 平均分成 3 份的矩陣 [0 3 6]
result4 = np.linspace(0, 10, 3)
print(result4)

# 建立一個 2x3 的矩陣，裡面的元素全都是 7
result5 = np.full([2, 2], 7)
print(result5)

# 建立一個 3x3 的單位矩陣
result6 = np.eye(5)
print(result6)

# 建立 2x3 的矩陣，元素的值為隨機的
result7 = np.random.random([2, 3])
print(result7)