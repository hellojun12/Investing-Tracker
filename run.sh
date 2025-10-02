#!/bin/bash
# 현재 경로를 PYTHONPATH로 고정해서 Python 실행
export PYTHONPATH=$(pwd)
echo "PYTHONPATH set to: $PYTHONPATH"
python "$@"
