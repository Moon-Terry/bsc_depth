CUDA_VISIBLE_DEVICES=0 python train_end_to_end.py --data_path /media/bigssd2/bsc_depth/SCARED --log_dir ./results/ --split SCARED

# Train PIPAC
# CUDA_VISIBLE_DEVICES=0 python train_stage_one.py --data_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned --model_name stage1_pipac --split PIPAC_train --log_dir ./pipac_result --load_weights_folder ./result/stage2/models/weights_19
# CUDA_VISIBLE_DEVICES=0 python train_stage_two.py --data_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned --model_name stage2_pipac --split PIPAC_train --log_dir ./pipac_result --load_weights_folder ./pipac_result/stage1/models/weights_19
CUDA_VISIBLE_DEVICES=0 python train_end_to_end.py --data_path /media/bigssd2/bsc_depth/PIPAC_VIDEOS/cleaned --model_name pipac --log_dir ./results/ --split PIPAC_train --load_weights_folder ./result/stage2/models/