# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



import numpy as np



from .LSTM import LSTMClassifier
from .CNN import CNN

def setup(opt):
    
    if opt.model == 'lstm':
        model = LSTMClassifier(opt)
    elif opt.model == 'cnn':
        model = CNN(opt)
 
    else:
        raise Exception("model not supported: {}".format(opt.model))
    return model
