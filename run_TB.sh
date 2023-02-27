#!/bin/bash
pkill tensorboard
nohup tensorboard --logdir="$PWD/_hpmser_runs" >/dev/null 2>&1 &
