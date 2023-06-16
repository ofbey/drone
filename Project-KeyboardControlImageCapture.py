from djitellopy import tello
import time
import KeyPressModule as kp
import cv2

kp.init()
myTello = tello.Tello()
myTello.connect()
print(myTello.get_battery())
global img
myTello.streamon()
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed

    if kp.getKey("q"):
        myTello.land(); time.sleep(3)
    if kp.getKey("e"):
        myTello.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f"Resources/Images/{time.time()}.jpg", img)
        time.sleep(0.3)

    return[lr, fb, ud, yv]



while True:
    values = getKeyboardInput()
    myTello.send_rc_control(values[0], values[1], values[2], values[3])
    img = myTello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
