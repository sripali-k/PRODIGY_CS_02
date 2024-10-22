from PIL import Image
import numpy as np

def load_image(image_path):
    """Load an image from the specified path."""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def image_to_array(image):
    """Convert a PIL Image to a NumPy array."""
    return np.array(image)

def encrypt_image(image_array):
    """Encrypt the image by inverting pixel values."""
    # Example: Inverting pixel values (simple encryption)
    encrypted_array = 255 - image_array
    return encrypted_array

def save_image(image_array, output_path):
    """Save the NumPy array as an image."""
    encrypted_image = Image.fromarray(image_array)
    encrypted_image.save(output_path)

def main():
    input_image_path = 'input-image/input-image.jpg'  # Change this to your image path
    output_image_path = 'output-image/encrypted_image.png'

    image = load_image(input_image_path)

    if image is None:
        return  # Exit if image loading failed

    image_array = image_to_array(image)
    encrypted_array = encrypt_image(image_array)
    save_image(encrypted_array, output_image_path)

    print("Image encrypted successfully!")

if __name__ == "__main__":
    main()
