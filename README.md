# OCR Image Text Extraction with OpenCV and Tesseract

## Description
This project extracts text from images using Python, OpenCV, and Tesseract OCR. It preprocesses the image (grayscale, noise removal, and thresholding) to improve text recognition accuracy.

## Requirements
Ensure you have Python installed along with the following packages:

```bash
pip install opencv-python pytesseract
```

Additionally, install Tesseract OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki). Make sure to update the path to Tesseract in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Features
- Converts image to grayscale
- Removes noise with median blur
- Applies adaptive thresholding
- Extracts text from the processed image

## Usage
1. Place the target image (`th.png`) in the same directory as the script.
2. Run the script with:

```bash
python extract_text_from_image.py
```

3. The extracted text will print to the console.

## Example Output
```bash
Detected text: "Hello, World!"
```

## Customization
- Adjust `medianBlur()` kernel size for stronger noise removal.
- Change thresholding method for different image types.

## Troubleshooting
- Ensure Tesseract's path is correct.
- If the image is unreadable, tweak preprocessing steps.
- Verify OpenCV and Tesseract versions are up-to-date.
