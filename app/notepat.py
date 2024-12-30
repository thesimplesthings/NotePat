import os
import tkinter as tk
from tkinter import PhotoImage, filedialog, messagebox

from app.formatters import get_formatter


class NotePat:
    FILE_TYPES = [("Text files", "*.txt"), ("All files", "*.*")]
    FONT_SIZES = [10, 12, 16, 20, 24, 30]

    def __init__(self, root: tk.Tk):
        self.root = root
        self.formatter = get_formatter()
        self._setup_window()
        self._setup_logo()
        self._setup_menu()
        self._setup_text_area()
        self._setup_bindings()

    def _setup_window(self):
        self.root.title("Notepat 0.1")
        self.root.iconbitmap("notepat.ico")
        self.font_size = 10
        self.current_file = None

    def _setup_logo(self):
        self.logo = PhotoImage(file="app/assets/images/notepat.png")
        self.logo_label = tk.Label(self.root, image=self.logo, bg="white")
        self.logo_label.place(x=5, y=5)

    def _setup_menu(self):
        self.menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        tools_menu.add_command(label="Pat the selection!", command=self.format_text, accelerator="Ctrl+Shift+F")
        self.menu_bar.add_cascade(label="Tools", menu=tools_menu)

        font_menu = tk.Menu(self.menu_bar, tearoff=0)
        for size in self.FONT_SIZES:
            font_menu.add_command(label=f"{size} pt", command=lambda s=size: self.change_font_size(s))
        self.menu_bar.add_cascade(label="Font Size", menu=font_menu)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="Overview", command=self.show_help)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=self.menu_bar)

    def _setup_text_area(self):
        text_frame = tk.Frame(self.root)
        text_frame.pack(expand=True, fill=tk.BOTH)

        self.text_area = tk.Text(text_frame, wrap=tk.WORD, undo=True)
        self.text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def _setup_bindings(self):
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda event: self.save_as_file())
        self.root.bind("<Control-a>", lambda event: self.select_all())
        self.root.bind("<Control-Shift-F>", lambda event: self.format_text())

    def show_help(self):
        # Create a new window
        help_window = tk.Toplevel(self.root)
        help_window.title("Help - Overview")
        help_window.geometry("400x200")
        help_text = """
        https://github.com/thesimplesthings/NotePat
        MIT License
        Ctrl+Shift+F to perform action on selected text.
        Original creator - Miguel Campillos - miguelcampillos.com
        """
        # Create a label for displaying the help text
        label = tk.Label(help_window, text=help_text, justify="left", anchor="nw")
        label.pack(fill="both", padx=10, pady=10)

    def change_font_size(self, size: int):
        self.font_size = size
        self.text_area.config(font=("TkDefaultFont", self.font_size))

        # Recalculate the scroll region to ensure the scrollbar works properly
        self.text_area.update_idletasks()  # Refresh the canvas layout
        # self.text_area.configure(scrollregion=self.text_area.bbox("all"))

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=self.FILE_TYPES)
        if not file_path:
            return

        try:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

            self.current_file = file_path
            self.root.title(f"Notepat 0.1 - {os.path.basename(file_path)}")  # Update window title
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {e}")

    def save_file(self):
        """Save the current content to the current file or prompt for a file name if no file is open."""
        if self.current_file:
            # Save to the currently open file
            try:
                with open(self.current_file, "w") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content.strip())
                messagebox.showinfo("Saved", f"File saved: {self.current_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot save file: {e}")
        else:
            # No file currently open, prompt for "Save As"
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=self.FILE_TYPES)
        if not file_path:
            return

        try:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content.strip())
            # Update the current file path
            self.current_file = file_path
            self.root.title(f"Notepat 0.1 - {os.path.basename(file_path)}")  # Update window title
            messagebox.showinfo("Saved", f"File saved: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot save file: {e}")

    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return "break"

    def copy_text(self):
        try:
            self.root.clipboard_clear()
            text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.root.clipboard_append(text)
        except tk.TclError:
            pass

    def paste_text(self):
        try:
            text = self.root.clipboard_get()
            self.text_area.insert(tk.INSERT, text)
        except tk.TclError:
            pass

    def format_text(self):
        selected_text = self._get_selected_text()
        if not selected_text:
            messagebox.showinfo("No Selection", "Please select text to format.")
            return

        try:
            original_text = selected_text
            formatted_text = self.formatter.format_text(selected_text)
            if not formatted_text:
                return

            start, end = self._get_selected_range()
            self._display_provisional_text(start, end, formatted_text)

            should_apply_changes = messagebox.askyesno("Apply Changes?", "Do you want to apply the suggested changes?")
            if should_apply_changes:
                self._keep_the_changes(start, end)
            else:
                self._restore_original_text(start, end, original_text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def _get_selected_text(self) -> str | None:
        try:
            return self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            return None

    def _get_selected_range(self) -> tuple[str, str]:
        return self.text_area.index(tk.SEL_FIRST), self.text_area.index(tk.SEL_LAST)

    def _display_provisional_text(self, start: str, end: str, text: str):
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.text_area.insert(start, text)
        self.text_area.tag_add("italic", start, end)
        self.text_area.tag_configure("italic", font=("TkDefaultFont", self.font_size, "italic"))
        self.root.update()

    def _keep_the_changes(self, start: str, end: str):
        self.text_area.tag_remove("italic", start, end)

    def _restore_original_text(self, start: str, end: str, text: str):
        self.text_area.delete(start, end)
        self.text_area.insert(start, text)

    def run(self):
        self.root.mainloop()
