import cv2
def colorProfiles(n):
    if n == 0:
        name = "Pepsi"
        hsv_lower = (95, 100, 100)
        hsv_upper = (115, 255, 255)
        return (name, hsv_lower, hsv_upper)
    if n == 1:
        name = "Coke"
        hsv_lower = (0, 100, 100)
        hsv_upper = (10, 255, 255)
        return (name, hsv_lower, hsv_upper)


frame = cv2.imread("image.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
rects = {}
for i in range(2):
    name, hsv_lower, hsv_upper = colorProfiles(i)
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
    conts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = sorted(conts, key=cv2.contourArea, reverse=True)[0]
    rect = cv2.boundingRect(biggest)

    x, y, w, h = rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 3)
    cv2.putText(frame, name, (x, y + 3), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


cv2.imshow("Image", frame)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
