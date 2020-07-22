import time  # for printing out the time the program needs to run
import numpy as np
from PIL import Image
from math import sqrt


# function that creates a numpy array, which represents a rgb image, from a message
def create_ascii_rgb_array(msg):

    measures = find_fitting_measures(int(len(msg)/3)+1)  # finds fitting rectacle
    width, height = measures[0], measures[1]
    ascii_rgb_array = np.zeros([height, width, 3], dtype=np.uint8)  # creates array for rgb image
    values = [ord(m)*2 for m in msg]  # gets the ascii decimal value of every character o the message

    # puts every value in packs of three as rgb values in array
    counter = 0
    for i in range(height):
        for j in range(width):
            rgb = [0, 0, 0]
            for k in range(3):
                if counter < len(values):
                    rgb[k] = values[counter]
                counter += 1
            ascii_rgb_array[i, j] = rgb

    return ascii_rgb_array


# function that calculates a fitting rectangle for a specific number of elements
# f.ex. length: 20 -> 4, 5
def find_fitting_measures(length):
    height = int(sqrt(length))  # should be similar to a square, i.e. the squareroot is used
    width = int(length/height) + 1  # not too much, but enough lines
    if length % height == 0:
        width -= 1

    return [height, width]


def save_rgb_image(msg):  # using PIL
    array = create_ascii_rgb_array(msg)  # creates the needed array with the upper function
    img = Image.fromarray(array)  # creates an image using PIL
    img.save('images/testrgb2.png') # saves the image in the folder images under the name testrgb2
    print("Image is saved")


if __name__ == "__main__":
    start_time = time.time()

    with open('Texts/file.txt', 'r') as open_file:  # gets text/message from separate file in the folder Texts
        all_text = open_file.read()
        message = all_text.strip()
    save_rgb_image(message)  # embeds the text/message in the file

    print("--- %s seconds ---" % (time.time() - start_time))  # prints runtime

