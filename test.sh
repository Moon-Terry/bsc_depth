# for random videos
# CUDA_VISIBLE_DEVICES=0 python test_simple.py --model_path ./results/mdp/models/weights_19/ --image_path ./dataset/testset_dongin/ 

# for SCARED test set
CUDA_VISIBLE_DEVICES=0 python test_simple.py --model_path ./result/stage2/models/weights_19/ --image_path /media/bigssd2/bsc_depth/SCARED/dataset_6/keyframe_4/image_02/data 

# convert frames to video
# ffmpeg -framerate 25 -i %10d.jpeg -c:v libx264 -pix_fmt yuv420p dataset_#_keyframe_4_prediction.mp4

CUDA_VISIBLE_DEVICES=0 python test_simple.py --model_path ./result/pipac/models/weight_19 --image_path /media/bigssd2/bsc_depth/SCARED/testset...
