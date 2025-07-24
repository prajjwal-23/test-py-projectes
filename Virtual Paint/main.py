import cv2
import os
import numpy as np
import handtraking as htm


brushThikness = 15
eraserThikness = 50
xp, yp = 0, 0

folderPath = "header"
mylist = os.listdir(folderPath)
# print(mylist)
overlaylist = []
for imPath in mylist:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlaylist.append(image)
# print(len(overlaylist))

header = overlaylist[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)

window_width = 640
window_height = 480
# cv2.WINDOW_NORMAL makes the output window resizealbe
cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
# resize the window according to the screen resolution
cv2.resizeWindow('Resized Window', window_width, window_height)

# cap.set(3, 810)
# cap.set(4, 450)

detector = htm.handDetector(detectionCon=0.85)
imgCanvas = np.zeros((480, 640, 3), np.uint8)

while True:
    # 1. Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find hand landmarks
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        
        # tip of index and middle fingure
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        # print(x1, y1)
        # 3. check which fingure are up
        fingers = detector.fingersup()
        # print(fingure)

        # 4. if selection mode - two fing are up 
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            # checking for the click
            if y1 < 69:
                if 80 < x1 < 180:
                    header = overlaylist[0]
                    drawColor = (255, 0, 255)
                elif 240 < x1 < 335:
                    header = overlaylist[1]
                    drawColor = (255, 0, 0)
                if 370 < x1 < 480:
                    header = overlaylist[2]
                    drawColor = (0, 255, 0)
                if 510 < x1 < 620:
                    header = overlaylist[3]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1-25), (x2, y2+25), drawColor, cv2.FILLED)

        # 5. if draw mode - index fingure is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThikness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThikness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThikness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThikness)

            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Setting the header img
    img[0:69, 0:640] = header
    cv2.putText(img, "Press Esc to close", (10, 460), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255), 1)

    # img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)

    cv2.imshow("Resized Window", img)

    key = cv2.waitKey(1) & 0xff

    if key == 27:
        break

cv2.destroyAllWindows()
