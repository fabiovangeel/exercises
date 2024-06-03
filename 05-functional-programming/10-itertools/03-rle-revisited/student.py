import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained emotion classification model
model = load_model('emotion_classification_model.h5')

# Define facial expression labels
emotion_labels = ['Angry', 'Disgust', 'Fear',
                  'Happy', 'Sad', 'Surprise', 'Neutral']

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()

# Initialize OpenCV
cap = cv2.VideoCapture(0)  # Use default camera

while True:
    # Read frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Face Detection
    face_results = face_detection.process(frame_rgb)

    # Check if face(s) detected
    if face_results.detections:
        for detection in face_results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, bbox, (0, 255, 0), 2)

            # Extract face region for emotion classification
            face_roi = frame[int(bbox[1]):int(
                bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])]
            if face_roi.shape[0] > 0 and face_roi.shape[1] > 0:
                # Preprocess the face region for input to the model
                face_roi_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                face_roi_resized = cv2.resize(face_roi_gray, (48, 48))
                face_roi_normalized = face_roi_resized / 255.0
                face_roi_reshaped = np.reshape(
                    face_roi_normalized, (1, 48, 48, 1))

                # Perform emotion classification
                predicted_emotion_probs = model.predict(face_roi_reshaped)
                predicted_emotion_label = emotion_labels[np.argmax(
                    predicted_emotion_probs)]

                # Display the predicted emotion label
                cv2.putText(frame, predicted_emotion_label,
                            (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Facial Expression Recognition', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
