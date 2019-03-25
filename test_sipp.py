#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test_sipp.py
#   Usage: python test_sipp.py config_file config_sec

from sipp import sipp_func
import sys

if __name__ == '__main__':
    sipp = sipp_func.sipp_func(sys.argv[1], sys.argv[2])
    sipp.test()

