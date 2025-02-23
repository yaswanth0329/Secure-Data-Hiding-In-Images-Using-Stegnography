# Secure-Data-Hiding-In-Images-Using-Stegnography
Project Overview

This project demonstrates image steganography, where secret messages are embedded within an image without altering its visual appearance. The method ensures secure communication by using pixel value manipulation to hide data, making it undetectable to the human eye. A password-based decryption mechanism ensures authorized access to the hidden message.

Features

✔ Secure Message Encoding: Hides text inside an image using pixel values.
✔ Password Protection: Prevents unauthorized decryption of hidden data.
✔ Lossless Data Encoding: Uses least significant bit (LSB) manipulation to avoid noticeable changes in the image.
✔ Cross-Platform Compatibility: Works on Windows, Linux, and macOS using Python and OpenCV.

Installation & Dependencies

Ensure you have Python installed, then install the required libraries using:

pip install opencv-python

Usage Instructions

1. Encoding the Secret Message

1. Place your input image (e.g., mypic.jpg) in the project directory.


2. Run the script and enter your secret message and a passcode when prompted.


3. The script will generate an encrypted image (encryptedImage.jpg) containing the hidden message.



2. Decoding the Secret Message

1. Run the script again.


2. Enter the correct passcode to retrieve the hidden message.


3. If the password is incorrect, access to the hidden message is denied.

Code Explanation

1. Encoding:

Reads the input image using OpenCV.

Stores the secret message within the image pixels.

Saves the modified image as encryptedImage.jpg.

2. Decoding:

Reads the encrypted image.

Asks for the passcode to retrieve the original message.

If the password is correct, it decrypts and displays the hidden message.


Example Execution

Enter secret message: Hello, World
Enter a passcode: 12345
(Encrypted image is generated)

Enter passcode for Decryption: 12345
Decryption message: Hello, this is hidden!

(If the wrong passcode is entered, access is denied.)

Future Enhancements

Implement AES encryption before hiding the message for extra security.

Extend the project to support audio and video steganography.

Develop a GUI-based application for ease of use.

License

This project is open-source and can be modified for educational or personal use.


