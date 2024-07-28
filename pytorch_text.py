import torch
torch.__version__

x = torch.empty(5,3)
print(x)

x = torch.zeros(5,3,dtype=torch.double)
print(x)