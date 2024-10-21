# pdf_text_recognition
side_project_姑姑中華經研院文字辨識需求


https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/quickstart_en.md
paddleOCR_pdftotxt.py

conda create --name pdf_recog python=3.10

# pip install paddlepaddle-gpu # <= gpu version
python -m pip install paddlepaddle

pip install PyMuPDF
pip install albumentations
pip install tkinter

程式目錄下 有個data子目錄放的是要辨識的pdf
然後另有個output子目錄 放的是辨識完成的txt

另有error子目錄，放的是失敗的來源檔案(from data dir) 還有個pass子目錄 將處理成功的來源放到pass
另外有個log子目錄 紀錄每個檔案處理時間 以及失敗的traceback