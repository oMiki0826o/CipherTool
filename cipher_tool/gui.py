"""Provide the Tkinter desktop interface for CipherTool."""

import tkinter as tk
from tkinter import messagebox, ttk

from .registry import TOOLS, generate_parameters, run_tool

PARAMETER_LABELS = {
    "shift": "位移量",
    "a": "乘數 a",
    "b": "位移 b",
    "key": "密鑰",
    "keyword": "關鍵字",
    "substitution_alphabet": "替換字母表",
    "rails": "欄位數",
    "columns": "欄位數",
    "pairs": "字母配對表",
    "matrix": "2×2 矩陣",
    "position": "內圈位置",
    "from_base": "來源進位",
    "to_base": "目標進位",
}


def tool_id_from_name(name: str) -> str:
    """Resolve a GUI display name to its registered tool identifier."""
    for tool_id, tool in TOOLS.items():
        if tool["name"] == name:
            return tool_id
    raise ValueError("找不到指定工具。")


class CipherToolApp(ttk.Frame):
    """Render and coordinate CipherTool's single-window interface."""

    def __init__(self, root: tk.Tk) -> None:
        """Create the interface and load the initial tool selection."""
        super().__init__(root, padding=16)
        self.root = root
        self.category_value = tk.StringVar()
        self.tool_value = tk.StringVar()
        self.mode_value = tk.StringVar()
        self.parameter_values: dict[str, tk.StringVar] = {}
        self._build_widgets()
        self._select_initial_tool()

    def _build_widgets(self) -> None:
        """Build fixed controls; dynamic parameters are added on selection."""
        self.grid(sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="類型").grid(row=0, column=0, sticky="w", pady=4)
        self.category_box = ttk.Combobox(self, textvariable=self.category_value, state="readonly")
        self.category_box["values"] = tuple(dict.fromkeys(tool["category"] for tool in TOOLS.values()))
        self.category_box.grid(row=0, column=1, sticky="ew", pady=4)
        self.category_box.bind("<<ComboboxSelected>>", lambda event: self._refresh_tools())

        ttk.Label(self, text="方法").grid(row=1, column=0, sticky="w", pady=4)
        self.tool_box = ttk.Combobox(self, textvariable=self.tool_value, state="readonly")
        self.tool_box.grid(row=1, column=1, sticky="ew", pady=4)
        self.tool_box.bind("<<ComboboxSelected>>", lambda event: self._refresh_tool_details())

        ttk.Label(self, text="模式").grid(row=2, column=0, sticky="w", pady=4)
        self.mode_box = ttk.Combobox(self, textvariable=self.mode_value, state="readonly")
        self.mode_box.grid(row=2, column=1, sticky="ew", pady=4)

        self.parameter_frame = ttk.Frame(self)
        self.parameter_frame.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.parameter_frame.columnconfigure(1, weight=1)

        ttk.Label(self, text="輸入").grid(row=4, column=0, columnspan=2, sticky="w", pady=(12, 4))
        self.input_box = tk.Text(self, height=8, wrap="word")
        self.input_box.grid(row=5, column=0, columnspan=2, sticky="nsew")

        buttons = ttk.Frame(self)
        buttons.grid(row=6, column=0, columnspan=2, sticky="ew", pady=8)
        ttk.Button(buttons, text="執行", command=self._run).pack(side="left")
        self.random_button = ttk.Button(buttons, text="隨機產生", command=self._randomize)
        self.random_button.pack(side="left", padx=6)
        ttk.Button(buttons, text="複製結果", command=self._copy_output).pack(side="left", padx=6)
        ttk.Button(buttons, text="清除", command=self._clear).pack(side="left")

        ttk.Label(self, text="輸出").grid(row=7, column=0, columnspan=2, sticky="w", pady=(4, 4))
        self.output_box = tk.Text(self, height=8, wrap="word", state="disabled")
        self.output_box.grid(row=8, column=0, columnspan=2, sticky="nsew")
        self.rowconfigure(5, weight=1)
        self.rowconfigure(8, weight=1)

    def _select_initial_tool(self) -> None:
        """Select the first registered category and tool."""
        self.category_value.set(self.category_box["values"][0])
        self._refresh_tools()

    def _refresh_tools(self) -> None:
        """Show only the methods in the selected category."""
        choices = [tool["name"] for tool in TOOLS.values() if tool["category"] == self.category_value.get()]
        self.tool_box["values"] = choices
        self.tool_value.set(choices[0])
        self._refresh_tool_details()

    def _refresh_tool_details(self) -> None:
        """Update modes and parameter entries for the selected tool."""
        tool = TOOLS[tool_id_from_name(self.tool_value.get())]
        self.mode_box["values"] = tool["modes"]
        self.mode_value.set(tool["modes"][0])
        for widget in self.parameter_frame.winfo_children():
            widget.destroy()
        self.parameter_values = {}
        defaults = {"shift": "3", "a": "5", "b": "8", "rails": "3", "columns": "4", "pairs": "AM,BX,CQ,DW,ET,FR,GS,HL,IO,JP,KN,UV,YZ", "matrix": "3,3,2,5", "position": "3", "from_base": "10", "to_base": "16"}
        for row, name in enumerate(tool["parameters"]):
            ttk.Label(self.parameter_frame, text=PARAMETER_LABELS.get(name, name)).grid(row=row, column=0, sticky="w", pady=4)
            value = tk.StringVar(value=defaults.get(name, ""))
            ttk.Entry(self.parameter_frame, textvariable=value).grid(row=row, column=1, sticky="ew", pady=4)
            self.parameter_values[name] = value
        if tool_id_from_name(self.tool_value.get()) in {"caesar", "affine", "vigenere", "substitution", "playfair"}:
            self.random_button.state(["!disabled"])
        else:
            self.random_button.state(["disabled"])

    def _run(self) -> None:
        """Run the selected operation and show any validation error."""
        parameters = {name: value.get() for name, value in self.parameter_values.items()}
        try:
            result = run_tool(tool_id_from_name(self.tool_value.get()), self.mode_value.get(), self.input_box.get("1.0", "end-1c"), parameters)
        except ValueError as error:
            messagebox.showerror("輸入錯誤", str(error), parent=self.root)
            return
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", result)
        self.output_box.configure(state="disabled")

    def _copy_output(self) -> None:
        """Copy the current output to the system clipboard."""
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output_box.get("1.0", "end-1c"))

    def _randomize(self) -> None:
        """Fill the current form with generated key or parameter values."""
        for name, value in generate_parameters(tool_id_from_name(self.tool_value.get())).items():
            self.parameter_values[name].set(value)

    def _clear(self) -> None:
        """Clear both text areas while retaining the current tool settings."""
        self.input_box.delete("1.0", "end")
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.configure(state="disabled")


def launch() -> None:
    """Create the main window and start Tkinter's event loop."""
    root = tk.Tk()
    root.title("CipherTool")
    root.minsize(620, 520)
    CipherToolApp(root)
    root.mainloop()
