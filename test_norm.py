import numpy as np

x= np.array([4,3])
# chuẩn hóa để tính ra một đại lượng biểu diễn độ lớn một vector
#L0Norm 
#LONorm :2
l0norm = np.linalg.norm(x, ord= 0)
print(l0norm)


#L1Norm : Khoảng cách Mahattan
l1norm = np.linalg.norm(x, ord = 1)
print(l1norm)

#L2Norm: Khoang cach Euclid
l2norm = np.linalg.norm(x, ord = 2)
print(l2norm)
