import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # 결과 표시창
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
        
    def create_widgets(self):
        # 결과 표시 레이블
        result_label = ttk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Arial", 20),
            anchor="e",
            padding=10
        )
        result_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # 버튼 텍스트
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # 버튼 생성
        row = 1
        col = 0
        for button_text in buttons:
            button = ttk.Button(
                self.root,
                text=button_text,
                command=lambda x=button_text: self.button_click(x)
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear 버튼
        clear_button = ttk.Button(
            self.root,
            text="C",
            command=self.clear
        )
        clear_button.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=2, pady=2)
        
        # 그리드 가중치 설정
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def button_click(self, value):
        current = self.result_var.get()
        
        if value == '=':
            try:
                result = eval(current)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            if current == "0" or current == "Error":
                self.result_var.set(value)
            else:
                self.result_var.set(current + value)
                
    def clear(self):
        self.result_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop() 