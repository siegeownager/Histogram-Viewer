import numpy
from PIL import Image
import matplotlib.pyplot as plt


# Function to open and return the image object
def open_image():
    return Image.open('cat.jpg')


# Function to plot the graph
def plot_graph(color_array, color):
    x_array = list(range(256))
    plt.plot(x_array, color_array, color)


# Function to display the graph
def display_plots():
    plt.show()


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


# Function to create arrays with frequencies of each R, G, B value
def create_buckets(image, width, height, R_array, G_array, B_array):
    for i in range(height):
        for j in range(width):
            red_val, green_val, blue_val = image.getpixel((j, i))
            R_array[red_val] += 1
            G_array[green_val] += 1
            B_array[blue_val] += 1

    return R_array, G_array, B_array


def main():
    image = open_image()
    width, height = grab_dimensions(image)
    R_array, G_array, B_array = initialize_color_arrays()
    create_buckets(image, width, height, R_array, G_array, B_array)

    plot_graph(R_array, 'red')
    plot_graph(G_array, 'green')
    plot_graph(B_array, 'blue')

    display_plots()


if __name__ == "__main__":
    main()
