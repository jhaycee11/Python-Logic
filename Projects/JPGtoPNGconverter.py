import os
import sys
from PIL import Image

def main():
    imgdir = sys.argv[1]
    newdir = sys.argv[2]
    if is_exist(imgdir, newdir):
        convert(imgdir, newdir)
    else:
        print("Please Try Again!")

def is_exist(imgdir, newdir):
    if os.path.exists(imgdir):
        if not os.path.exists(newdir):
            os.makedirs(newdir)
        return imgdir, newdir

def convert(imgdir, newdir):
    for images in os.listdir(imgdir):
        img = Image.open(f"{imgdir}{images}")
        img_rename = os.path.splitext(images)[0]
        img.save(f"{newdir}{img_rename}.png", "png")
        print(img_rename)

if __name__ == "__main__":
    main()