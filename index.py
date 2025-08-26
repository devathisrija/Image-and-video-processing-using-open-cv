
import cv2
import numpy as np
import uuid
from datetime import datetime
from logging_file import setup_logging  # Make sure this is correctly imported

# Initialize logging
logger = setup_logging("index.log")


class IMAGE_PROCESSING:
    def __init__(self):
        self.image = None
        self.coords = []

    def set_image(self, image):
        self.image = image

    def mouse_click(self):
        try:
            logger.info("Waiting for mouse click coordinates")
            coords = []

            # Create a copy of the image to draw on
            display_img = self.image.copy()

            def click_event(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    # Add coordinates to list
                    coords.append((x, y))
                    logger.info(f"Clicked at: {x}, {y}")

                    # Draw a red circle at click location
                    cv2.circle(display_img, (x, y), 5, (0, 0, 255), -1)

                    # If we have multiple points, draw lines between them
                    if len(coords) > 1:
                        cv2.line(display_img, coords[-2], coords[-1], (0, 255, 0), 2)

                    # Update the displayed image
                    cv2.imshow("Click to select point(s)", display_img)

            # Show the initial image
            cv2.imshow("Click to select point(s)", display_img)
            cv2.setMouseCallback("Click to select point(s)", click_event)

            # Wait for user to press a key
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return coords
        except Exception as e:
            logger.error(f"Mouse click error: {e}")
            return []

    def line(self, color, thickness):
        try:
            coords = self.mouse_click()
            if len(coords) >= 2:
                cv2.line(self.image, coords[0], coords[1], color, thickness)
            image_path = f"static/outputs/line_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, self.image)
            return image_path
        except Exception as e:
            logger.error(f"Line drawing error: {e}")

    def arrow_line(self, color, thickness):
        try:
            coords = self.mouse_click()
            if len(coords) >= 2:
                cv2.arrowedLine(self.image, coords[0], coords[1], color, thickness)
            image_path = f"static/outputs/line_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, self.image)
            return image_path
        except Exception as e:
            logger.error(f"Line drawing error: {e}")

    def rectangle(self, color, thickness):
        try:
            coords = self.mouse_click()
            if len(coords) >= 2:
                cv2.rectangle(self.image, coords[0], coords[1], color, thickness)
            image_path = f"static/outputs/rectangle_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, self.image)
            return image_path
        except Exception as e:
            logger.error(f"Rectangle drawing error: {e}")

    def circle(self, radius, color, thickness):
        try:
            coords = self.mouse_click()
            if coords:
                cv2.circle(self.image, coords[0], radius, color, thickness)
            image_path = f"static/outputs/circle_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, self.image)
            return image_path
        except Exception as e:
            logger.error(f"Circle drawing error: {e}")

    def roi(self):
        try:
            # Create a named window
            cv2.namedWindow("Select ROI Points", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Select ROI Points", 800, 600)

            # Make a copy of the image to draw on
            display_img = self.image.copy()
            coords = []

            # Mouse callback function
            def mouse_callback(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    coords.append((x, y))
                    logger.info(f"Clicked at: ({x}, {y})")
                    # Draw a circle at the clicked point
                    cv2.circle(display_img, (x, y), 5, (0, 0, 255), -1)
                    cv2.imshow("Select ROI Points", display_img)

                    # Draw rectangle if we have two points
                    if len(coords) >= 2:
                        cv2.rectangle(display_img, coords[0], coords[1], (0, 255, 0), 2)
                        cv2.imshow("Select ROI Points", display_img)

            # Set mouse callback
            cv2.setMouseCallback("Select ROI Points", mouse_callback)

            # Show the image and wait for clicks
            cv2.imshow("Select ROI Points", display_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Verify we got exactly 3 points
            if len(coords) != 3:
                logger.info("Error: Need exactly 3 points (2 for ROI, 1 for destination)")
                return None

            # Extract ROI
            x1, y1 = coords[0]
            x2, y2 = coords[1]
            roi = self.image[y1:y2, x1:x2].copy()

            # Paste ROI at destination
            dx, dy = coords[2]
            h, w = roi.shape[:2]

            # Ensure paste area is within bounds
            if dy + h > self.image.shape[0] or dx + w > self.image.shape[1]:
                h = min(h, self.image.shape[0] - dy)
                w = min(w, self.image.shape[1] - dx)
                roi = roi[:h, :w]

            self.image[dy:dy + h, dx:dx + w] = roi

            output_path = f"static/outputs/roi_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(output_path, self.image)
            logger.info(f"ROI operation complete. Saved at {output_path}")
            return output_path

        except Exception as e:
            print(f"ROI error: {e}")
            return None

    def text(self, text, font_scale, font, color, thickness):
        try:
            coords = self.mouse_click()
            if coords:
                cv2.putText(self.image, text, coords[0], font, font_scale, color, thickness)
            image_path = f"static/outputs/text_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, self.image)
            return image_path
        except Exception as e:
            logger.error(f"Text insertion error: {e}")

    def datetime(self, font_scale, font, color, thickness):
        try:
            coords = self.mouse_click()
            if coords:
                dt = str(datetime.now())
                cv2.putText(self.image, dt, coords[0], font, font_scale, color, thickness)
            image_path = f"static/outputs/datetime_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, self.image)
            return image_path
        except Exception as e:
            logger.error(f"Datetime insertion error: {e}")

    def resize(self, width, height):
        try:
            logger.info(f"Resizing image to {width}x{height}")

            if self.image is None:
                logger.error("No image loaded for resizing")
                return None

            # Validate dimensions
            if width <= 0 or height <= 0:
                logger.error(f"Invalid dimensions: {width}x{height}")
                return None

            # Perform the resize
            resized = cv2.resize(self.image, (width, height))

            # Save the result
            image_path = f"static/outputs/resized_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, resized)
            logger.info(f"Resized image saved to {image_path}")

            return image_path

        except Exception as e:
            logger.error(f"Resize error: {e}")
            return None

    def add(self, image2):
        try:
            if self.image.shape != image2.shape:
                image2 = cv2.resize(image2, (self.image.shape[1], self.image.shape[0]))
            added = cv2.add(self.image,image2)
            image_path = f"static/outputs/add_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, added)
            return image_path
        except Exception as e:
            logger.error(f"Image weighted add error: {e}")

    def add_weight(self, image2, w1, w2):
        try:
            if self.image.shape != image2.shape:
                image2 = cv2.resize(image2, (self.image.shape[1], self.image.shape[0]))
            added = cv2.addWeighted(self.image, w1, image2, w2, 0)
            image_path = f"static/outputs/add_weighted_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, added)
            return image_path
        except Exception as e:
            logger.error(f"Image weighted add error: {e}")

    def edge(self):
        try:
            kernel_filter = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
            # kernel_filter=np.array([[1,1,1],[0,1,1],[2,1,1]])
            kernel_image = cv2.filter2D(self.image, -1, kernel=kernel_filter)
            image_path = f"static/outputs/edge_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path,kernel_image)
            return image_path
        except Exception as e:
            logger.error(f"Edge detection error: {e}")

    def face_detect_photo(self):
        try:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            image_path = f"static/outputs/face_photo_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(image_path, self.image)
            return image_path
        except Exception as e:
            logger.error(f"Face detection error: {e}")

    def count_frames(self, video_path):
        try:
            logger.info("Counting frames")
            cap = cv2.VideoCapture(video_path)
            total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            cap.release()
            return total
        except Exception as e:
            logger.error(f"Frame count error: {e}")
            return 0

    def overlay_datetime(self, video_path):
        try:
            cap = cv2.VideoCapture(video_path)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            output_path = f"static/outputs/overlay_{uuid.uuid4().hex}.mp4"
            out = cv2.VideoWriter(output_path, fourcc, cap.get(5),
                                  (int(cap.get(3)), int(cap.get(4))))
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                text = cv2.getTickCount()
                datetime_text = cv2.putText(
                    frame, str(datetime.now()), (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                out.write(frame)
            cap.release()
            out.release()
            return output_path
        except Exception as e:
            logger.error(f"Overlay datetime error: {e}")
            return None

    def detect_faces_video(self, video_path):
        try:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            cap = cv2.VideoCapture(video_path)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            output_path = f"static/outputs/facedetect_{uuid.uuid4().hex}.mp4"
            out = cv2.VideoWriter(output_path, fourcc, cap.get(5),
                                  (int(cap.get(3)), int(cap.get(4))))
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                out.write(frame)
            cap.release()
            out.release()
            return output_path
        except Exception as e:
            logger.error(f"Face detect video error: {e}")
            return None
