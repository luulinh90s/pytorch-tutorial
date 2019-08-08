# To create custom dataset from MSCOCO-2014

import torch
from torchvision import transforms, datasets

class_num = 80

data_transform = transforms.Compose([
        transforms.RandomSizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

dataset = datasets.ImageFolder(root='train2014/',
                               transform=data_transform)
dataset_loader = torch.utils.data.DataLoader(dataset,
                                             batch_size=class_num, shuffle=True,
                                             num_workers=4)

pass