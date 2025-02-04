### Cartoonify



## **📌 Project Description**
This project applies a **cartoon effect** to images, videos, and webcam streams using **OpenCV**. The process involves **image smoothing, edge detection, and color filtering** to produce a cartoon-like output.

The project also supports real-time video processing, displaying frames per second (**FPS**) on the output.



## **Features**
✔ Convert static images to cartoon-like images  
✔ Apply cartoon effect to webcam and live video streams  
✔ Process video files and save cartoonified output  
✔ Display FPS to monitor performance during real-time processing  


## **📌 How It Works**

1. **Static Image Processing:**  
   The script reads an input image, applies the cartoon effect, and displays the output.

2. **Webcam Processing:**  
   The live webcam feed is processed frame by frame, applying the cartoon effect in real time with FPS visualization.

3. **Video Processing:**  
   A video file is processed, and the cartoonified output is saved to the `output` directory.



## **📌 Requirements**
Make sure you have the required libraries installed. Use this command to install dependencies:

```sh
pip install opencv-python opencv-python-headless numpy matplotlib
```



## **📌 How to Run**
### **1. Static Image Processing**
Run this command to apply the cartoon effect to an image:

```sh
python Cartoonify.py --image images/Ali.jpg
```



### **2. Webcam Processing**
Run this command to apply the cartoon effect to a live webcam feed:

```sh
python Cartoonify.py --webcam
```



### **3. Video Processing**
Run this command to apply the cartoon effect to a video file:

```sh
python Cartoonify.py --video videos/Jobs_2.mp4
```



## **🛠 Technologies Used**
- **Python** 🐍  
- **OpenCV** 📷 (Computer Vision library)  
- **Numpy** 🔢 (Numerical processing)  
- **Matplotlib** 📊 (For visualization)  


