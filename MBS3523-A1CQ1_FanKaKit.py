import serial
import cv2

serCom = serial.Serial('COM4', baudrate=115200)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    while serCom.inWaiting() == 0:
        pass
    VR = serCom.readline()
    VR = str(VR, 'utf-8')
    VR = VR.strip('\r\n')
    print(VR)
    while True:
        success, frame = cam.read()
        cv2.putText(frame, 'Brightness = ' + VR + "%", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 2)
        cv2.imshow('Window', frame)
        if cv2.waitKey(1) & 0xff == 27:
            break
    cam.release()
    cv2.destroyAllWindows()
