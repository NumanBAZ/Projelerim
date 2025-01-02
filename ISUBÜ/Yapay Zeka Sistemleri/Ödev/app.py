import os
from flask import Flask, request, render_template, send_from_directory
import cv2
import numpy as np
from werkzeug.utils import secure_filename

# Flask uygulamasını başlat
app = Flask(__name__)

# Yükleme klasörü
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# İzin verilen dosya uzantıları
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# İzin verilen dosya uzantılarını kontrol etme
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Görüntü işleme fonksiyonları
def gray_histogram(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    histogram_image = cv2.equalizeHist(gray_image)
    return gray_image, histogram_image

def turn(img):
    angle = 45
    center = (img.shape[1] // 2, img.shape[0] // 2)
    scale = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    turn_image = cv2.warpAffine(img, rotation_matrix, (img.shape[1], img.shape[0]))
    return turn_image

def blur(img):
    kernel_size = (15, 15)
    blur_image = cv2.GaussianBlur(img, kernel_size, 0)
    return blur_image

def sobel_canny_laplation(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    sobel_image = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    canny_image = cv2.Canny(gray_image, 50, 150)

    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    laplacian_image = cv2.convertScaleAbs(laplacian)

    return sobel_image, canny_image, laplacian_image

def edge(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_float = np.float32(gray_image)
    harris_corners = cv2.cornerHarris(gray_float, blockSize=7, ksize=3, k=0.04)

    harris_image = img.copy()
    harris_image[harris_corners > 0.01 * harris_corners.max()] = [0, 255, 255]

    corners = cv2.goodFeaturesToTrack(gray_image, maxCorners=100, qualityLevel=0.01, minDistance=10)
    corners = np.int8(corners)
    shitomasi_image = img.copy()
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(shitomasi_image, (x, y), 5, (0, 255, 0), -1)  # Yeşil noktalar

    return harris_image, shitomasi_image

def contour(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contour_image = img.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Yeşil renk, kalınlık: 2
    return contour_image

def erosion(img):
    # Gri tonlamaya çevirme
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aşındırma işlemi için kernel oluşturuluyor
    kernel = np.ones((5,5), np.uint8)
    erosion_image = cv2.erode(gray_image, kernel, iterations=1)
    return erosion_image

def dilation(img):
    # Gri tonlamaya çevirme
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Genişletme işlemi için kernel oluşturuluyor
    kernel = np.ones((5,5), np.uint8)
    dilation_image = cv2.dilate(gray_image, kernel, iterations=1)
    return dilation_image

def treshold(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_value = 127  # Eşik değeri
    max_value = 255        # Üst değer (beyaz)
    _, binary_thresh = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_BINARY)
    return binary_thresh

# Ana sayfa
@app.route('/')
def index():
    return render_template("index.html")

# Resim yükleme ve işlem yapma
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "Dosya seçilmedi!", 400

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Resmi yükle ve işle
        orjinal_img = cv2.imread(filepath)
        img = cv2.imread(filepath)
        gray_image, histogram_image = gray_histogram(img)
        turn_image = turn(img)
        blur_image = blur(img)
        sobel_image, canny_image, laplacian_image = sobel_canny_laplation(img)
        harris_image, shitomasi_image = edge(img)
        contour_image = contour(img)
        binary_thresh = treshold(img)
        erosion_image = erosion(img)
        dilation_image = dilation(img)

        # İşlenmiş resimleri kaydet
        processed_images = {
            'orjinal_img':'orjinal_img.png',
            'gray_image': 'gray_image.png',
            'histogram_image': 'histogram_image.png',
            'turn_image': 'turn_image.png',
            'blur_image': 'blur_image.png',
            'sobel_image': 'sobel_image.png',
            'canny_image': 'canny_image.png',
            'laplacian_image': 'laplacian_image.png',
            'harris_image': 'harris_image.png',
            'shitomasi_image': 'shitomasi_image.png',
            'contour_image': 'contour_image.png',
            'threshold_image': 'threshold_image.png',
            'erosion_image': "erosion_image.png",
            'dilation_image': "dilation_image.png"
        }

        # Kaydetme işlemi
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['orjinal_img']), orjinal_img)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['gray_image']), gray_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['histogram_image']), histogram_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['turn_image']), turn_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['blur_image']), blur_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['sobel_image']), sobel_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['canny_image']), canny_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['laplacian_image']), laplacian_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['harris_image']), harris_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['shitomasi_image']), shitomasi_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['contour_image']), contour_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['threshold_image']), binary_thresh)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['erosion_image']), erosion_image)
        cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], processed_images['dilation_image']), dilation_image)

        # İşlenmiş resimleri gösterme
        return render_template("images.html", processed_images=processed_images)

# Yüklenen dosyayı sunma
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# İşlenmiş dosyayı sunma
@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    app.run(debug=True)
