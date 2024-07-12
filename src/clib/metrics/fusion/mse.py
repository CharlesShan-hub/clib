import torch
import torch.nn.functional as F

###########################################################################################

__all__ = [
    'mse',
    'mse_approach_loss',
    'mse_metric'
]

def mse(y_true: torch.Tensor, y_pred: torch.Tensor, eps: float = 1e-10) -> torch.Tensor:
    """
    Calculate the Mean Squared Error (MSE) between true and predicted values.

    Args:
        y_true (torch.Tensor): The true values tensor.
        y_pred (torch.Tensor): The predicted values tensor.
        eps (float, optional): A small value to avoid numerical instability. Default is 1e-10.

    Returns:
        torch.Tensor: The MSE between true and predicted values.
    """
    return torch.mean((y_true - y_pred)**2)

mse_approach_loss = mse

def mse_metric(A: torch.Tensor, B: torch.Tensor, F: torch.Tensor) -> torch.Tensor:
    w0 = w1 = 0.5
    return w0 * mse(A, F) + w1 * mse(B, F)

###########################################################################################

def main():
    from torchvision import transforms
    from torchvision.transforms.functional import to_tensor
    from PIL import Image

    torch.manual_seed(42)

    transform = transforms.Compose([transforms.ToTensor()])

    vis = to_tensor(Image.open('../imgs/TNO/vis/9.bmp')).unsqueeze(0)
    ir = to_tensor(Image.open('../imgs/TNO/ir/9.bmp')).unsqueeze(0)
    fused = to_tensor(Image.open('../imgs/TNO/fuse/U2Fusion/9.bmp')).unsqueeze(0)

    print(f'MSE(ir,ir):{mse(ir,ir)}')
    print(f'MSE(ir,vis):{mse(ir,vis)}')
    print(f'MSE(ir,fused):{mse(ir,fused)}')

if __name__ == '__main__':
    main()
