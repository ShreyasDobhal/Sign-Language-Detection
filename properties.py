import cv2

index = []
for i in range(0,99):
    try :
        cam = cv2.VideoCapture(i)
        if cam.read()[0] == True:
            index.append(i)
            cam.release()
    except:
        continue

def get_available_cameras():
    return index

def get_camera_port():
    return index[len(index)-1]
