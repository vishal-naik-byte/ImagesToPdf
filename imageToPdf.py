import os
from PIL import Image

def add_image_to_pdf(pdf_path, image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure image is in RGB mode for PDF compatibility
        if not os.path.exists(pdf_path):
            img.save(pdf_path, "PDF", resolution=100.0, save_all=True)
        else:
            img.save(pdf_path, "PDF", resolution=100.0, save_all=True, append=True)
        print(f"Image '{image_path}' added to PDF '{pdf_path}'")
    except Exception as e:
        print(f"Error adding image '{image_path}' to PDF: {e}")

# Set the directory path
directory_path = "/home/kali/Documents/"
pdf_path = os.path.join(directory_path, "images1.pdf")

# List all image files in the directory and sort them numerically
images = sorted([f for f in os.listdir(directory_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.webp')], key=lambda x: int(os.path.splitext(x)[0]))
images = images[3342:]
#print(images)
#exit()
# Process each image and add it to the PDF
for image_name in images:
    image_path = os.path.join(directory_path, image_name)
    add_image_to_pdf(pdf_path, image_path)
