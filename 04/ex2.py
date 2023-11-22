import torch
from torch import nn


if __name__ == "__main__":
    my_tensor = torch.ones((32, 1024))
    fc = nn.Linear(in_features=1024, out_features=256, bias=True)
    print(repr(fc(my_tensor).size()))
    fc2 = nn.Linear(in_features=1024, out_features=2048, bias=True)
    print(repr(fc2(my_tensor).size()))