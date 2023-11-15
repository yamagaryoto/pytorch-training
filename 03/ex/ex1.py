import torch
import numpy as np

if __name__=="__main__":
    data = np.array([
        [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
        [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
        [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
    ])
    data_tensor = torch.tensor(data, dtype=float)
    print("1:", data_tensor)
    data_tensor1 = torch.permute(data_tensor, (2, 0, 1))
    print("2:", data_tensor1)
    data_tensor2 = data_tensor1[0] + data_tensor1[1]
    print("3:", data_tensor2)
    data_tensor3 = data_tensor2.mean(dim=1)
    print("4:", data_tensor3)
    x = data_tensor2.sum(dim=1)
    y = data_tensor2.size(dim=1)
    data_tensor4 = x / y
    print("5:", data_tensor4)
