import click
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets
from torch.utils.data import DataLoader, random_split

from transform import transform
from model import LeNet
from config import TrainOptions
from clib.train import BaseTrainer


@click.command()
@click.option('--model_base_path', type=click.Path(exists=True), required=True)
@click.option('--dataset_path', type=click.Path(exists=True), required=True)
@click.option('--num_classes', type=int, default=10, show_default=True)
@click.option('--use_relu', type=bool, default=False, show_default=True)
@click.option('--use_max_pool', type=bool, default=False, show_default=True)
@click.option('--train_mode', type=str, default='Holdout', show_default=False)
@click.option('--seed', type=int, default=42, show_default=True, required=False)
@click.option('--epoch', type=int, default=2, show_default=True, required=False)
@click.option('--batch_size', type=int, default=8, show_default=True, required=False)
@click.option('--lr', type=float, default=0.03, show_default=True, required=False)
@click.option('--factor', type=float, default=0.1, show_default=True, required=False)
@click.option('--repeat', type=int, default=2, show_default=True, required=False)
@click.option('--val', type=float, default=0.8, show_default=True, required=False)
@click.option('--comment', type=str, default="", show_default=False)
def train(model_base_path,dataset_path,num_classes,use_relu,use_max_pool,\
          train_mode,seed,epoch,batch_size,lr,factor,repeat,val,comment):

    opts = TrainOptions().parse({
        'model_base_path': model_base_path,
        'dataset_path': dataset_path,
        'num_classes': num_classes,
        'use_relu': use_relu,
        'use_max_pool': use_max_pool,
        'train_mode': train_mode,
        'seed': seed,
        'epoch': epoch,
        'batch_size': batch_size,
        'lr': lr,
        'factor': factor,
        'repeat': repeat,
        'val': val,
        'comment': comment
    },present=True)

    trainer = BaseTrainer(opts)
    trainer.model = LeNet(
        num_classes=opts.num_classes,
        use_max_pool=opts.use_max_pool,
        use_relu=opts.use_relu
    )
    trainer.criterion = nn.CrossEntropyLoss()
    trainer.optimizer = optim.Adam(
        params=trainer.model.parameters(), 
        lr=opts.lr
    )
    trainer.transform = transform
    train_dataset = datasets.MNIST(
        root=opts.dataset_path, 
        train=True, 
        download=True, 
        transform=trainer.transform
    )
    test_dataset = datasets.MNIST(
        root=opts.dataset_path, 
        train=False,
        download=True, 
        transform=trainer.transform
    )
    val_size = int(opts.val * len(train_dataset)) 
    train_size = len(train_dataset) - val_size
    train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])
    trainer.train_loader = DataLoader(dataset=train_dataset, batch_size=opts.batch_size, shuffle=True)
    trainer.val_loader = DataLoader(dataset=val_dataset, batch_size=opts.batch_size, shuffle=True)
    trainer.test_loader = DataLoader(dataset=test_dataset, batch_size=opts.batch_size, shuffle=True)
    trainer.train()

if __name__ == '__main__':
    train()