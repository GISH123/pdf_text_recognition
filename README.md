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
另外還要在--hidden-import裡面加入fitz  
執行auto-py-to-exe成功後，  
會在output資料夾產生出此程式exe的資料夾，我將該資料夾壓縮成zip，存在dist資料夾裡面  

因檔案太大無法上傳至git，我存到google drive，以下網址可下載可使用的執行檔  
https://drive.google.com/file/d/1h6CwzvTACbjsJDo10YKmpbstmrNFu6Vw/view?usp=drive_link  

### 執行方式

下載zip檔案解壓縮，執行裡面的exe檔案，會跑出一個小介面(如果沒有的話應該就是被縮小了，請在下方工具列打開一個羽毛圖案的視窗)  
先點選上面的按鈕選擇要辨識的資料夾(裡面放pdf檔案，程式也只會抓副檔名為pdf的檔案)  
然後點選下面的開始辨識按鈕

如圖  
![Alt text](示意圖.png "preview")  

### 速度問題

當前版本使用的是CPU版本，GPU會快很多，但是要裝對應的cuda跟cudnn，根據每張顯卡的版本要裝不同的版，會有點麻煩，  
這部分要弄的話就是希望可以去現場或者遠端操控需要裝gpu版本的電腦直接安裝  