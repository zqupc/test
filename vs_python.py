import numpy as np
import torch
import pandas as pd
a = torch.Tensor(3,5)
b = torch.Tensor(3,5)
a = a.add(b)
a=a.numpy()
print(a)
