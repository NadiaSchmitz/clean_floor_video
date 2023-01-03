# PROJEKT Sauberer Boden
# Teil 1
# Ziel - Video-Datei in einzelne Bilder aufgeteilt und Bildgröße reduzieren

import cv2

capture = cv2.VideoCapture('videos/Video_clean_floor.mp4')
dataset = []

i = 0

while True:
    success, img = capture.read()
    try:
        wb_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        break
    img_size_cut = cv2.resize(wb_img, (150, 150))
    dataset.append(img_size_cut)
    cv2.imshow('Floor', img_size_cut)
    path = r'C:\Users\nadii\Desktop\github\clean_floor_video\videos\dataset\img_' + str(i) + '.jpg'

    cv2.imwrite(path, img_size_cut)
    i = i + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

print("Anzahl der Bilder im Dataset: ", len(dataset))
print("Pfad: ", path)
