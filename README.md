# OCR Project

## Installation

1. Install Tesseract OCR:
   - Download and install from: https://github.com/UB-Mannheim/tesseract/wiki
   - Or use winget: `winget install UB-Mannheim.TesseractOCR`

2. Install Khmer language data:
   - Download `khm.traineddata` from: https://github.com/tesseract-ocr/tessdata/raw/main/khm.traineddata
   - Place it in `C:\Program Files\Tesseract-OCR\tessdata\`

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

## Run

python -m streamlit run main.py