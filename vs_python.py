import numpy as np
import torch

a = torch.Tensor(3,5)
b = torch.Tensor(3,5)
a = a.add(b)
a=a.numpy()
print(a)
