_base_ = ['./rotated_retinanet_obb_r50_fpn_1x_dota_le90.py']

optim_wrapper = dict(type='AmpOptimWrapper', loss_scale='dynamic')