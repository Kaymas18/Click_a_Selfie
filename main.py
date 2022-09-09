def print_hi(name):
    print(f'Hi, {name}')  
if __name__ == '__main__':
    print_hi('PyCharm')
    from cv2 import *
    cam_port = 0
    cam = VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        imshow("Kaymas18", image)
        imwrite("Kaymas18.png", image)
        waitKey(0)
        destroyWindow("Kaymas18")
    else:
        print("No image detected. Please! try again")
