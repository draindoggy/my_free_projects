from PIL import Image
import os.path
print('введите название изображения, которое хотите обрезать: ')
nazv_image = str(input())
image = Image.open(nazv_image)
left = top = 0
i = 1
right = int(input('ширина изображения: '))
bottom = int(input('высота изображения: '))
cropped_image = image.crop((left, top, right, bottom))
if os.path.exists('cropped_image.jpg'):
    while os.path.exists('cropped_image'+str(i)+'.jpg'):
        i+=1
    cropped_image.save('cropped_image'+str(i)+'.jpg')
else:
    cropped_image.save('cropped_image.jpg')