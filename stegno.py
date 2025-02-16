import cv2
import numpy as np
from PIL import Image

# Function to encode text into an image
def encode_image(image_path, secret_text, output_path):
    img = cv2.imread(image_path)
    binary_secret = ''.join(format(ord(i), '08b') for i in secret_text) + '1111111111111110'  # Delimiter

    data_index = 0
    binary_secret_len = len(binary_secret)
    for row in img:
        for pixel in row:
            for channel in range(3):  # BGR channels
                if data_index < binary_secret_len:
                    pixel[channel] = pixel[channel] & ~1 | int(binary_secret[data_index])
                    data_index += 1
                else:
                    break

    cv2.imwrite(output_path, img)
    print("Image saved with hidden message:", output_path)

# Function to decode text from an image
def decode_image(image_path):
    img = cv2.imread(image_path)
    binary_secret = ""

    for row in img:
        for pixel in row:
            for channel in range(3):
                binary_secret += str(pixel[channel] & 1)

    binary_values = [binary_secret[i:i+8] for i in range(0, len(binary_secret), 8)]
    secret_text = ''.join(chr(int(b, 2)) for b in binary_values if b != '11111110')  # Stop at delimiter
    return secret_text

# Example Usage
image_path = "input_image.png"  # Input image (Use PNG for lossless format)
output_path = "encoded_image.png"
secret_message = "Hello, this is a hidden message!"

# Encode text into image
encode_image(image_path, secret_message, output_path)

# Decode hidden text from the image
decoded_message = decode_image(output_path)
print("Decoded message:", decoded_message)