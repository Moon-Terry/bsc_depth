- Code path
/home/dongin/repo/AF-SfMLearner

- Data path
/media/bigssd2/bsc_depth/SCARED

- Conda environment
# Login with dongin's account (it's on dongin's directory)
Conda environment: AFlearner

- Model path
./result/stage2/models/weights_19

- Author model path
./result/Model_MIA

- Train model (We followed what authors did)
CUDA_VISIBLE_DEVICES=0 python train_stage_one.py --data_path /media/bigssd2/bsc_depth/SCARED --model_name stage1 --split endovis2 --log_dir ./result
CUDA_VISIBLE_DEVICES=0 python train_stage_two.py --data_path /media/bigssd2/bsc_depth/SCARED --model_name stage2 --split endovis2 --log_dir ./result --load_weights_folder ./result/stage1/models/weights_19
(We dont have stage1 checkpoint now, we deleted it after training)

- Train PIPAC
CUDA_VISIBLE_DEVICES=0 python train_end_to_end.py --data_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned --model_name pipac_no_finetune --log_dir ./result/ --split PIPAC_train 
CUDA_VISIBLE_DEVICES=0 python train_end_to_end.py --data_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned --model_name pipac_more_epoch --log_dir /media/bigssd2/bsc_depth/model_ckpts --split PIPAC_train --load_weights_folder /media/bigssd2/bsc_depth/model_ckpts/stage2/models/ --num_epochs 40 --save_frequency 10

- Evaluation 
# Evaulate the test set on our model
CUDA_VISIBLE_DEVICES=0 python evaluate_depth.py --data_path /media/bigssd2/bsc_depth/SCARED --load_weights_folder /media/bigssd2/bsc_depth/model_ckpts/stage2/models/ --eval_mono --eval_split endovis2
# Evaluate the test set on the author's model
CUDA_VISIBLE_DEVICES=0 python evaluate_depth.py --data_path /media/bigssd2/bsc_depth/SCARED --load_weights_folder ./result/Model_MIA --eval_mono --eval_split endovis2

- Get inferences
CUDA_VISIBLE_DEVICES=0 python test_simple.py --model_path ./result/stage2/models/ --image_path /media/bigssd2/bsc_depth/SCARED/testset...

# PIPAC inferences
CUDA_VISIBLE_DEVICES=0 python test_simple.py --model_path ./result/pipac/models/weights_19/ --image_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned/test_set
CUDA_VISIBLE_DEVICES=0 python test_simple.py --model_path ./result/stage2/models --image_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned/test_set

CUDA_VISIBLE_DEVICES=0 python test_simple.py --model_path  /media/bigssd2/bsc_depth/model_ckpts/pipac_no_finetune/models/weights_19  --image_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned/test_set



# Prediction files can be found at /media/bigssd2/bsc_depth/SCARED_testset_pred (with raw input videos - stereo, before processing - and depth map videos)