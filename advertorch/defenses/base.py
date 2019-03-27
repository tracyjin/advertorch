# Copyright (c) 2018-present, Royal Bank of Canada.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from abc import ABCMeta
import torch.nn as nn


class Processor(nn.Module):
    """
    Processor
    """
    __metaclass__ = ABCMeta
    def __init__(self):
        """
        Processor
        """
        super(Processor, self).__init__()

    def forward(self, x):
        return x

    def extra_repr(self):
        return 'EmptyDefense (Identity)'
