from PIL import Image


def open_image():
    return Image.open('cat.jpg')


def grab_dimensions(image):
    width, height = image.size
    return width, height

def create_buckets(image, width, height):
    for i in range(height):
        for j in range(width):
            im = image.getpixel((j, i))
            print(im)



def main():
    image = open_image()
    width, height = grab_dimensions(image)
    create_buckets(image, width, height)


if __name__ == "__main__":
    main()
