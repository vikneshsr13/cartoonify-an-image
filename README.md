Cartoonify An Image

This Python script converts a regular image into a cartoon-like version using OpenCV. It processes an input image to generate grayscale, edge-detected, and cartoonized outputs. The outputs are displayed side by side and saved locally.

Features

Reads and processes an input image.

Converts the image to grayscale.

Detects edges in the image.

Applies a cartoon effect using bilateral filtering and bitwise masking.

Saves the grayscale and cartoonized images.

Displays the original, grayscale, edge-detected, and cartoonized images side by side.



Prerequisites

Python 3.6+

OpenCV library (cv2)

Numpy library (numpy)



Installation

Clone the repository:

git clone https://github.com/vikneshsr13/cartoonify-an-image.git
cd cartoonify-image

Install the required libraries:

pip install opencv-python-headless numpy



Usage

Place your input image in the same directory as the script and update the file_path variable with the image file name (e.g., kissik.jpg).

Run the script:

python cartoonify_image.py



Outputs:

gray_image.jpg: Grayscale version of the input image.

cartoon_image.jpg: Cartoonized version of the input image.

The script will display all four images (Original, Grayscale, Edges, Cartoon) side by side in a single window.

Script Details

Main Steps

Load Image:
Reads the input image and verifies its existence.

Edge Detection:
Converts the image to grayscale and applies adaptive thresholding.

Cartoonization:
Applies bilateral filtering for smoothing and combines it with edges to create the cartoon effect.

Display and Save:
Displays the results side by side and saves the grayscale and cartoon images.

Functions

read_image(file_path): Loads the image from the specified file path.

get_edges(img): Converts the image to grayscale and performs edge detection.

cartoonize_image(img, edges): Generates the cartoonized version of the image.

display_images(images, titles): Displays images side by side in a single window.

Example Output

After running the script, the following outputs are generated:

Original Image

Grayscale Image

Edges Image

Cartoon Image

Troubleshooting

FileNotFoundError: Ensure the file path to the input image is correct.

Display Issues: If running in a non-GUI environment (e.g., remote servers), use a Jupyter notebook or Google Colab.

Contributions

Feel free to open issues or submit pull requests to improve this script.

Acknowledgments

OpenCV Documentation

Community tutorials for image processing.

