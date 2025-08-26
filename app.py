from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import cv2
import os
import uuid
from index import IMAGE_PROCESSING
from werkzeug.utils import secure_filename
from logging_file import setup_logging  # Your custom logging import

# Initialize logging
logger = setup_logging("app.log")

UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
VIDEO_FOLDER = 'static/videos'
app = Flask(__name__)
app.secret_key = "secret123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['VIDEO_FOLDER'] = VIDEO_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

uploaded_image_path = None
uploaded_video_path = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global uploaded_image_path
    if request.method == 'POST':
        image = request.files.get('image')
        if image:
            filename = secure_filename(image.filename)
            uploaded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(uploaded_image_path)
            logger.info(f"Image uploaded: {uploaded_image_path}")
            return render_template('index.html', image_url='/' + uploaded_image_path)
        video = request.files.get('video')
        if video:
            filename = secure_filename(video.filename)
            uploaded_video_path = os.path.join(app.config['VIDEO_FOLDER'], filename)
            video.save(uploaded_video_path)
            logger.info(f"Video uploaded: {uploaded_video_path}")
            return render_template('index.html', video_url='/' + uploaded_video_path)
    return render_template('index.html')

@app.route('/line', methods=['GET', 'POST'])
def line():
    global uploaded_image_path
    if request.method == 'POST':
        hex_color = request.form.get('color', '#ff0000').lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))  # Convert hex to RGB
        bgr = rgb[::-1]
        thickness = int(request.form.get('thickness', 2))
        img = cv2.imread(uploaded_image_path)
        processor = IMAGE_PROCESSING()
        processor.set_image(img)
        output_path = processor.line(color=bgr, thickness=thickness)
        return render_template('line.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('line.html')

@app.route('/arrowed_line', methods=['GET', 'POST'])
def arrow():
    global uploaded_image_path
    if request.method == 'POST':
        hex_color = request.form.get('color', '#ff0000').lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))  # Convert hex to RGB
        bgr = rgb[::-1]
        thickness = int(request.form.get('thickness', 2))
        img = cv2.imread(uploaded_image_path)
        processor = IMAGE_PROCESSING()
        processor.set_image(img)
        output_path = processor.arrow_line(color=bgr, thickness=thickness)
        return render_template('arrowed_line.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('arrowed_line.html')

@app.route('/rectangle', methods=['GET', 'POST'])
def rectangle():
    global uploaded_image_path
    if request.method == 'POST':
        hex_color = request.form.get('color', '#ff0000').lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))  # Convert hex to RGB
        bgr = rgb[::-1]
        thickness = int(request.form.get('thickness', 3))
        img = cv2.imread(uploaded_image_path)
        processor = IMAGE_PROCESSING()
        processor.set_image(img)
        output_path = processor.rectangle(color=bgr, thickness=thickness)
        return render_template('rectangle.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('rectangle.html')


@app.route('/roi', methods=['GET', 'POST'])
def roi():
    global uploaded_image_path
    if not uploaded_image_path:
        return "No image uploaded", 400

    img = cv2.imread(uploaded_image_path)
    processor = IMAGE_PROCESSING()
    processor.set_image(img)

    output_path = processor.roi()

    if output_path:
        return render_template('roi.html',
                               image_url='/' + output_path,
                               download_url='/' + output_path)
    else:
        return "ROI operation failed. Please try again.", 400





@app.route('/circle', methods=['GET', 'POST'])
def circle():
    global uploaded_image_path
    if request.method == 'POST':
        hex_color = request.form.get('color', '#ff0000').lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))  # Convert hex to RGB
        bgr = rgb[::-1]
        thickness = int(request.form.get('thickness', 3))
        radius = int(request.form.get('radius', 30))
        img = cv2.imread(uploaded_image_path)
        processor = IMAGE_PROCESSING()
        processor.set_image(img)
        output_path = processor.circle(color=bgr, thickness=thickness, radius=radius)
        return render_template('circle.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('circle.html')

@app.route('/text', methods=['GET', 'POST'])
def text():
    global uploaded_image_path
    if request.method == 'POST':
        message = request.form.get('text', 'Hello!')
        hex_color = request.form.get('color', '#ff0000').lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))  # Convert hex to RGB
        bgr = rgb[::-1]
        thickness = int(request.form.get('thickness', 2))
        font_scale = float(request.form.get('font_size', 1))
        font_style = int(request.form.get('font_style', 0))
        img = cv2.imread(uploaded_image_path)
        processor = IMAGE_PROCESSING()
        processor.set_image(img)
        output_path = processor.text(text=message, color=bgr, thickness=thickness, font_scale=font_scale, font=font_style)
        return render_template('text.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('text.html')

@app.route('/datetime', methods=['GET', 'POST'])
def datetime_add():
    global uploaded_image_path
    if request.method == 'POST':
        hex_color = request.form.get('color', '#ff0000').lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))  # Convert hex to RGB
        bgr = rgb[::-1]
        thickness = int(request.form.get('thickness', 1))
        font_scale = float(request.form.get('font_size', 0.7))
        font_style = int(request.form.get('font_style', 1))
        img = cv2.imread(uploaded_image_path)
        processor = IMAGE_PROCESSING()
        processor.set_image(img)
        output_path = processor.datetime(color=bgr, thickness=thickness, font=font_style, font_scale=font_scale)
        return render_template('date_time.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('date_time.html')


@app.route('/resize', methods=['GET', 'POST'])
def resize_image():
    global uploaded_image_path
    if request.method == 'POST':
        if not uploaded_image_path or not os.path.exists(uploaded_image_path):
            flash("No image uploaded or image not found", "error")
            return redirect(url_for('index'))

        try:
            # Get user inputs
            width = int(request.form.get('width'))
            height = int(request.form.get('height'))

            # Load image
            img = cv2.imread(uploaded_image_path)
            if img is None:
                flash("Failed to load the image", "error")
                return redirect(url_for('index'))

            # Create processor and resize
            processor = IMAGE_PROCESSING()
            processor.set_image(img)
            output_path = processor.resize(width, height)

            if output_path:
                return render_template('resize.html',
                                       image_url='/' + output_path,
                                       download_url='/' + output_path,
                                       original_width=img.shape[1],
                                       original_height=img.shape[0])
            else:
                flash("Invalid resize dimensions", "error")
                return redirect(url_for('resize_image'))

        except ValueError:
            flash("Please enter valid numbers for width and height", "error")
            return redirect(url_for('resize_image'))
        except Exception as e:
            logger.error(f"Resize error: {e}")
            flash("An error occurred during resizing", "error")
            return redirect(url_for('resize_image'))

    # GET request - show form with original dimensions
    if uploaded_image_path and os.path.exists(uploaded_image_path):
        img = cv2.imread(uploaded_image_path)
        if img is not None:
            return render_template('resize.html',
                                   original_width=img.shape[1],
                                   original_height=img.shape[0])

    return render_template('resize.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    global uploaded_image_path
    if request.method == 'POST':
        file = request.files.get('second_image')
        if not file:
            return "Second image not provided", 400


        second_image_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(second_image_path)

        img1 = cv2.imread(uploaded_image_path)
        img2 = cv2.imread(second_image_path)

        processor = IMAGE_PROCESSING()
        processor.set_image(img1)
        output_path = processor.add(img2)
        return render_template('add.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('add.html')

@app.route('/add_weight', methods=['GET', 'POST'])
def add_weight():
    global uploaded_image_path
    if request.method == 'POST':
        file = request.files.get('second_image')
        if not file:
            return "Second image not provided", 400

        w1 = float(request.form.get('w1', 0.5))
        w2 = float(request.form.get('w2', 0.5))

        second_image_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(second_image_path)

        img1 = cv2.imread(uploaded_image_path)
        img2 = cv2.imread(second_image_path)

        processor = IMAGE_PROCESSING()
        processor.set_image(img1)
        output_path = processor.add_weight(img2, w1, w2)
        return render_template('add_weight.html', image_url='/' + output_path, download_url='/' + output_path)
    return render_template('add_weight.html')

@app.route('/edge', methods=['GET', 'POST'])
def edge():
    global uploaded_image_path
    img = cv2.imread(uploaded_image_path)
    processor = IMAGE_PROCESSING()
    processor.set_image(img)
    output_path = processor.edge()
    return render_template('edge.html', image_url='/' + output_path, download_url='/' + output_path)

@app.route('/face_detect_photo', methods=['GET', 'POST'])
def detect_faces_photo():
    global uploaded_image_path
    img = cv2.imread(uploaded_image_path)
    processor = IMAGE_PROCESSING()
    processor.set_image(img)
    output_path = processor.face_detect_photo()
    return render_template('face_detect_photo.html', image_url='/' + output_path, download_url='/' + output_path)

@app.route('/video', methods=['GET', 'POST'])
def video():
    global uploaded_video_path
    if request.method == 'POST':
        video = request.files['video']
        if video:
            filename = secure_filename(video.filename)
            uploaded_video_path = os.path.join(app.config['VIDEO_FOLDER'], filename)
            video.save(uploaded_video_path)
            return render_template('index.html', video_url='/' + uploaded_video_path)
    return render_template('index.html')

@app.route('/frame_count', methods=['POST'])
def frame_count():
    processor = IMAGE_PROCESSING()
    count = processor.count_frames(uploaded_video_path)
    return render_template('index.html', video_url='/' + uploaded_video_path, frame_count=count)

@app.route('/overlay_datetime', methods=['POST'])
def overlay_datetime():
    processor = IMAGE_PROCESSING()
    output_path = processor.overlay_datetime(uploaded_video_path)
    return render_template('index.html', video_url='/' + uploaded_video_path, overlay_output='/' + output_path)

@app.route('/face_detect_video', methods=['POST'])
def face_detect_video():
    processor = IMAGE_PROCESSING()
    output_path = processor.detect_faces_video(uploaded_video_path)
    return render_template('index.html', video_url='/' + uploaded_video_path, face_detect_output='/' + output_path)


if __name__ == '__main__':
    app.run(debug=True)

