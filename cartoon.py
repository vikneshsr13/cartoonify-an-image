import cv2
import numpy as np

# Function to read an image
def read_image(file_path):
    img = cv2.imread(file_path)
    if img is None:
        raise FileNotFoundError(f"Error: Could not load image at {file_path}. Please check the file path.")
    return img

# Function to create edge detection
def get_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    gray = cv2.medianBlur(gray, 5)  # Apply median blur
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )  # Edge detection
    return gray, edges

# Function to cartoonize the image
def cartoonize_image(img, edges):
    color = cv2.bilateralFilter(img, 9, 250, 250)  # Smooth the image
    cartoon = cv2.bitwise_and(color, color, mask=edges)  # Combine with edges
    return cartoon

# Function to display images side by side
def display_images(images, titles):
    # Ensure all images have the same number of channels
    resized_images = [
        cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) == 2 else img
        for img in images
    ]
    # Resize images for consistent display
    resized_images = [cv2.resize(img, (300, 300)) for img in resized_images]
    combined_image = cv2.hconcat(resized_images)  # Horizontally concatenate images
    cv2.imshow(' | '.join(titles), combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function
def main():
    try:
        # Specify the file path
        file_path = "imagename.jpg"  # Update with your file path

        # Step 1: Load the image
        img = read_image(file_path)

        # Step 2: Get grayscale and edges
        gray, edges = get_edges(img)

        # Step 3: Cartoonize the image
        cartoon = cartoonize_image(img, edges)

        # Step 4: Save outputs
        cv2.imwrite("gray_image.jpg", gray)
        cv2.imwrite("cartoon_image.jpg", cartoon)

        # Step 5: Display images
        images = [img, gray, edges, cartoon]
        titles = ["Original", "Grayscale", "Edges", "Cartoon"]
        display_images(images, titles)

        print("Images saved: gray_image.jpg, cartoon_image.jpg")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
