import os
import concurrent.futures
import time
from PIL import Image

t1 = time.perf_counter()

image_folder = r'C:\Users\GetDo\Project\NN\Resized'
image_folder_target = r'C:\Users\GetDo\Project\NN\BndW'
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')]

size = (28, 28)

#bndw means black and white

def process_image_bndw(img):
    image = Image.open(image_folder+'/'+img)
    new_image = image.convert("L")
    new_image.save(image_folder_target+'/'+img)
    print(f'{img} was processed')


#with concurrent.futures.ProcessPoolExecutor() as executor:
#    executor.map(process_image_bndw, image_files)

#FThe multiprocessing is still not working


for image in image_files:
    process_image_bndw(image)


t2 = time.perf_counter()


print(f'Finished in {t2-t1} seconds')
