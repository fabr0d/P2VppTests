# -*- coding: utf-8 -*-
#
# Developed by Haozhe Xie <cshzxie@gmail.com>

import cv2
import matplotlib.pyplot as plt
import os

from mpl_toolkits.mplot3d import Axes3D


def get_volume_views(volume, save_dir, epochID, sampleName, taxonomyId):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    volume = volume.squeeze().__ge__(0.5)
    fig = plt.figure()
    ax = fig.gca(projection=Axes3D.name)
    #ax.set_aspect('equal')
    ax.voxels(volume, edgecolor="k")

    #Is reconstructed
    save_path = os.path.join(save_dir, '%s-%s-%s-voxels-Epoch%06d.png' % (taxonomyId, sampleName, '3DRecons', epochID))
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()
    return cv2.imread(save_path)
