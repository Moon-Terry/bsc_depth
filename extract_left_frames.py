import cv2
import glob
import os

def extract_left_frames(path_to_target_folder):
  train_vol_names = glob.glob(os.path.join(path_to_target_folder, '*.png'))
  train_vol_names.sort()
  for image in train_vol_names:
    vol1 = cv2.imread(image, 1)
    vol1 = vol1[0:1024, :, :]
    cv2.imwrite(image, vol1)
 

if __name__ == '__main__':
  for i in range(1, 10): # dataset 1-9
    for j in range(1, 5): # keyframe 1-4
      if i == 1 and j == 4:
        continue

      path = '/media/bigssd2/bsc_depth/SCARED/dataset_{}/keyframe_{}/image_02/data/'.format(i, j)
      extract_left_frames(path)
      print('done with dataset {} keyframe {}'.format(i, j))