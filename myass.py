import pytesseract
from PIL import Image
from fpdf import FPDF
import os

image_folder = "/data/data/com.termux/files/home/downloads"  # Update this to the actual path of your images folder
text_folder = "/data/data/com.termux/files/home/downloads/texts"

# Make a directory for text files if it doesn’t exist
os.makedirs(text_folder, exist_ok=True)

# Step 1: Extract text from each image
for img_name in os.listdir(image_folder):
    if img_name.endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(image_folder, img_name)
        text = pytesseract.image_to_string(Image.open(img_path))
        with open(f"{text_folder}/{img_name}.txt", "w") as text_file:
            text_file.write(text)

# Step 2: Create a single PDF with extracted text
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Times", size=10)  # Set font to Times New Roman with specified size

for text_file in sorted(os.listdir(text_folder)):
    with open(f"{text_folder}/{text_file}", "r") as file:
        text = file.read()
        pdf.multi_cell(0, 10, text)  # Adds single-line spacing

pdf.output("output.pdf")
