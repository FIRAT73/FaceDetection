import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()             #kare kare yakalamak

    cv2.imshow("frame",frame)
    if cv2.waitKey(20)  & 0xFF == ord("q"):
        break

#Aşağıdaki kodlarda yakalanan nesneyi serbest bırakmak için kullandık
cap.release()
cv2.destroyAllWindows()