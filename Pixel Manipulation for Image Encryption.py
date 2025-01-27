from PIL import Image
import numpy as np

# Function to encrypt the image using pixel manipulation
def encrypt_image(image_path, key=5):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode
    
    # Convert image to a numpy array of pixels
    pixels = np.array(img)
    
    # Encrypt pixels by shifting the RGB values
    encrypted_pixels = (pixels + key) % 256  # Apply key to shift pixel values
    
    # Convert back to an image
    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
    return encrypted_img

# Function to decrypt the image (reverse of encryption)
def decrypt_image(encrypted_image, key=5):
    # Convert image to a numpy array of pixels
    encrypted_pixels = np.array(encrypted_image)
    
    # Decrypt pixels by reversing the shift operation
    decrypted_pixels = (encrypted_pixels - key) % 256
    
    # Convert back to an image
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
    return decrypted_img

# Encrypting and decrypting the image
def main():
    # Load your image
    image_path = 'image.jpg'  # Change this to your image file path
    
    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key=5)
    encrypted_image.save('encrypted_image.jpg')
    
    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key=5)
    decrypted_image.save('decrypted_image.jpg')

    print("Image encryption and decryption complete!")

if __name__ == "__main__":
    main()
