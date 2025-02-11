# o	Load an image using OpenCV.
# o	Convert the image to grayscale using NumPy.
# o	Apply a simple thresholding technique to create a binary image.
# o	Use NumPy to calculate and display the histogram of pixel values.
# o	Create a simple function to detect edges in the image using the Canny edge detector.

import cv2
import numpy as np
import matplotlib.pylab as plt

# function to reload image
def loadImage(path):
    img=cv2.imread(path)

    if img is None:
        print("Sorry could not load image. check the file path.")
        return None
    
    re_img=cv2.resize(img,(500,300))

    cv2.imshow("window1",re_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return re_img

# function to convert image to graysacle
def convert_greyScale(image):  
    grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    re_img=cv2.resize(grey,(500,300))

    print("Showing image!")
    print("press any key to close the image wiindow")

    cv2.imshow("window2",re_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return re_img

# function to apply threshold technique to create binary image
def threshold_binary_img(image):

    # img=cv2.imread(path)
    if image is None:
        print("No loaded image.")
        return None
    
    image=cv2.resize(image,(400,250))

    _,th=cv2.threshold(image,180,255,cv2.THRESH_BINARY)

    print("Showing image!")
    print("press any key to close the image wiindow")
    
    cv2.imshow("threshold",th)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function to calculate and display the histogram of pixel values.
def cal_pixels_histogram(image):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    hist=cv2.calcHist([image],[0],None,[255],[0,255])

    plt.plot(hist)
    print("showing the histogram!")
    plt.show()

    # cv2.imshow("window1",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function to detect edges using Canny edge detector
def canny_edge(image):
    if image is None:
        print("No loaded image.")
        return None
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(image, 100, 200)
    cv2.imshow("window2",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return edges

# path=r"C:\Users\DELL\OneDrive\Desktop\numpy\image8.png"

path=input("Enter path of image: ").strip()
print("press any key to close the image window.")
image=loadImage(path)

# menu to choose which function to call
while True:
    print("\n\n.............................................")
    print("Menu: ")
    print("1. Reload image")
    print("2. convert image to graysacle.")
    print("3. threshold technique to create binary image/")
    print("4. calculate and display the histogram of pixel values.")
    print("5. detect edges using Canny edge detector")
    print("6. Exit")
    
    ch=int(input("Enter choice: "))

    # for reloading image
    if ch==1:
        image=loadImage(path)
        if image is None:
            grey_image=convert_greyScale(image)

    # for conversion of an image to grayscale
    elif ch==2:
        grey_image=convert_greyScale(image)

    # to apply threshold technique to create binary image
    elif ch==3:
        threshold_binary_img(image)

    # to calculate and display the histogram of pixel values
    elif ch==4:
        cal_pixels_histogram(image)
    
    # to detect edges using canny edge detector
    elif ch==5:
        canny_edge(image)

    # exit the code
    elif ch==6:
        print("Exiting from the program!!")
        break

    # for invalid choice 
    else:
        print("Invalid choice. Try again. ")