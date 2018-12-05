#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import select
import signal
import shlex
import subprocess
import sys

BABELD_PROCESS = None

def sig_handler(signum, frame):
    if BABELD_PROCESS is not None:
        BABELD_PROCESS.terminate()

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

sys.stdout.flush()
attribs = json.loads(input())

cmd = './babeld -I /tmp/babeld-{node}.pid -L /tmp/babeld-{node}.log -G 6872 -H 1 -h 1 -w {ifaces}'.format(node=attribs['node_name'], ifaces=' '.join(attribs['interfaces']))

with open('/tmp/meshinery-debug-{}'.format(attribs['node_name']), 'w') as f:
    print(cmd, file=f)

cmd_chopped = shlex.split(cmd)

sys.stdout.flush()

BABELD_PROCESS = subprocess.Popen(cmd_chopped, stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

sys.stdout.flush()

stdout, stderr = BABELD_PROCESS.communicate()

print('Babel stdout:\n{out}\nBabel stderr:\n{err}'.format(out=stdout, err=stderr))
sys.stdout.flush()
