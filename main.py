import sys
import json
import glob
import cv2
import os
# import logging
import function
import time

# initialize
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

def make_folder(rootPath: str, path: str):
    os.makedirs(rootPath + path, exist_ok=True)

def get_images(path: str):
    types = (
        path + '/*.png', 
        path + '/*.jpg'
    )

    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))

    return files_grabbed

def save_image(path: str, image):
    cv2.imwrite(path, image)


if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    nasPath = data["nasPath"]
    inputDir = data["inputDir"]
    outputDir = data["outputDir"]

    print("Prepare for 5 seconds...")
    time.sleep(5)
    print("End. Process Start")

    make_folder(nasPath, outputDir)
    img_arr = get_images(nasPath + inputDir)

    for i in img_arr:
        file_name = os.path.basename(i)
        r = function.process_image(i)
        save_image(nasPath + outputDir + "/" + file_name, r)

    print("py-image-sample2 Process Complete")