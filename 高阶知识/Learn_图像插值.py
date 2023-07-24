import torch
import torch.nn.functional as F

img = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
print(img*10)
print('-'*100)
img = torch.unsqueeze(torch.unsqueeze(img, dim=0), dim=0)
Img = F.interpolate(img, scale_factor=2, mode='bilinear')
print(Img*10)



