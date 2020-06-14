# coding=utf-8
# 利用类似冒泡算法中两两比较的原理，将临近的UV点坐标合并

import maya.cmds as cmds
import pymel.core as pc
import os
from math import sqrt


def multi_merge(threshold):
    selected_uv = cmds.ls(sl=True, flatten=True)
    selected_uv_pos = cmds.polyEditUV(query=True)
    length = len(selected_uv_pos)
    pos_u = [selected_uv_pos[i] for i in range(length) if i % 2 == 0]
    pos_v = [selected_uv_pos[i] for i in range(length) if i % 2 != 0]
    for name in selected_uv:
        current_u, current_v = cmds.polyEditUV(name, query=True)
        for i in range(length / 2):
            if sqrt( (pos_u[i] - current_u) ** 2 + (pos_v[i] - current_v) ** 2 ) < threshold:
                cmds.select(selected_uv[i], r=True)
                cmds.polyEditUV(u=current_u, v=current_v, r=False)
    cmds.select(selected_uv)


multi_merge(0.02)
    
