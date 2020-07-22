import time
import numpy as np
from PIL import Image


def decode_rgb_image(img_array):
    width = array.shape[1]  # width and height of picture is determined
    height = array.shape[0]
    values = []

    for i in range(height):  # puts the rgb values in a one dimensional list
        for j in range(width):
            for k in range(3):
                values.append(img_array[i, j][k])
    message = ''.join(chr(int(v/2)) for v in values if v != 0)  # translates Ascii Value to chraracter

    return message


if __name__ == "__main__":
    start_time = time.time()

    img = Image.open('images/testrgb2.png')
    array = np.array(img)  # get the array of the rgb values from the image
    print(decode_rgb_image(array))

    print("--- %s seconds ---" % (time.time() - start_time))
