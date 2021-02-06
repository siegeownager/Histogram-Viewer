import numpy
import PIL
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilenames, askdirectory, askopenfilename
from tkinter.messagebox import showerror, showinfo

WINDOW_SIZE = '300x300'


# Function to open and return the image object
def open_image():
    image_file = askopenfilename(filetypes=(("Image Files", "*.jpg *.png"),))
    return PIL.Image.open(image_file)


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


# This function is for generating the graphical window
def generate_ui():

    root = Tk()

    root.geometry(WINDOW_SIZE)

    frame1 = Frame(root)  # Image Select button
    frame2 = Frame(root)  # Convert button

    root.title("Image Histogram Viewer")

    # Button that executes the function to load the log file(s)
    button_default_text = StringVar()
    button_default_text.set("Select Image")

    select_button = Button(frame1, textvariable=button_default_text, command=open_image, width=22)
    select_button.pack()

    # Scroll bar and the list box for displaying the timezones
    scrollbar = Scrollbar(frame2)
    scrollbar.pack(side=RIGHT, fill=Y)



    # Button that calls the conversion function
    convert_button = Button(frame2, text="Convert", command=open_image, width=22)
    convert_button.pack()


    frame1.pack(padx=10, pady=10)
    frame2.pack(padx=1, pady=1)


def main():
    #generate_ui()
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
