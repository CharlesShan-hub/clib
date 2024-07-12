import torch

###########################################################################################

__all__ = [
    'sd',
    'sd_approach_loss',
    'sd_metric'
]

def sd(tensor: torch.Tensor) -> torch.Tensor:
    """
    Calculate the standard deviation of a tensor.

    Args:
        tensor (torch.Tensor): Input tensor, assumed to be in the range [0, 1].

    Returns:
        torch.Tensor: The standard deviation of the input tensor.

    Reference:
        [1] Y.-J. Rao, "In-fibre bragg grating sensors," Measurement science and technology,
        vol. 8, no. 4, p. 355, 1997.
    """
    return torch.sqrt(torch.mean((tensor - tensor.mean())**2))

# 如果两幅图相等，SD 会一致
def sd_approach_loss(A: torch.Tensor, F: torch.Tensor) -> torch.Tensor:
    return torch.abs(sd(A) - sd(F))

# 与 VIFB 统一
def sd_metric(A: torch.Tensor, B: torch.Tensor, F: torch.Tensor) -> torch.Tensor:
    return sd(F) * 255.0  # 与 VIFB 统一，需要乘 255

###########################################################################################

def main():
    from utils import ir,vis,fused  # type: ignore

    print(f'SD(ir):{sd(ir)}')
    print(f'SD(vis):{sd(vis)}')
    print(f'SD(fused):{sd(fused)}')

if __name__ == '__main__':
    main()
