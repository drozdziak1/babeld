#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys

cmd = "./babeld -I /tmp/babeld.pid -L /tmp/babeld.log -H 1 -h 1 -w babel-nc"

os.system(cmd)
