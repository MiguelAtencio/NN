import os
from PIL import Image, ImageStat

image_folder = r'C:\Users\GetDo\Project\NN\archive'
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')]

cont = 0
duplicate_files = []

for file_org in range(len(image_files)):
    if not image_files[file_org] in duplicate_files and image_files[file_org]:
        image_org = Image.open(os.path.join(image_folder, image_files[file_org]))
        pix_mean1 = ImageStat.Stat(image_org).mean

        for file_check in range(file_org, file_org+1):
            if file_check <= len(image_files):
                if image_files[file_check] != image_files[file_org]:
                    image_check = Image.open(os.path.join(image_folder, image_files[file_check]))
                    pix_mean2 = ImageStat.Stat(image_check).mean

                    if pix_mean1 == pix_mean2:
                        duplicate_files.append(image_files[file_check])
                        os.remove(image_folder + '/'+ image_files[file_check])
                        cont += 1

print(str(cont) + ' duplicated files were deleted')
print(duplicate_files)
##4,319 pictures