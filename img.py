import os
import sys
from PIL import Image

input_folder = "images"
output_folder = "resized_images"
new_size = (800, 600)
output_format = "JPEG"

# ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# if input folder missing, create it and ask user to add images
if not os.path.exists(input_folder):
    os.makedirs(input_folder, exist_ok=True)
    print(f"Created input folder: {os.path.abspath(input_folder)}")
    print("Add image files (jpg, png, gif...) into that folder and run the script again.")
    sys.exit(0)

processed = 0
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)
        try:
            with Image.open(img_path) as img:
                # convert to RGB for JPEG output
                if output_format.upper() == "JPEG" and img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                resized_img = img.resize(new_size, Image.LANCZOS)
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                resized_img.save(output_path, output_format, quality=85)
                print(f"✅ Resized and saved: {output_path}")
                processed += 1
        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

if processed == 0:
    print("No images found in the input folder.")
else:
    print(f"🎉 {processed} images processed. Output: {os.path.abspath(output_folder)}")