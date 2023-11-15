import torch
from torch.nn import Module

class Mymodel(Module):

    def __init__(self, mytensor:torch.Tensor, elem_add:int, ele_multiply:int):
        super().__init__()
        self.mytensor= mytensor
        self.elem_add = elem_add
        self.elem_multiply = ele_multiply

    def forward(self, x:torch.Tensor):
        problem2_out = x + self.mytensor
        problem3_out = problem2_out + self.elem_add
        problem4_out = problem3_out * self.elem_multiply

        return problem2_out, problem3_out, problem4_out

        
    
if __name__ == "__main__":
    mymodel = Mymodel(torch.ones((3, 3)), 4, 6)
    p2out, p3out, p4out = mymodel.forward(torch.full((3, 3), 2))

    print("===== problem 2 =====")
    print(repr(p2out))
    print("===== problem 3 =====")
    print(repr(p3out))
    print("===== problem 4 =====")
    print(repr(p4out))