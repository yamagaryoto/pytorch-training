import torch
from torch import nn

if __name__ == "__main__":
    my_tensor = torch.ones((32, 3, 128, 128))
    conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    print("1:", my_tensor.size())
    print("2:", conv1(my_tensor).size())
    conv3 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    print("3:", repr(conv3(my_tensor).size()))
