import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 뷰어")
        self.root.geometry("800x600")
        
        # 메인 프레임
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 이미지 표시 레이블
        self.image_label = ttk.Label(self.main_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # 버튼 프레임
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=10)
        
        # 이미지 선택 버튼
        self.select_button = ttk.Button(
            self.button_frame,
            text="이미지 선택",
            command=self.select_image
        )
        self.select_button.pack(side=tk.LEFT, padx=5)
        
        # 현재 이미지 저장
        self.current_image = None
        
    def select_image(self):
        # 파일 선택 대화상자 열기
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("이미지 파일", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("모든 파일", "*.*")
            ]
        )
        
        if file_path:
            try:
                # 이미지 로드
                image = Image.open(file_path)
                
                # 이미지 크기 조정 (창 크기에 맞게)
                window_width = self.root.winfo_width()
                window_height = self.root.winfo_height()
                
                # 이미지 비율 유지하면서 크기 조정
                image_ratio = image.width / image.height
                window_ratio = window_width / window_height
                
                if image_ratio > window_ratio:
                    new_width = window_width - 20  # 여백 고려
                    new_height = int(new_width / image_ratio)
                else:
                    new_height = window_height - 20
                    new_width = int(new_height * image_ratio)
                
                image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # PhotoImage 객체 생성
                self.current_image = ImageTk.PhotoImage(image)
                
                # 이미지 표시
                self.image_label.configure(image=self.current_image)
                
            except Exception as e:
                tk.messagebox.showerror("오류", f"이미지를 불러오는 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop() 