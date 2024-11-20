# -*- coding: utf-8 -*-

from .flatten import TracingAdapter
from .torchscript import scripting_with_instances, dump_torchscript_IR

try:
    from caffe2.proto import caffe2_pb2 as _tmp
    from caffe2.python import core
    from .api import *
    # caffe2 is optional
except ImportError:
    pass

__all__ = [k for k in globals().keys() if not k.startswith("_")]
