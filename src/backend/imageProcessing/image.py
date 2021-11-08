import numpy as np
from PIL import Image
import os
# cwd = os.getcwd()
# os.chdir(os.path.join(cwd, "Algeo02-20112", "src", "backend"))
from svd import *


def imageToThreeArray(address):
    img = Image.open(address)
    arr = np.array(img)
    intArr = np.vectorize(np.int64)
    arr = intArr(arr)
    return [arr[0:, 0:, 0], arr[0:, 0:, 1], arr[0:, 0:, 2]]

def threeArrayToOneArray(array):
    newArr = np.zeros((len(array[0]), len(array[0][0]), 3), dtype=np.uint8)
    newArr[0:, 0:, 0] = array[0]
    newArr[0:, 0:, 1] = array[1]
    newArr[0:, 0:, 2] = array[2]
    return newArr

def arrayToImg(array):
    img = Image.fromarray(array)
    img.save(r"imageProcessing\new.jpg")
    return

def coba(threeArray):
    red = threeArray[0]
    green = threeArray[1]
    blue = threeArray[2]
    length = len(red)
    red = svd(red, length/2)
    green = svd(green, length/2)
    blue = svd(blue, length/2)
    newArr = [red, green, blue]
    return newArr
cwd = os.getcwd()
os.chdir(os.path.join(cwd, "Algeo02-20112", "src", "backend"))
# arrayToImg(threeArrayToOneArray(coba(imageToThreeArray(r"imageProcessing\img.jpg"))))
x = imageToThreeArray(r"imageProcessing\img.jpg")[0]
# print(np.dot(x, transpose(x)))
# print(getEigenValues(np.array(x)))
print(svd(x, 5))
# print(np.array(svd([[1, 1, 1, 0, 0],
#      [3, 3, 3, 0, 0],
#      [4, 4, 4, 0, 0],
#      [5, 5, 5, 0, 0],
#      [0, 2, 0, 4, 4],
#      [0, 0, 0, 5, 5],
#      [0, 1, 0, 2, 2]], 3)))
# print(svd(imageToThreeArray(r"imageProcessing\img.jpg")[0], 70))



# arrayToImg(threeArrayToOneArray(imageToThreeArray(r"imageProcessing\img.jpg")))
