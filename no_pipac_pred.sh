#!/bin/bash

# 모델 경로
MODEL_PATH=./result/stage2/models
# 루트 이미지 경로
BASE_PATH=/media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned/test_set

# 모든 keyframe image 경로 순회
find "$BASE_PATH" -type d -path "*/keyframe*/image_02/data" | while read -r image_path; do
    echo "Running prediction on: $image_path"
    CUDA_VISIBLE_DEVICES=0 python test_simple.py \
        --model_path "$MODEL_PATH" \
        --image_path "$image_path"
done