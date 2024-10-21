# pdf_text_recognition
side_project_姑姑中華經研院文字辨識需求

因檔案太大無法上傳至git，我存到google drive，以下網址可下載可使用的執行檔  
https://drive.google.com/file/d/1h6CwzvTACbjsJDo10YKmpbstmrNFu6Vw/view?usp=drive_link  

### 執行方式

下載上面的google drive連結，zip檔案解壓縮，執行裡面的exe檔案，會跑出一個小介面(如果沒有的話應該就是被縮小了，請在下方工具列打開一個羽毛圖案的視窗)  
先點選上面的按鈕選擇要辨識的資料夾(裡面放pdf檔案，程式也只會抓副檔名為pdf的檔案)  
然後點選下面的開始辨識按鈕

如圖  
![Alt text](示意圖.png "preview")  

執行完後，解壓縮後的資料夾裡面會有四個資料夾，  
(1)error  
辨識失敗的pdf會被移到這裡  
(2)pass
辨識成功的pdf會被移到這裡  
(3)log
啟動一次會有兩個檔案，error_log紀錄失敗原因與時間戳記，跟processing_log紀錄花費時間跟時間戳記  
(4)output  
產生之文字檔會放在這  


### 速度問題

當前版本使用的是CPU版本，GPU會快很多，但是要裝對應的cuda跟cudnn，根據每張顯卡的版本要裝不同的版，會有點麻煩，  
這部分要弄的話就是希望可以去現場或者遠端操控需要裝gpu版本的電腦直接安裝  







### environment (從這裡開始，非開發者可無視)  

參考 https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/quickstart_en.md  

conda create --name pdf_recog python=3.10  
pip install paddlepaddle-gpu # <= gpu version  
python -m pip install paddlepaddle  

pip install PyMuPDF  
pip install albumentations  
pip install tkinter  

### 打包成exe  

用pyinstaller無法成功，  
參考解決方案 : https://github.com/PaddlePaddle/PaddleOCR/discussions/11490  
另外還要在--hidden-import裡面加入fitz  
執行auto-py-to-exe成功後，  
會在output資料夾產生出此程式exe的資料夾，我將該資料夾壓縮成zip，存在dist資料夾裡面  
