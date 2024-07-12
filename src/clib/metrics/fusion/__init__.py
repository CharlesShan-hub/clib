'''
 * 方法(): 默认输入都是 0-1 的张量
 * 方法_metric(): 默认输入都是 0-1 的张量, 但会调整调用方法()的输入，会与 VIFB 一致
 * 方法_approach_loss()：默认输入都是 0-1 的张量，用于趋近测试
 *
'''

# 信息论
from .ce import *              # VIFB - 交叉熵
# from metrics.en import *       # VIFB - 信息熵
# from metrics.te import *       # MEFB - tsallis熵
# from metrics.mi import *       # VIFB - 互信息
# from metrics.nmi import *      # MEFB - 标准化互信息
# from metrics.q_ncie import *   # MEFB - 非线性相关性
# from metrics.snr import *      # Many - 信噪比
# from metrics.psnr import *     # VIFB - 峰值信噪比
# from metrics.cc import *       # Tang - 相关系数
# from metrics.scc import *
# from metrics.scd import *      # Tang - 差异相关和

# 结构相似性
# from metrics.ssim import *     # VIFB - 结构相似度测量
# from metrics.ms_ssim import *  # Tang - 多尺度结构相似度测量
# from metrics.q_s import *      # MEFB - 利用 SSIM 的指标 Piella's Fusion Quality Index
# from metrics.q_w import *      # MEFB - 利用 SSIM 的指标 Weighted Fusion Quality Index
# from metrics.q_e import *      # MEFB - 利用 SSIM 的指标 Piella's Edge-dependent Fusion Quality Index
# from metrics.q_c import *      # MEFB - Cvejic
# from metrics.q_y import *      # MEFB - Yang
# from metrics.mb import *       # Mean bias
# from metrics.eme import *
# from metrics.mae import *
# from metrics.mse import *      # VIFB - 均方误差
# from metrics.rmse import *     # VIFB - 均方误差
# from metrics.nrmse import *    # Normalized Root Mean Square Error
# from metrics.ergas import *    # Normalized Global Error
# from metrics.q_h import *      # OB
# from metrics.q import *        # REV
# from metrics.wfqi import *
# from metrics.efqi import *

# 图片信息
from .ag import *              # VIFB - 平均梯度
# from metrics.ei import *       # VIFB - 边缘强度
# # from metrics.pfe import *      # Many
# from metrics.sd import *       # VIFB - 标准差
# from metrics.sf import *       # VIFB - 空间频率
# from metrics.q_sf import *     # OE - 基于空间频率的指标
# from metrics.q_abf import *    # VIFB - 基于梯度的融合性能
# from metrics.eva import *      # Zhihu - 点锐度
# from metrics.asm import *      # Zhihu - 角二阶矩 - 不可微!!!
# from metrics.sam import *      # Zhihu - 光谱角测度 - 要修改
# from metrics.con import *      # 对比度
# from metrics.fmi import *      # OE - fmi_w(Discrete Meyer wavelet),fmi_g(Gradient),fmi_d(DCT),fmi_e(Edge),fmi_p(Raw pixels (no feature extraction))
# from metrics.q_p import *      # MEFB
# from metrics.n_abf import *    # Tang - 基于噪声评估的融合性能
# from metrics.pww import *      # Many - Pei-Wei Wang's algorithms

# 视觉感知
# from metrics.q_cv import *     # VIFB - H. Chen and P. K. Varshney
# from metrics.q_cb import *     # VIFB - 图像模糊与融合的质量评估 包含 cbb,cbm,cmd
# from metrics.vif import *      # 视觉保真度 - 不可微!! 优化用 VIFF 就行
# from metrics.viff import *     # Tang - 视觉保真度

# 新指标暂时没分类
# # from metrics.df import *       #
# # from metrics.q_mi import *     #
# # from metrics.q_s import *      #
# # from metrics.q_e import *      #
# # from metrics.uqi import *      # Many
# # from metrics.qi import *       # Many
# # from metrics.theta import *    # Many
# # from metrics.fqi import *      # Many
# # from metrics.fsm import *      # Many
# # from metrics.wfqi import *     # Many
# # from metrics.efqi import *     # Many
# # from metrics.d import *        # Many

# 打开一个注释需要满足的要求
# 1. 更改了 if __main__里边的测试函数
# 2. 写了 Reference
# 3. 下边的字典完善了
# 4. 找到了对应的 matlab 代码


import os
from pathlib import Path
from torchvision import transforms
from torchvision.transforms.functional import to_tensor
from PIL import Image


def load_demo_image():
    # 定义变换
    transform = transforms.Compose([transforms.ToTensor()])
    # 获取当前文件的绝对路径
    current_file_path = Path(__file__).resolve()
    # 定义资源文件夹的相对路径
    RESOURCE_DIR =Path(current_file_path.parent, 'resources')
    # 打开图片
    return [to_tensor(Image.open(Path(RESOURCE_DIR,f'{f}.bmp'))).unsqueeze(0)\
                        for f in ['vis','ir','fused']]
[vis, ir, fused] = load_demo_image()


info_summary_dict = {
    'ce':{
        'type': 'Information Theory',
        'name': 'Cross Entropy',
        'zh': '交叉熵',
        'metric':ce_metric
    },
    'ag':{
        'type': 'Image Feature',
        'name': 'Average Gradient',
        'zh': '平均梯度',
        'metric':ag_metric
    }
}