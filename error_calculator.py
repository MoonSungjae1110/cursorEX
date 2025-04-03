import tkinter as tk
from tkinter import ttk, messagebox

class ErrorCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("오차율 계산기")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # 메인 프레임
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 이론값 입력
        ttk.Label(self.main_frame, text="이론값:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.theoretical_var = tk.StringVar()
        self.theoretical_entry = ttk.Entry(self.main_frame, textvariable=self.theoretical_var)
        self.theoretical_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        # 계산값 입력
        ttk.Label(self.main_frame, text="계산값:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.calculated_var = tk.StringVar()
        self.calculated_entry = ttk.Entry(self.main_frame, textvariable=self.calculated_var)
        self.calculated_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        # 계산 버튼
        self.calculate_button = ttk.Button(
            self.main_frame,
            text="오차율 계산",
            command=self.calculate_error
        )
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=20)
        
        # 결과 표시 레이블
        self.result_var = tk.StringVar()
        self.result_var.set("오차율: ")
        self.result_label = ttk.Label(
            self.main_frame,
            textvariable=self.result_var,
            font=("Arial", 12)
        )
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
        
        # 설명 레이블
        explanation = """
        오차율(%) = |(이론값 - 계산값) / 이론값| × 100
        
        ※ 이론값이 0인 경우 오차율을 계산할 수 없습니다.
        """
        self.explanation_label = ttk.Label(
            self.main_frame,
            text=explanation,
            justify=tk.LEFT
        )
        self.explanation_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        # 그리드 가중치 설정
        self.main_frame.grid_columnconfigure(1, weight=1)
        
    def calculate_error(self):
        try:
            theoretical = float(self.theoretical_var.get())
            calculated = float(self.calculated_var.get())
            
            if theoretical == 0:
                messagebox.showerror("오류", "이론값이 0이면 오차율을 계산할 수 없습니다.")
                return
                
            error_rate = abs((theoretical - calculated) / theoretical) * 100
            self.result_var.set(f"오차율: {error_rate:.4f}%")
            
        except ValueError:
            messagebox.showerror("오류", "올바른 숫자를 입력해주세요.")
        except Exception as e:
            messagebox.showerror("오류", f"계산 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ErrorCalculator(root)
    root.mainloop() 