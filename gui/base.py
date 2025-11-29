import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import os
import json
from datetime import datetime
from utils.converter import convert_image
from configure.settings import file_types, convert_loss
from gui.ico_checker_window import IcoCheckerWindow

class ImageConverterApp(ttk.Window):
    def __init__(self):
        self.settings_file = "user_settings.json"
        self.settings = self._load_settings()
        
        super().__init__(themename=self.settings.get("theme", "litera"))
        self.title("图片转换神器")
        self.geometry("700x600")

        self.input_path = tk.StringVar(value=self.settings.get("default_input_path", ""))
        self.output_path = tk.StringVar(value=self.settings.get("default_output_path", ""))
        self.output_format = tk.StringVar(value=file_types[0] if file_types else '')
        self.output_filename = tk.StringVar()
        self.ico_checker_window = None

        self._create_menu()
        self._create_widgets()
        
        if self.input_path.get():
            base_name = os.path.splitext(os.path.basename(self.input_path.get()))[0]
            self.output_filename.set(base_name)
            self.after(100, self.show_loss_info)

        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _create_menu(self):
        menubar = ttk.Menu(self)
        self.config(menu=menubar)
        
        tools_menu = ttk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="工具", menu=tools_menu)
        tools_menu.add_command(label="ICO 分辨率检测", command=self._open_ico_checker)

    def _open_ico_checker(self):
        if self.ico_checker_window and self.ico_checker_window.winfo_exists():
            self.ico_checker_window.deiconify()
            self.ico_checker_window.lift()
            self.ico_checker_window.focus_set()
        else:
            self.ico_checker_window = IcoCheckerWindow(self)

    def _load_settings(self):
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, "r", encoding="utf-8") as f:
                    return json.load(f)
        except (IOError, json.JSONDecodeError):
            pass
        return {"default_input_path": "", "default_output_path": "", "theme": "litera"}

    def _save_settings(self):
        self.settings["theme"] = self.style.theme.name
        try:
            with open(self.settings_file, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=4)
        except IOError:
            self.log_message("错误：无法保存设置。")

    def _set_default_input_path(self):
        path = self.input_path.get()
        if path and os.path.isfile(path):
            self.settings["default_input_path"] = path
            self.log_message(f"默认输入文件已设置为: {path}")
        else:
            messagebox.showwarning("无效路径", "请先选择一个有效的输入文件。")

    def _set_default_output_path(self):
        path = self.output_path.get()
        if path and os.path.isdir(path):
            self.settings["default_output_path"] = path
            self.log_message(f"默认输出目录已设置为: {path}")
        else:
            messagebox.showwarning("无效路径", "请先选择一个有效的输出目录。")

    def _toggle_theme(self):
        self.style.theme_use("cyborg" if self.style.theme.name == "litera" else "litera")

    def _create_widgets(self):
        main_frame = ttk.Frame(self, padding="15")
        main_frame.pack(fill=BOTH, expand=YES)

        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=X, pady=(0, 10))
        ttk.Label(header_frame, text="图片转换神器", font=("", 18, "bold")).pack(side=LEFT, expand=YES)
        ttk.Button(header_frame, text="🎨", command=self._toggle_theme, bootstyle="secondary-outline").pack(side=RIGHT)

        io_frame = ttk.Labelframe(main_frame, text="文件路径", padding="15")
        io_frame.pack(fill=X, pady=10)
        io_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(io_frame, text="输入文件:").grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
        ttk.Entry(io_frame, textvariable=self.input_path).grid(row=0, column=1, sticky="ew")
        ttk.Button(io_frame, text="选择...", command=self.select_input_file, bootstyle="secondary-outline").grid(row=0, column=2, padx=(5, 0))
        ttk.Button(io_frame, text="设为默认", command=self._set_default_input_path, bootstyle="info-outline").grid(row=0, column=3, padx=(5, 0))

        ttk.Label(io_frame, text="输出目录:").grid(row=1, column=0, padx=(0, 10), pady=5, sticky="w")
        ttk.Entry(io_frame, textvariable=self.output_path).grid(row=1, column=1, sticky="ew")
        ttk.Button(io_frame, text="选择...", command=self.select_output_dir, bootstyle="secondary-outline").grid(row=1, column=2, padx=(5, 0))
        ttk.Button(io_frame, text="设为默认", command=self._set_default_output_path, bootstyle="info-outline").grid(row=1, column=3, padx=(5, 0))

        conv_frame = ttk.Labelframe(main_frame, text="转换操作", padding="15")
        conv_frame.pack(fill=X, pady=10)
        conv_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(conv_frame, text="输出格式:").grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
        format_menu = ttk.Combobox(conv_frame, textvariable=self.output_format, values=file_types, state="readonly")
        format_menu.grid(row=0, column=1, sticky="w")
        format_menu.bind("<<ComboboxSelected>>", self.show_loss_info)

        ttk.Label(conv_frame, text="输出文件名:").grid(row=1, column=0, padx=(0, 10), pady=5, sticky="w")
        ttk.Entry(conv_frame, textvariable=self.output_filename).grid(row=1, column=1, sticky="ew")

        ttk.Button(conv_frame, text="一键转换", command=self.convert, bootstyle="success").grid(row=2, column=1, pady=15)

        log_frame = ttk.Labelframe(main_frame, text="信息日志", padding="10")
        log_frame.pack(fill=BOTH, expand=YES, pady=10)
        
        self.log_text = tk.Text(log_frame, height=15, relief="flat")
        self.log_text.pack(fill=BOTH, expand=YES)
        self.log_text.config(state=tk.DISABLED)

    def select_input_file(self):
        initial_dir = os.path.dirname(self.settings.get("default_input_path", "/"))
        filetypes_list = [f"*.{ext}" for ext in file_types if ext != 'svg']
        filetypes_str = " ".join(filetypes_list)
        
        path = filedialog.askopenfilename(
            title="选择图片文件",
            initialdir=initial_dir if os.path.isdir(initial_dir) else "/",
            filetypes=[("Image Files", filetypes_str), ("All files", "*.*")]
        )
        if path:
            self.input_path.set(path)
            base_name = os.path.splitext(os.path.basename(path))[0]
            self.output_filename.set(base_name)
            if not self.output_path.get():
                self.output_path.set(os.path.dirname(path))
            self.log_message(f"已选择输入文件: {path}")
            self.show_loss_info()

    def select_output_dir(self):
        initial_dir = self.settings.get("default_output_path", "")
        path = filedialog.askdirectory(
            title="选择输出目录",
            initialdir=initial_dir if os.path.isdir(initial_dir) else "/"
        )
        if path:
            self.output_path.set(path)
            self.log_message(f"已选择输出目录: {path}")

    def show_loss_info(self, event=None):
        input_p = self.input_path.get()
        if not input_p: return
        
        input_ext = os.path.splitext(input_p)[1].lower().replace('.', '')
        output_ext = self.output_format.get().lower()

        if not input_ext:
            self.log_message("提示：请先选择一个输入文件。")
            return

        if input_ext == output_ext:
            self.log_message(f"提示：输出格式与输入格式相同 ({output_ext})，无需转换。")
            return

        loss_info = convert_loss.get((input_ext, output_ext), "无特定转换损失信息。")
        self.log_message(f"从 {input_ext} 转换为 {output_ext}：\n{loss_info}")

    def convert(self):
        input_p = self.input_path.get()
        output_p = self.output_path.get()
        output_f = self.output_format.get()
        output_n = self.output_filename.get()

        if not all([input_p, output_p, output_f, output_n]):
            messagebox.showerror("错误", "所有字段都必须填写！")
            return

        self.log_message(f"正在转换 {os.path.basename(input_p)} 为 {output_f}...")
        self.update_idletasks()

        result = convert_image(input_p, output_p, output_f, output_n)
        self.log_message(result)
        if "成功" in result:
            messagebox.showinfo("成功", result)
        else:
            messagebox.showerror("转换失败", result)

    def log_message(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete("1.0", tk.END)
        self.log_text.insert(tk.END, f"[{self.get_timestamp()}] {message}\n\n")
        self.log_text.config(state=tk.DISABLED)
        self.log_text.see(tk.END)

    def get_timestamp(self):
        return datetime.now().strftime("%H:%M:%S")

    def _on_close(self):
        self._save_settings()
        self.destroy()

if __name__ == '__main__':
    app = ImageConverterApp()
    app.mainloop()
