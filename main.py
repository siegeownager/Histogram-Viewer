from PIL import Image


def open_image():
    return Image.open('cat.jpg')


def grab_dimensions(image):
    width, height = image.size
    return width, height


def main():
    image = open_image()
    width, height = grab_dimensions(image)
    print(width)
    print(height)


if __name__ == "__main__":
    main()
