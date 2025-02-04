import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time

# Function to apply cartoon effect to an image
def cartoonify(image):
    grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    getEdge = cv2.adaptiveThreshold(
        smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=9
    )
    colorImage = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    return cartoonImage

# Function to visualize FPS on the frame
def visualize_fps(image, fps):
    text_color = (0, 255, 0) if len(np.shape(image)) == 3 else (255, 255, 255)
    cv2.putText(
        image, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2, cv2.LINE_AA
    )
    return image

# Section 1: Static Image Processing
if __name__ == "__main__":
    input_path = os.path.join("images", "Ali.jpg")
    image = cv2.imread(input_path)
    cartoon_image = cartoonify(image)
    cv2.imshow("Cartoonified Image", cartoon_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Section 2: Webcam Processing
    CAMERA_DEVICE_ID = 0
    IMAGE_WIDTH = 800
    IMAGE_HEIGHT = 600
    fps = 0

    cap = cv2.VideoCapture(CAMERA_DEVICE_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_HEIGHT)

    while True:
        start_time = time.time()
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (IMAGE_WIDTH, IMAGE_HEIGHT))
        frame = cartoonify(frame)
        frame = visualize_fps(frame, fps)
        cv2.imshow("Webcam Cartoonified", frame)

        end_time = time.time()
        fps = 1 / (end_time - start_time) if end_time > start_time else 0

        if cv2.waitKey(33) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Section 3: Video Processing
    CAMERA_DEVICE_ID = os.path.join("videos", "Jobs_2.mp4")
    IMAGE_WIDTH = 1000
    IMAGE_HEIGHT = 600
    FRAME_RATE = 30
    DURATION = 1 / FRAME_RATE

    cap = cv2.VideoCapture(CAMERA_DEVICE_ID)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "cartoon_output.mp4")
    out = cv2.VideoWriter(output_path, fourcc, FRAME_RATE, (IMAGE_WIDTH, IMAGE_HEIGHT))

    while cap.isOpened():
        start_time = time.time()
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (IMAGE_WIDTH, IMAGE_HEIGHT))
        cartoon_frame = cartoonify(frame)
        out.write(cartoon_frame)
        cartoon_frame = visualize_fps(cartoon_frame, fps)
        cv2.imshow("Video Cartoonified", cartoon_frame)

        end_time = time.time()
        seconds = end_time - start_time
        if seconds < DURATION:
            time.sleep(DURATION - seconds)
        fps = 1 / (time.time() - start_time)

        if cv2.waitKey(33) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
