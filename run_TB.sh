#!/bin/bash
pkill tensorboard
nohup tensorboard --logdir="$PWD/hpmser_runs" >/dev/null 2>&1 &
