# Image-and-video-processing-using-open-cv
# 🖼️🎥 Image & Video Processor  
_A powerful web-based tool for all your media processing needs_

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


## ⚙️ Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/image-video-processor.git
   cd image-video-processor
2. **Create virtual environment :**
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
3. **Install dependencies :**
   pip install -r requirements.txt
4. **Run the Flask app :**
   python app.py
5. **Open the browser and visit :**
   http://127.0.0.1:5000/



