import numpy
from PIL import Image


# Function to open and return the image object
def open_image():
    return Image.open('cat.jpg')


# Function to grab the dimensions of the image
def grab_dimensions(image):
    width, height = image.size
    return width, height


# Function to initialize empty color arrays
def initialize_color_arrays():
    R_array = [0] * 256
    G_array = [0] * 256
    B_array = [0] * 256
    return R_array, G_array, B_array


# Function to test if the number of loops is accurate
def test_array(array):
    sum_val = 0
    for i in range(len(array)):
        sum_val = sum_val + array[i]

    return sum_val


def create_buckets(image, width, height):
    R_array, G_array, B_array = initialize_color_arrays()

    for i in range(height):
        for j in range(width):
            red_val, green_val, blue_val = image.getpixel((j, i))
            R_array[red_val] += 1
            G_array[green_val] += 1
            B_array[blue_val] += 1

    print(numpy.histogram(R_array, 256)) # Seems to be wrong


def main():
    image = open_image()
    width, height = grab_dimensions(image)
    create_buckets(image, width, height)
    initialize_color_arrays()


if __name__ == "__main__":
    main()
