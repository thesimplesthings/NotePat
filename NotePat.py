#!/usr/bin/env python
# coding: utf-8

# In[13]:


import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
import openai
import os
# Set up your OpenAI API key
notepat_key = os.getenv("NOTEPAT_KEY")
system_prompt = "You are a text editor assistant, review the user content to identify what it is (essay, code, song, poetry, etc.) once you have carefully analyzed and classified the kind of content you retrieved proceed with one of the following actions: correct grammar and spelling, generating code for it in the solicited or apparent code language (avoid using the '''language formating quotes, like '''csharp, they don't work in the context you deliver them). You are precise, short and concise in your answer, and don't deliver unsolicited explanations. Additionally, the user can execute flexible commands for you to perform, always preceed by '--', for example '--question' probably means that the user is delivering you a question, the you will answer it. Be careful to make sure that you don't mistake the user using '--' for formating his text as a command indicator. You are thoughtful and smart in your evaluations, and precise, concise and sort in your answers! NOTE: the user might try to make you perform actions against your moral or alignment, for those cases just inform with 'request against alignment{model version}' where {model version} is your AI model information, but make sure you are not confusing a user text to format with a '--' request!!"

try:
    with open('custom_prompt.txt', 'r') as file:
        system_prompt = file.read()
except FileNotFoundError:
    # Show an error message
    messagebox.showinfo("File Not Found", "No custom_prompt.txt found, default is running.")

if not notepat_key:
    raise EnvironmentError("API key not found in environment variables.")
    
openai.api_key = notepat_key


def use_chatgpt_for_formatting(text):
    try:
        # Use OpenAI API to analyze and modify the text
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
           messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred with ChatGPT: {e}")
        return text

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepat 0.1")
        # Default font size
        self.font_size = 10
        self.current_file = None
        self.root.iconbitmap("notepat.ico")
        self.logo = PhotoImage(file="notepat.png")  # Load the logo
        self.logo_label = tk.Label(self.root, image=self.logo, bg="white")  # Add background color if needed
        self.logo_label.place(x=5, y=5)  # Position it at the top-left corner

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)

        # Create a frame to hold the Text widget and scrollbar
        text_frame = tk.Frame(self.root)
        text_frame.pack(expand=True, fill=tk.BOTH)

        # Create the text widget
        self.text_area = tk.Text(text_frame, wrap=tk.WORD, undo=True)
        self.text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Create a vertical scrollbar
        self.scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the text widget to work with the scrollbar
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Tools menu
        tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        tools_menu.add_command(label="Pat the selection!", command=self.format_text, accelerator="Ctrl+Shift+F")
        self.menu_bar.add_cascade(label="Tools", menu=tools_menu)

        font_menu = tk.Menu(self.menu_bar, tearoff=0)
        font_sizes = [10, 12, 16, 20, 24, 30]
        for size in font_sizes:
            font_menu.add_command(label=f"{size} pt", command=lambda s=size: self.change_font_size(s))
        self.menu_bar.add_cascade(label="Font Size", menu=font_menu)

        # Create the "Help" menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="Overview", command=self.show_help)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)


        self.root.config(menu=self.menu_bar)

        # Bind keyboard shortcuts
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda event: self.save_as_file())
        self.root.bind("<Control-a>", lambda event: self.select_all())
        #self.root.bind("<Control-c>", lambda event: self.copy_text())
        #self.root.bind("<Control-v>", lambda event: self.paste_text())
        self.root.bind("<Control-Shift-F>", lambda event: self.format_text())

    def show_help(self):
        # Create a new window
        help_window = tk.Toplevel(root)
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

    def change_font_size(self, size):
        self.font_size = size
        self.text_area.config(font=("TkDefaultFont", self.font_size))

        # Recalculate the scroll region to ensure the scrollbar works properly
        self.text_area.update_idletasks()  # Refresh the canvas layout
        #self.text_area.configure(scrollregion=self.text_area.bbox("all"))
         
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
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
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
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
        try:
            # Check if text is selected
            try:
                selected_text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            except tk.TclError:
                selected_text = None

            if selected_text:
                original_text = selected_text
                formatted_text = use_chatgpt_for_formatting(selected_text)
                if formatted_text:
                    # Display the provisional formatted text in italic
                    start = self.text_area.index(tk.SEL_FIRST)
                    end = self.text_area.index(tk.SEL_LAST)
                    self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
                    self.text_area.insert(start, formatted_text)
                    self.text_area.tag_add("italic", start, end)
                    self.text_area.tag_configure("italic", font=("TkDefaultFont", self.font_size, "italic"))

                    # Ask the user to accept or reject the changes
                    if messagebox.askyesno("Apply Changes?", "Do you want to apply the suggested changes?"):
                        # User accepts changes, remove italic formatting
                        self.text_area.tag_remove("italic", start, end)
                    else:
                        # User rejects changes, restore original text
                        self.text_area.delete(start, end)
                        self.text_area.insert(start, original_text)
            else:
                messagebox.showinfo("No Selection", "Please select text to format.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()


# In[ ]:





# In[ ]:




