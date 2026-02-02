from PIL import Image
from tqdm import tqdm
import os

def resize_image(image_path, output_folder, size):
    try:
        with Image.open(image_path) as img:
            img.thumbnail(size, Image.Resampling.LANCZOS)

            filename = os.path.splitext(os.path.basename(image_path))[0]
            save_path = os.path.join(output_folder, filename + ".jpg")

            img.save(save_path, "JPEG")
    except Exception as e:
        print(f"Error with {image_path}: {e}")

# USER INPUT
path = input("Enter path to images folder: ").strip().strip('"')
size_input = input("Enter size (width,height): ").strip()
size = tuple(map(int, size_input.split(",")))

# CHECK FOLDER EXISTS
if not os.path.isdir(path):
    print("Folder does not exist. Please check the path.")
    exit()

print(f"Input Folder: {path}")

# CREATE OUTPUT FOLDER
output_folder = os.path.join(path, "resize")
os.makedirs(output_folder, exist_ok=True)
print(f"Resize folder ready at: {output_folder}")

# FIND ALL IMAGES (INCLUDING SUBFOLDERS)
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")

image_files = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.lower().endswith(valid_extensions):
            image_files.append(os.path.join(root, file))

if not image_files:
    print("No image files found.")
    exit()

print(f"Found {len(image_files)} images.")

# RESIZE PROCESS
for image_path in tqdm(image_files, desc="Resizing Images"):
    resize_image(image_path, output_folder, size)

print("Resizing Completed! Check the 'resize' folder.")