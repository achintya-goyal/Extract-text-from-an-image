import cv2
import pytesseract

# added this because I was having error regarding the location of tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def get_text(im):
    text = pytesseract.image_to_string(im)
    return text


# get grey scale image
def grayscale(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


# noise removal
def removeNoise(im):
    return cv2.medianBlur(im, 3)


# threshold
def thresholding(im):
    return cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = cv2.imread('th.png')
img = grayscale(img)
img = removeNoise(img)
img = thresholding(img)

print(get_text(img))
