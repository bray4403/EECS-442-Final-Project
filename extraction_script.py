import os
import random
import shutil
from PIL import Image
import os
import random
import shutil

# Path to the folder containing the letter folders
source_folder = 'C:/Users/johno/OneDrive/Desktop/archive/ASL_Alphabet_Dataset/asl_alphabet_train'

# Destination folder where you want to move the images
destination_parent_folder = 'C:/Users/johno/OneDrive/Desktop/archive/extract_train_3'
destination_parent_folder_2 = 'C:/Users/johno/OneDrive/Desktop/archive/extract_test_3'
destination_parent_folder_3 = 'C:/Users/johno/OneDrive/Desktop/archive/extract_val_3'

for letter in os.listdir(source_folder):
    print(letter)

def resize_image(image_path, target_size=(64, 64)):
    with Image.open(image_path) as img:
        img_resized = img.resize(target_size)
        return img_resized

# Loop through each letter folder
for letter in os.listdir(source_folder):
    letter_folder = os.path.join(source_folder, letter)
    
    # Check if it's a directory
    if os.path.isdir(letter_folder):
        # Create a new folder for the letter inside the destination parent folder
        destination_letter_folder = os.path.join(destination_parent_folder, letter)
        destination_letter_folder_2 = os.path.join(destination_parent_folder_2, letter)
        destination_letter_folder_3 = os.path.join(destination_parent_folder_3, letter)
        os.makedirs(destination_letter_folder, exist_ok=True)
        os.makedirs(destination_letter_folder_2, exist_ok=True)
        os.makedirs(destination_letter_folder_3, exist_ok=True)
        
        # Get the list of image files in the letter folder
        images = [f for f in os.listdir(letter_folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]
        
        print(len(images[:int(len(images)*.10)]))
        # Select a random sample of images
        selected_images = random.sample(images[int(len(images)*.20):], 200)
        selected_images_2 = random.sample(images[int(len(images)*.10):int(len(images)*.20)], 40)
        selected_images_3 = random.sample(images[:int(len(images)*.10)], min(len(images[:int(len(images)*.10)])-1,40))
        print("test")
        
        for i, image in enumerate(selected_images_3):
            source_image = os.path.join(letter_folder, image)
            destination_image = os.path.join(destination_letter_folder_3, letter + '_' + str(i+1) + os.path.splitext(image)[1])
            resized_image = resize_image(source_image)
            resized_image.save(destination_image)

        # Move the selected images to the destination folder
        for i, image in enumerate(selected_images):
            
            source_image = os.path.join(letter_folder, image)
            destination_image = os.path.join(destination_letter_folder, letter + '_' + str(i+1) + os.path.splitext(image)[1])
            resized_image = resize_image(source_image)
            resized_image.save(destination_image)

        for i, image in enumerate(selected_images_2):
            source_image = os.path.join(letter_folder, image)
            destination_image = os.path.join(destination_letter_folder_2, letter + '_' + str(i+1) + os.path.splitext(image)[1])
            resized_image = resize_image(source_image)
            resized_image.save(destination_image)

        
