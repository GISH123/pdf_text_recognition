# pdf_text_recognition
side_project_姑姑中華經研院文字辨識需求


參考 https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/quickstart_en.md  


執行 paddleOCR_pdftotxt.py  


### environment
conda create --name pdf_recog python=3.10
pip install paddlepaddle-gpu # <= gpu version
python -m pip install paddlepaddle

pip install PyMuPDF  
pip install albumentations  
pip install tkinter  


### doc

使用者可選擇指定資料夾，會辨識資料夾內所有pdf  
! 注意 選擇的資料夾在辨識完成後，會被分類到以下子目錄資料夾  
(1) pass 存放辨識成功並產出txt的pdf檔案  
(2) error 存放過程中因任何原因辨識失敗的pdf檔案  


另有log子目錄  存放辨識過程中的一些處理訊息 如辨識了多久 以及失敗的traceback  

### 打包成exe  

用pyinstaller無法成功，  
參考解決方案 : https://github.com/PaddlePaddle/PaddleOCR/discussions/11490  
會在output資料夾產生出此程式exe的資料夾，我將該資料夾壓縮成zip，存在dist資料夾裡面  

因檔案太大無法上傳至git，我存到google drive，以下網址可下載可使用的執行檔  
https://drive.google.com/file/d/1h6CwzvTACbjsJDo10YKmpbstmrNFu6Vw/view?usp=drive_link  