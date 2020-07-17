import cv2

# Load cascade
cascade = cv2.CascadeClassifier('/home/ndafarhan/Documents/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

# Capture video dari webcam
vid_cap = cv2.VideoCapture(0)


while True:
    # Mendapatkan frame dari video
    _, frame = vid_cap.read()
    # Mengkonversi gambar menjadi grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Deteksi wajah dengan cascade yang telah dipanggil
    wajah = cascade.detectMultiScale(grayscale, 1.1, 4)
    # Buat boundingbox
    for (x, y, w, h) in wajah:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "wajah terdeteksi", (x-25, y-5), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 255), 1)
    # Memunculkan hasil
    cv2.imshow('Video', frame)
    # Close window hasil dengan tombol esc
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

vid_cap.release()
cv2.destroyAllWindows()
