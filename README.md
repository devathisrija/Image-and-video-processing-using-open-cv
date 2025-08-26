# Image-and-video-processing-using-open-cv
## 🖼️🎥 Image & Video Processor  
_A powerful web-based tool for all your media processing needs_

---

## 📌 Overview  
This project is a **Flask-based Image and Video Processing Application** that allows users to perform a wide variety of editing and analysis tasks directly through the browser.  
Built using **Python, Flask, OpenCV, HTML, CSS, and JavaScript**, it eliminates the need for heavy desktop software and provides an easy-to-use, interactive interface.  

Users can:  
- Upload **images** and perform operations such as drawing shapes, adding text/timestamps, resizing, face detection, edge detection, ROI selection, and blending images.  
- Upload **videos** (up to 200MB) and perform frame counting, overlay timestamps, and detect faces on every frame.  
- **Preview and download** processed results (JPG/PNG for images, MP4 for videos).  

---

## 🚀 Features  

### 🖼️ Image Processing  
- Draw **Line, Arrow, Rectangle, Circle** with mouse-click selection  
- Add **custom text** or **current date & time**  
- Select **Region of Interest (ROI)** and crop/paste  
- **Resize** images to desired dimensions  
- Detect **faces** using OpenCV Haar cascades  
- Perform **edge detection** (Canny & filters)  
- **Add or blend images** (normal/weighted)  

### 🎥 Video Processing  
- Get **total frame count** of uploaded videos  
- Overlay **date & time** on every frame  
- Perform **real-time face detection** per frame  

### 💾 Output Options  
- Download **processed images** in JPG/PNG format  
- Download **processed videos** in MP4 format  

---

## 🛠️ Tech Stack  

**Backend**  
- Python 3.10  
- Flask 2.2  
- OpenCV 4.6.0  
- NumPy  

**Frontend**  
- HTML5, CSS3, JavaScript  
- Bootstrap (for responsive UI)  

**Version Control**  
- Git & GitHub

---

## 📂 Project Structure  

```plaintext
├── app.py              # Flask main application
├── index.py            # Image & video processing logic (OpenCV)
├── templates/          # HTML templates (index, line, circle, text, etc.)
│   ├── index.html
│   ├── line.html
│   ├── circle.html
│   ├── text.html
│   ├── resize.html
│   ├── add.html
│   ├── add_weight.html
│   ├── roi.html
│   ├── edge.html
│   ├── face_detect_photo.html
│   └── other feature-specific pages...
├── static/             # Static files (uploaded & processed content)
│   ├── uploads/        # Uploaded images/videos
│   ├── outputs/        # Processed images/videos
│   ├── videos/         # Uploaded videos
│   ├── css/            # Stylesheets
│   └── js/             # JavaScript files
├── logging_file.py     # Custom logging setup
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── screenshots/        # Screenshots for README (optional)
```

---

## ⚙️ Installation & Setup  

Follow these steps to set up and run the project locally:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/image-video-processor.git
   cd image-video-processor
   ```

2. **(Optional) Create a virtual environment**  
   It’s recommended to use a virtual environment to avoid dependency conflicts.  
   ```bash
   python -m venv venv
   ```

   Activate it:  
   - **Windows (PowerShell):**  
     ```bash
     venv\Scripts\activate
     ```
   - **Linux / macOS:**  
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**  
   ```bash
   python app.py
   ```

5. **Open the application in your browser**  
   ```
   http://127.0.0.1:5000/
   ```

✅ Now your app should be running locally — you can upload images/videos and try all processing features.

---
## 11. Screenshots

This section provides visual references for each feature of the **Image & Video Processing Application**.  

### Image Processing Features

**Upload Image**  
![Upload Image](screenshots/Screenshot (652).png)


**Draw Line**  
![Draw Line](path/to/screenshot2.png)  

**Add Text**  
![Add Text](path/to/screenshot3.png)  

**Draw Circle**  
![Draw Circle](path/to/screenshot4.png)  

**Add Date/Time**  
![Add DateTime](path/to/screenshot5.png)  

**Image Addition**  
![Add Images](path/to/screenshot6.png)  

**Weighted Addition**  
![Weighted Add](path/to/screenshot7.png)  

**Edge Detection**  
![Edge Detection](path/to/screenshot8.png)  

**Face Detection (Image)**  
![Face Detection](path/to/screenshot9.png)  

### Video Processing Features

**Upload Video**  
![Upload Video](path/to/screenshot10.png)  

**Frame Count**  
![Frame Count](path/to/screenshot11.png)  

**Date/Time Overlay (Video)**  
![DateTime Video](path/to/screenshot12.png)  

**Face Detection (Video)**  
![Face Detection Video](path/to/screenshot13.png)  

> **Note:** Replace `path/to/screenshotX.png` with the actual paths to your screenshots.


## 🧪 Testing  

The application was tested for:  
- ✅ Valid/invalid file uploads  
- ✅ Image operations (shapes, text, ROI, resize, blending)  
- ✅ Video operations (frame count, overlay timestamp, face detection)  
- ✅ Mobile/desktop responsiveness  

---

## 🚀 Future Enhancements  

- 📷 Real-time webcam support for live processing  
- 📦 Batch processing for multiple images/videos  
- 🎨 Advanced filters & AI-powered image enhancements  
- ☁️ Cloud integration (Google Drive, AWS S3, Dropbox)  
- 🔑 User accounts & history tracking  

---

## 📖 References  

- [Flask Documentation](https://flask.palletsprojects.com/)  
- [OpenCV Documentation](https://docs.opencv.org/)  
- [Python Official Docs](https://docs.python.org/3/)  
- [Bootstrap](https://getbootstrap.com/)  
- [MDN Web Docs](https://developer.mozilla.org/)  

---

## 👩‍💻 Author  

**Devathi Srija**  
_Viharatech | 2025_




