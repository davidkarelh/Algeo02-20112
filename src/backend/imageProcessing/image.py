import numpy as np
from PIL import Image
import os

def imageToThreeArray(img_data):
    img = Image.open(img_data)
    arr = np.array(img)
    return [arr[0:, 0:, 0], arr[0:, 0:, 1], arr[0:, 0:, 2]]

def threeArrayToOneArray(array):
    newArr = np.zeros((len(array[0]), len(array[0][0]), 3), dtype=np.uint8)
    newArr[0:, 0:, 0] = array[0]
    newArr[0:, 0:, 1] = array[1]
    newArr[0:, 0:, 2] = array[2]
    return newArr

def arrayToImg(array):
    img = Image.fromarray(array)
    img.save(r"new.jpg")
    return

ERR_TOL = 0.999999
MAX_LOOP = 100

def svd(A, percent):
    s = np.linalg.matrix_rank(A)
    rank = int(round(s * int(percent) / 100))
    n, m = np.shape(A)
    V = np.random.rand(m, s)
    err = 1 # inisialisasi error
    i = 0  
    while (err > ERR_TOL and i < MAX_LOOP):
        Q, R = np.linalg.qr(np.dot(A, V))
        U = Q[:,:s]
        Q, R = np.linalg.qr(np.dot(np.transpose(A), U))
        V = Q[:,:s]
        sigma = R[:s, :s]
        err = np.linalg.norm(np.dot(A, V) - np.dot(U, sigma))
        err = err / (s - rank + 1)
        i += 1
    print(i)
    return rank, U, sigma, V

def kompresiSVD(matrix, percent):
    rank, U, S, V = svd(matrix, percent)
    print("svd done")
    return np.dot(np.dot(U[0:, 0:rank], S[0:rank, 0:rank]), np.transpose(V[0:, 0:rank]))

def compress(img_data, percent):
    print("yes")
    x = imageToThreeArray(img_data)
    print("yes")
    R = x[0]
    print("yes")
    G = x[1]
    print("yes")
    B = x[2]
    print("yes")
    NR = kompresiSVD(R, percent)
    print("yes")
    NG = kompresiSVD(G, percent)
    print("yes")
    NB = kompresiSVD(B, percent)
    print("done")
    return np.uint8( threeArrayToOneArray ([NR, NG, NB]) )

def main():
    os.chdir(os.path.join("Algeo02-20112", "src", "backend", "imageProcessing"))
    
    x = imageToThreeArray(r"img.jpg")
    rank, UR, sigmaR, VR = svd(x[0], 80)
    rank, UG, sigmaG, VG = svd(x[1], 80)
    rank, UB, sigmaB, VB = svd(x[2], 80)

    # rank = 70
    R = np.dot(np.dot(UR[0:, 0:rank], sigmaR[0:rank, 0:rank]), np.transpose(VR[0:, 0:rank]))
    G = np.dot(np.dot(UG[0:, 0:rank], sigmaG[0:rank, 0:rank]), np.transpose(VG[0:, 0:rank]))
    B = np.dot(np.dot(UB[0:, 0:rank], sigmaB[0:rank, 0:rank]), np.transpose(VB[0:, 0:rank]))
    Image.fromarray(np.uint8(threeArrayToOneArray([R, G, B]))).save(r"1.jpg")

if __name__ == "__main__":
    main()