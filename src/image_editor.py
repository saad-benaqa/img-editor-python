from PIL import Image, ImageEnhance
import os

def modify_image(input_path, output_folder):
    image = Image.open(input_path)

    enhancer = ImageEnhance.Contrast(image)
    edited_image = enhancer.enhance(1.5)  
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, os.path.basename(input_path))
    
    edited_image.save(output_path)
    print(f"Modified image saved to {output_path}")

if __name__ == "__main__":
    input_image_path = "original_photos/sample.jpeg"
    modify_image(input_image_path, "modified_photos")
