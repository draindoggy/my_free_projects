from PIL import Image
print('введите название изображения, которое хотите обрезать: ')
nazv_image = str(input())
image = Image.open(nazv_image)
left = 0
top = 0
right = int(input('ширина изображения: '))
bottom = int(input('высота изображения: '))
cropped_image = image.crop((left, top, right, bottom))
cropped_image.save('cropped_image.jpg')