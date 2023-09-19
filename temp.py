import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread(r"C:\Users\11471\Desktop\IMG\linber.png")
cv2.imshow("image", img)
cv2.waitKey(0)  # 等待用户按下任意键
cv2.destroyAllWindows()  # 关闭图像窗口
print("opencv test")
img = cv2.imread(r"C:\Users\11471\Desktop\IMG_6276.JPG", cv2.IMREAD_GRAYSCALE)
# 图象的显示，创建一个窗口
cv2.imshow("image", img)
# 等待时间
cv2.waitKey(0)
cv2.destroyAllWindows()
#
vc = cv2.VideoCapture(r"C:\Users\11471\Desktop\opencvL\PKC`ORLU5S3$2STD2U0KH{R.gif")
if vc.isOpened():
    open, frame = vc.read()
else:
    open = False
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("result", gray)
        if cv2.waitKey(1000) & 0xFF == 27:
            break
vc.release()
cv2.destroyAllWindows()
