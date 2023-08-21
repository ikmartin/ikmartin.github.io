#!/bin/bash
git --work-tree=/home/ploum/gemlog --git-dir=/home/ploum/gemlog.git checkout -f
cd ~/gemlog/
./publish.py
#~/offpunk/offpunk.py --sync --cache-validity 1
