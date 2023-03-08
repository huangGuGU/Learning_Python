from PIL import Image
import torch
from torchvision import transforms
import matplotlib.pyplot as plt



path = r'/Users/hzh/Desktop/x.png'
img = Image.open(path).convert('L')
img = transforms.ToTensor()(img)
img = transforms.Resize((100,100))(img)
img_k = torch.fft.fft2(img)
img_k =torch.fft.fftshift(img_k)

img_done = torch.abs(torch.fft.ifft2(img_k))

img_done = torch.squeeze(img_done,0)
plt.subplot(131)
plt.title('img_FF-1')
plt.imshow(img_done)


img_kk = torch.fft.fft2(img_k)
img_kk = torch.abs(img_kk )
img_kk = torch.squeeze(img_kk,0)
plt.subplot(132)
plt.title('img_2F')
plt.imshow(img_kk)

img_kkkk = torch.fft.fft2(torch.fft.fft2(img_kk))
img_kkkk = torch.abs(img_kkkk )
img_kkkk = torch.squeeze(img_kkkk,0)
plt.subplot(133)
plt.title('img_4F')
plt.imshow(img_kkkk)

plt.tight_layout()
plt.show()
