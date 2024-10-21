import os
import shutil
import time
import traceback
from datetime import datetime
from tkinter import Tk, filedialog, Label, Button, Entry, ttk
from paddleocr import PaddleOCR
import threading

# Initialize OCR Model
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# User Interface
class PDFRecognitionApp:
    def __init__(self, root):
        self.root = root
        root.title("PDF Recognition with PaddleOCR")

        self.label = Label(root, text="Choose the input directory containing PDF files")
        self.label.pack()

        self.choose_dir_button = Button(root, text="Choose Input Directory", command=self.choose_data_directory)
        self.choose_dir_button.pack()

        self.output_label = Label(root, text="Output Directory Name:")
        self.output_label.pack()
        self.output_entry = Entry(root)
        self.output_entry.pack()

        self.start_button = Button(root, text="Start Processing", command=self.start_processing_thread)
        self.start_button.pack()

        self.progress_label = Label(root, text="Progress:")
        self.progress_label.pack()
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack()
        self.progress_status_label = Label(root, text="")
        self.progress_status_label.pack()

    def choose_data_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            global data_dir
            data_dir = directory
            self.label.config(text=f"Selected Directory: {data_dir}")

    def start_processing_thread(self):
        processing_thread = threading.Thread(target=self.start_processing)
        processing_thread.start()

    def start_processing(self):
        # Get output directory name from user
        output_dir_name = self.output_entry.get() or 'output'

        # Directories Setup
        output_dir = os.path.join(os.getcwd(), output_dir_name)
        error_dir = os.path.join(os.getcwd(), 'error')
        pass_dir = os.path.join(os.getcwd(), 'pass')
        log_dir = os.path.join(os.getcwd(), 'log')

        # Create necessary directories if they don't exist
        for directory in [data_dir, output_dir, error_dir, pass_dir, log_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)

        # Initialize logs with timestamp
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        processing_log_path = os.path.join(log_dir, f'processing_log_{timestamp_str}.txt')
        error_log_path = os.path.join(log_dir, f'error_log_{timestamp_str}.txt')
        with open(processing_log_path, 'w') as f:
            f.write("Processing Log\n====================\n")
        with open(error_log_path, 'w') as f:
            f.write("Error Log\n====================\n")

        # Start processing PDF files
        pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith('.pdf')]
        total_files = len(pdf_files)
        self.progress_bar['maximum'] = total_files

        start_time = time.time()
        for idx, pdf_file in enumerate(pdf_files):
            pdf_path = os.path.join(data_dir, pdf_file)

            try:
                # Start timer for each file
                file_start_time = time.time()
                print(f"Processing: {pdf_path}")
                
                # Update progress status for the current file
                self.progress_status_label.config(text=f"Processing file {idx + 1} of {total_files}: {pdf_file}")
                self.root.update_idletasks()
                
                # Perform OCR on the PDF
                result = ocr.ocr(pdf_path, cls=True)
                
                # Extract and write to output file
                all_text = ""
                for page_num, page in enumerate(result):
                    res = page
                    if res:
                        txts = [line[1][0] for line in res]
                        txts_joined = ' '.join(txts)
                        all_text += f"Page {page_num + 1}: {txts_joined} \n"

                output_txt_path = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}.txt")
                with open(output_txt_path, 'w', encoding='utf-8') as f:
                    f.write(all_text)

                # Move successfully processed files to pass directory
                shutil.move(pdf_path, os.path.join(pass_dir, pdf_file))
                
                # Log processing time
                file_end_time = time.time()
                processing_time = file_end_time - file_start_time
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(processing_log_path, 'a') as log_file:
                    log_file.write(f"[{timestamp}] {pdf_file} processed successfully in {processing_time:.2f} seconds\n")

            except Exception as e:
                # Log the error and move the file to the error directory
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(error_log_path, 'a') as error_log:
                    error_log.write(f"[{timestamp}] Error processing {pdf_file}:\n{traceback.format_exc()}\n\n")
                with open(processing_log_path, 'a') as log_file:
                    log_file.write(f"[{timestamp}] ERROR: Failed to process {pdf_file}\n")
                shutil.move(pdf_path, os.path.join(error_dir, pdf_file))

            # Update progress bar and label after each file
            self.progress_bar['value'] = idx + 1
            self.progress_status_label.config(text=f"File {idx + 1} of {total_files} completed: {pdf_file}")
            self.root.update_idletasks()

        end_time = time.time()
        total_processing_time = end_time - start_time
        print(f"All files processed in {total_processing_time:.2f} seconds")
        self.progress_status_label.config(text="Processing complete!")

# Run the Application
if __name__ == "__main__":
    root = Tk()
    pdf_recognition_app = PDFRecognitionApp(root)
    root.mainloop()
