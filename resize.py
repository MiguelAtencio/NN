import os
import concurrent.futures
import time
from PIL import Image

t1 = time.perf_counter()

image_folder = r'C:\Project\NN\archive'
image_folder_target = r'C:\Project\NN\Resized'
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')]

size = (28, 28)

def process_image_resize(img):
    image = Image.open(image_folder+'/'+img)
    new_image = image.resize(size)
    new_image.save(image_folder_target+'/'+img)
    print(f'{img} was processed')


#with concurrent.futures.ProcessPoolExecutor() as executor:
#    executor.map(process_image_resize, image_files)

#For some reason the multiprocess didnt work


for image in image_files:
    process_image_resize(image)


t2 = time.perf_counter()


print(f'Finished in {t2-t1} seconds')

