# Opens and saves binary files

import sys

from PIL import Image

images = []  # store image objects

# add all images to list
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# save gif starting from images[0]
# "costumes.gif": name of file to save
# save_all=True: save all frames, core of generating gif
# append_images=[]: accept a list, use images[1:] if more than 2 images to append
# duration=200: time every frame stays, in milisecond (0.2s in this case)
# loop=0: number of loop, 0 is infinite
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
