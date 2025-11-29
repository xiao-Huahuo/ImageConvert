import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from utils.menu.ico_checker import get_ico_resolutions

class IcoCheckerWindow(ttk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("ICO 分辨率检测器")
        self.geometry("400x300")

        self.transient(master)
        self.lift()
        self.focus_set()

        self._create_widgets()

    def _create_widgets(self):
        main_frame = ttk.Frame(self, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- File Selection ---
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.filepath_var = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.filepath_var, state="readonly").pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        ttk.Button(file_frame, text="选择 ICO 文件...", command=self.check_ico).pack(side=tk.LEFT)

        # --- Results Display ---
        result_frame = ttk.Labelframe(main_frame, text="包含的分辨率", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True)

        self.result_text = tk.Text(result_frame, wrap="word", relief="flat", height=8)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        self.result_text.config(state="disabled")

    def check_ico(self):
        file_path = filedialog.askopenfilename(
            title="选择一个 ICO 文件",
            filetypes=[("ICO files", "*.ico"), ("All files", "*.*")]
        )
        if not file_path:
            return

        self.filepath_var.set(file_path)
        success, data = get_ico_resolutions(file_path)
        
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        
        if success:
            if data:
                resolutions_str = "\n".join([f"- {w}x{h}" for w, h in data])
                self.result_text.insert("1.0", resolutions_str)
            else:
                self.result_text.insert("1.0", "未在此文件中检测到任何分辨率。")
        else:
            self.result_text.insert("1.0", data) # 'data' contains the error message
            
        self.result_text.config(state="disabled")
        
        # 重新获取焦点，以防文件对话框关闭后窗口被置于底层
        self.lift()
        self.focus_set()
