import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import os
import time

class Slideshow:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 슬라이드쇼")
        self.root.geometry("800x600")
        
        # 이미지 리스트와 현재 인덱스
        self.images = []
        self.current_index = -1
        
        # 메인 프레임
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 이미지 표시 레이블
        self.image_label = ttk.Label(self.main_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # 컨트롤 프레임
        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(fill=tk.X, pady=10)
        
        # 폴더 선택 버튼
        self.folder_button = ttk.Button(
            self.control_frame,
            text="폴더 선택",
            command=self.select_folder
        )
        self.folder_button.pack(side=tk.LEFT, padx=5)
        
        # 시작/정지 버튼
        self.start_button = ttk.Button(
            self.control_frame,
            text="시작",
            command=self.toggle_slideshow
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # 이전/다음 버튼
        self.prev_button = ttk.Button(
            self.control_frame,
            text="이전",
            command=self.prev_image
        )
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = ttk.Button(
            self.control_frame,
            text="다음",
            command=self.next_image
        )
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        # 현재 이미지 저장
        self.current_image = None
        self.is_playing = False
        self.after_id = None
        
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.images = []
            # 지원하는 이미지 확장자
            image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
            
            # 폴더 내의 이미지 파일 찾기
            for file in os.listdir(folder_path):
                if file.lower().endswith(image_extensions):
                    self.images.append(os.path.join(folder_path, file))
            
            if self.images:
                self.current_index = 0
                self.show_current_image()
                messagebox.showinfo("알림", f"{len(self.images)}개의 이미지를 찾았습니다.")
            else:
                messagebox.showwarning("경고", "선택한 폴더에 이미지가 없습니다.")
    
    def show_current_image(self):
        if 0 <= self.current_index < len(self.images):
            try:
                # 이미지 로드
                image = Image.open(self.images[self.current_index])
                
                # 이미지 크기 조정 (창 크기에 맞게)
                window_width = self.root.winfo_width()
                window_height = self.root.winfo_height()
                
                # 이미지 비율 유지하면서 크기 조정
                image_ratio = image.width / image.height
                window_ratio = window_width / window_height
                
                if image_ratio > window_ratio:
                    new_width = window_width - 20
                    new_height = int(new_width / image_ratio)
                else:
                    new_height = window_height - 20
                    new_width = int(new_height * image_ratio)
                
                image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # PhotoImage 객체 생성
                self.current_image = ImageTk.PhotoImage(image)
                
                # 이미지 표시
                self.image_label.configure(image=self.current_image)
                
                # 현재 이미지 정보 표시
                self.root.title(f"이미지 슬라이드쇼 - {self.current_index + 1}/{len(self.images)}")
                
            except Exception as e:
                messagebox.showerror("오류", f"이미지를 불러오는 중 오류가 발생했습니다: {str(e)}")
    
    def next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.show_current_image()
    
    def prev_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.show_current_image()
    
    def toggle_slideshow(self):
        if not self.images:
            messagebox.showwarning("경고", "먼저 폴더를 선택해주세요.")
            return
            
        if self.is_playing:
            self.is_playing = False
            self.start_button.configure(text="시작")
            if self.after_id:
                self.root.after_cancel(self.after_id)
        else:
            self.is_playing = True
            self.start_button.configure(text="정지")
            self.auto_advance()
    
    def auto_advance(self):
        if self.is_playing:
            self.next_image()
            self.after_id = self.root.after(3000, self.auto_advance)  # 3초마다 다음 이미지

if __name__ == "__main__":
    root = tk.Tk()
    app = Slideshow(root)
    root.mainloop() 