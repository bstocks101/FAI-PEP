#!/usr/bin/env python

##############################################################################
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
##############################################################################


from .caffe2.caffe2 import Caffe2Framework
from .generic.generic import GenericFramework
from .oculus.oculus import OculusFramework

frameworks = {
    'caffe2': Caffe2Framework,
    'generic': GenericFramework,
    'oculus': OculusFramework
}


def getFrameworks():
    global frameworks
    return frameworks
