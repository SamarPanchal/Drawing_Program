import threading

import cv2
import time

inp = input("press 'y' to take your screenshot: ")

count = 16


def take_shot():

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (20, 450)
    font_scale = 1
    color = (0, 255, 0)
    thickness = 2

    global count
    time.sleep(1.0)
    count -= 1
    if count == 0:
        #######################
        exit()
    else:
        cv2.putText(read, f'Screenshot in {count}', org, font,
                    font_scale, color, thickness, cv2.LINE_AA)

    cv2.imshow("Screenshot - Press 'e' key to Exit", read)


if inp == "y":
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:

        success, read = cap.read()
        if cv2.waitKey(1) == ord("e"):
            break

        take_shot()
