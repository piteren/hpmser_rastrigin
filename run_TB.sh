#!/bin/bash
pkill tensorboard
nohup tensorboard --logdir="$PWD/_hpmser" >/dev/null 2>&1 &
