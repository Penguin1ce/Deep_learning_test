import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 在OpenCV中，cv2.VideoCapture.read() 返回一个包含两个值的元组：
# 第一个值是一个布尔值，表示是否成功读取了一帧图像，
# 第二个值是读取的图像数据，通常是一个NumPy数组（多维数组），表示图像的像素值。
# 如果成功读取了图像，第一个值为True，否则为False。
vc = cv2.VideoCapture(r"C:\Users\11471\Desktop\opencvL\acho.MP4")
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("result", gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break
vc.release()  # 如当你已经读取完视频所有帧或者你想切换到另一个设备时。
cv2.destroyAllWindows()
img = cv2.imread(r"C:\Users\11471\Desktop\IMG_6276.JPG")
print(img.shape)
shark = img[0:800, 0:400]
cv_show("shark", shark)
