#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

def grayscale(pixels):
    '''The function takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list of pixels for an image that 
    is a grayscale version of the original image.'''
    new_img = blank_image(len(pixels), len(pixels[0]))
    for i in range(0,len(new_img)):
        for j in range(0, len(new_img[0])):
            lumin = brightness(pixels[i][j])
            new_img[i][j] = [lumin, lumin, lumin]
    return new_img


def mirror_vert(pixels):
    '''This function takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list of pixels for an image in which 
    the original image is “mirrored” vertically.'''
    new_img = blank_image(len(pixels), len(pixels[0]))
    for i in range(len(new_img)//2):
        for j in range(len(new_img[0])):
            new_img[i][j] = pixels[i][j]
            new_img[len(pixels)-i-1][j] = pixels[i][j]
    if len(pixels) % 2 != 0:
        for j in range(len(new_img[0])):
            new_img[(len(pixels)//2)][j] = pixels[len(pixels)//2][j]
    return new_img
            


def flip_horiz(pixels):
    '''This function takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list of pixels for an image in which 
    the original image is “flipped” horizontally.'''
    new_img = blank_image(len(pixels), len(pixels[0]))
    for i in range(len(new_img)):
        for j in range(len(new_img[0])):
            new_img[i][j] = pixels[i][len(new_img[0])-1-j]
    return new_img


def reduce(pixels): 
    '''This function takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list that represents an image that is 
    half the size of the original image.'''
    reqheight = len(pixels)//2
    reqwidth = len(pixels[0])//2
    new_img = blank_image(reqheight,reqwidth)
    for i in range(reqheight):
        for j in range(reqwidth):
            new_img[i][j] = pixels[(2*i)][(2*j)]
    return new_img


def transpose(pixels): 
    '''This function takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list that is the transpose of pixels.'''
    new_img = blank_image(len(pixels[0]), len(pixels))
    for j in range(len(pixels[0])):
        for i in range(len(pixels)):
            new_img[j][i] = pixels[i][j]
    return new_img
                                    
