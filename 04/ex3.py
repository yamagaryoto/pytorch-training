import torch
from torch import nn
from torch.nn import Module

class MyModel(Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, tensor):
        conv1 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=8)
        out1 = conv1(tensor)
        norm = nn.BatchNorm2d(num_features=256)
        out2 = norm(out1)
        relu = nn.ReLU()
        out3 = relu(out2)
        fc = nn.Linear(in_features=256*16*16, out_features=64, bias=True)
        out4 = fc(out3.view(-1, 256*16*16))
        return out4


if __name__ == "__main__":
    in_tonsor = torch.ones((32, 3, 128, 128))
    model = MyModel()
    out = model.forward(in_tonsor)
    print(out.size())