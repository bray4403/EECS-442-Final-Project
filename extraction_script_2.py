from PIL import Image
import os

# Define the input and output folders
input_folder = 'C:/Users/johno/downloads/ChicagoFSWILD'
output_folder = 'C:/Users/johno/downloads/ChicagoFSWILDout'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Walk through all subdirectories and process images
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust the extensions as needed
            # Construct the full path to the image
            img_path = os.path.join(root, filename)
            
            # Open the image
            img = Image.open(img_path)
            
            # Resize the image to 64x64
            img_resized = img.resize((64, 64))
            
            # Create the corresponding output subdirectory structure
            relative_path = os.path.relpath(root, input_folder)
            output_subfolder = os.path.join(output_folder, relative_path)
            os.makedirs(output_subfolder, exist_ok=True)
            
            # Save the resized image to the output folder
            output_path = os.path.join(output_subfolder, filename)
            img_resized.save(output_path)

            print(f'{filename} resized and saved to {output_path}')