import cv2
import os

path = "Images"

images = []

for file in os.listdir(path):
    root ,ext = os.path.splitext(file)
    if ext in [".jpg","jpeg","gif","png"]:
        fileName = path+"/"+file
        images.append(fileName)

count = len(images)

frame = cv2.imread(images[0])
height , width , channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)


for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)


out.release()
print("Done")



