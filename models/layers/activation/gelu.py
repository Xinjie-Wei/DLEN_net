#
# For licensing see accompanying LICENSE file.
# Copyright (C) 2020 Apple Inc. All Rights Reserved.
#

from torch import nn, Tensor

from . import register_act_fn


@register_act_fn(name="gelu")
class GELU(nn.GELU):
    def __init__(self):
        super(GELU, self).__init__()

