import os
import argparse
from PIL import Image

def apply_logo_to_folder(input_folder, output_folder, logo_path, position):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each image in the folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            print(f"Processing {filename}...")

            # Apply logo to the image
            apply_logo(image_path, logo_path, output_path, position)

def apply_logo(image_path, logo_path, output_path, position):
    # Load the base image and logo
    base_image = Image.open(image_path).convert("RGBA")  # Ensure base image is in RGBA
    logo = Image.open(logo_path).convert("RGBA")         # Ensure logo is in RGBA

    # Resize logo to fit if it's too large
    base_width, base_height = base_image.size
    max_logo_width = base_width // 5
    max_logo_height = base_height // 5
    logo.thumbnail((max_logo_width, max_logo_height), Image.LANCZOS)

    # Define positions for the logo
    logo_width, logo_height = logo.size
    positions = {
        "Top Left": (10, 10),
        "Top Center": ((base_width - logo_width) // 2, 10),
        "Top Right": (base_width - logo_width - 10, 10),
        "Middle Right": (base_width - logo_width - 10, (base_height - logo_height) // 2),
        "Bottom Right": (base_width - logo_width - 10, base_height - logo_height - 10),
        "Bottom Center": ((base_width - logo_width) // 2, base_height - logo_height - 10),
        "Bottom Left": (10, base_height - logo_height - 10),
        "Middle Left": (10, (base_height - logo_height) // 2)
    }

    # Get the specified position or default to Bottom Right
    pos = positions.get(position, positions["Bottom Right"])

    # Paste the logo onto the base image with transparency handling
    base_image.paste(logo, pos, logo)  # Use logo as its own mask

    # Convert back to RGB if you want to save as JPEG, or keep as RGBA for PNG
    final_image = base_image.convert("RGB") if output_path.lower().endswith(".jpg") else base_image
    final_image.save(output_path)
    print(f"Saved processed image to {output_path}")

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Apply a logo to all images in a folder at a specified position.")
    parser.add_argument("input_folder", type=str, help="Path to the input images folder")
    parser.add_argument("output_folder", type=str, help="Path to the output images folder")
    parser.add_argument("logo_path", type=str, help="Path to the logo image")
    parser.add_argument("position", type=str, choices=[
        "Top Left", "Top Center", "Top Right", "Middle Right", 
        "Bottom Right", "Bottom Center", "Bottom Left", "Middle Left"
    ], help="Position to place the logo on the images")

    args = parser.parse_args()

    # Run the main function with the parsed arguments
    apply_logo_to_folder(args.input_folder, args.output_folder, args.logo_path, args.position)
