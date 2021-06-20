import cv2
import json

with open('sample_labels.json') as json_file:
    json_data = json.load(json_file)

bbox_num = len(json_data["annotation"][9].get('objects'))

img = cv2.imread("sample_images/img10.jpg")

red_color = (0, 0, 255)
font = cv2.FONT_HERSHEY_SIMPLEX


for i in range(bbox_num):
    text = json_data["annotation"][9].get('objects')[i].get('class')
    x_center, y_center, width, height = json_data["annotation"][9].get('objects')[i].get('position')
    x1 = int(x_center - width//2)
    y1 = int(y_center - height//2)
    x2 = int(x1 + width)
    y2 = int(y1 + height)
    img = cv2.putText(img, text, (x1, y1), font, 0.5, red_color, 1)
    img = cv2.rectangle(img, (x1, y1), (x2, y2), red_color)


cv2.imshow("img", img)
cv2.imwrite("bbox_img10.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()