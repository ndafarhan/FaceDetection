import face_recognition
import cv2

# Capture video dari webcam
vid_cap = cv2.VideoCapture(0)

while True:
    # Mendapatkan frame dari video
    _, frame = vid_cap.read()

    # Konversi channel dari BGR ke RGB
    rgb_frame = frame[:, :, ::-1]

    if True:
        # Menentukan koordinat wajah
        face_locations = face_recognition.face_locations(rgb_frame)

    # Buat boundingbox
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, "wajah terdeteksi", (left-25, top-5), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Close window hasil dengan tombol esc
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

vid_cap.release()
cv2.destroyAllWindows()
