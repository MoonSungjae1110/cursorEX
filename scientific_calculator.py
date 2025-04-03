import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("공학용 계산기")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # 결과 표시창
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # 이전 입력값 저장
        self.previous_value = 0
        self.operation = None
        self.start_new_number = True
        
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
        
        # 버튼 텍스트와 위치 정의
        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('√', 1, 3),
            ('log', 2, 0), ('ln', 2, 1), ('x²', 2, 2), ('x³', 2, 3),
            ('(', 3, 0), (')', 3, 1), ('π', 3, 2), ('e', 3, 3),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
            ('0', 7, 0), ('.', 7, 1), ('=', 7, 2), ('+', 7, 3),
            ('C', 8, 0), ('CE', 8, 1), ('⌫', 8, 2), ('±', 8, 3)
        ]
        
        # 버튼 생성
        for (text, row, col) in buttons:
            button = ttk.Button(
                self.root,
                text=text,
                command=lambda x=text: self.button_click(x)
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        # 그리드 가중치 설정
        for i in range(9):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def button_click(self, value):
        current = self.result_var.get()
        
        if value == 'C':
            self.result_var.set("0")
            self.start_new_number = True
        elif value == 'CE':
            self.result_var.set("0")
            self.start_new_number = True
        elif value == '⌫':
            if len(current) > 1:
                self.result_var.set(current[:-1])
            else:
                self.result_var.set("0")
                self.start_new_number = True
        elif value == '±':
            if current.startswith('-'):
                self.result_var.set(current[1:])
            else:
                self.result_var.set('-' + current)
        elif value == '=':
            try:
                # 수학 함수 처리
                expression = current.replace('π', str(math.pi))
                expression = expression.replace('e', str(math.e))
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('log', 'math.log10')
                expression = expression.replace('ln', 'math.log')
                expression = expression.replace('√', 'math.sqrt')
                
                # 각도는 라디안으로 변환
                if 'math.sin' in expression or 'math.cos' in expression or 'math.tan' in expression:
                    expression = expression.replace('math.sin', 'math.sin(math.radians')
                    expression = expression.replace('math.cos', 'math.cos(math.radians')
                    expression = expression.replace('math.tan', 'math.tan(math.radians')
                    expression += ')'
                
                result = eval(expression)
                self.result_var.set(str(result))
                self.start_new_number = True
            except:
                self.result_var.set("Error")
                self.start_new_number = True
        elif value in ['+', '-', '*', '/']:
            self.previous_value = float(current)
            self.operation = value
            self.start_new_number = True
        elif value == 'x²':
            try:
                result = float(current) ** 2
                self.result_var.set(str(result))
                self.start_new_number = True
            except:
                self.result_var.set("Error")
                self.start_new_number = True
        elif value == 'x³':
            try:
                result = float(current) ** 3
                self.result_var.set(str(result))
                self.start_new_number = True
            except:
                self.result_var.set("Error")
                self.start_new_number = True
        else:
            if self.start_new_number:
                self.result_var.set(value)
                self.start_new_number = False
            else:
                self.result_var.set(current + value)
                
            if self.operation and not self.start_new_number:
                try:
                    current_value = float(current)
                    if self.operation == '+':
                        result = self.previous_value + current_value
                    elif self.operation == '-':
                        result = self.previous_value - current_value
                    elif self.operation == '*':
                        result = self.previous_value * current_value
                    elif self.operation == '/':
                        result = self.previous_value / current_value
                    self.result_var.set(str(result))
                except:
                    self.result_var.set("Error")
                    self.start_new_number = True

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop() 