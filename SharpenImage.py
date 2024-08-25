import cv2
import numpy as np
import sys

def sharpen_image(input_image_path, output_image_path):
    # Load the image
    image = cv2.imread(input_image_path)

    # Check if image is loaded successfully
    if image is None:
        print(f"Error: Unable to load image {input_image_path}")
        return

    # Create a sharpening kernel
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])

    # Apply the filter to the image
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    # Save the sharpened image
    cv2.imwrite(output_image_path, sharpened_image)
    print(f"Sharpened image saved as {output_image_path}")

    # Display the sharpened image
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sharpen_image.py <input_image> <output_image>")
    else:
        input_image_path = sys.argv[1]
        output_image_path = sys.argv[2]
        sharpen_image(input_image_path, output_image_path)
