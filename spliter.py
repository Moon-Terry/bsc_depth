import os

# /media/bigssd2/bsc_depth/SCARED/dataset_{}/keyframe_{}/
# dataset_{}/keyframe_{} ## l

# Train dataset 1~7
def train():
    train_f = open("splits/SCARED/train_files.txt", 'w')

    for i in range(1, 8):
        for x in range(1,5):
            if i==1 and x==4:
                continue
            path = f"/media/bigssd2/bsc_depth/SCARED/dataset_{i}/keyframe_{x}/image_02/data"
            dir_list = os.listdir(path)
            png_files = [f for f in dir_list if f.endswith(".png")]

            for image in png_files:
                png_num = int(image[:-4])
                # To avoid getting errors for finding neighboring frames for first and last image
                if png_num == 1 or png_num == len(png_files):
                    print(f'excluded {path} {image}')
                    continue
                train_f.write(f"dataset_{i}/keyframe_{x} {png_num} l\n")
    train_f.close()
    # remove last line manually


# dataset 7~8
def validation():
    val_f = open("splits/SCARED/val_files.txt", 'w')

    for i in range(7, 9):
        for x in range(1, 5):
            path = f"/media/bigssd2/bsc_depth/SCARED/dataset_{i}/keyframe_{x}/image_02/data"
            dir_list = os.listdir(path)
            png_files = [f for f in dir_list if f.endswith(".png")]

            for image in png_files:
                png_num = int(image[:-4])
                # To avoid getting errors for finding neighboring frames for first and last image
                if png_num == 1 or png_num == len(png_files):
                    continue
                val_f.write(f"dataset_{i}/keyframe_{x} {png_num} l\n")
    val_f.close()
    # remove last line manually


# dataset 9
def test():
    test_f = open("splits/SCARED/test_files.txt", 'w')

    for x in range(1, 5):
        path = f"/media/bigssd2/bsc_depth/SCARED/dataset_9/keyframe_{x}/image_02/data"
        dir_list = os.listdir(path)
        png_files = [f for f in dir_list if f.endswith(".png")]

        for image in png_files:
            png_num = int(image[:-4])
            # To avoid getting errors for finding neighboring frames for first and last image
            if png_num == 1 or png_num == len(png_files):
                continue
            test_f.write(f"dataset_9/keyframe_{x} {png_num} l\n")
    test_f.close()
    # remove last line manually


if __name__ == "__main__":
    train()
    validation()
    test()