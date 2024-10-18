import os
import tkinter as tk
from tkinter import filedialog, messagebox
from treelib import Tree

def generate_project_map(directory, output_file):
    tree = Tree()
    tree.create_node(os.path.basename(directory), directory)

    for root, dirs, files in os.walk(directory):
        parent = root
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            tree.create_node(dir_name, dir_path, parent=parent)
        
        for file_name in files:
            file_path = os.path.join(root, file_name)
            tree.create_node(file_name, file_path, parent=parent)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(tree.show(line_type='ascii-em', stdout=False))

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def export_project_map():
    directory = directory_entry.get()
    if not directory:
        messagebox.showerror("خطأ", "الرجاء اختيار مجلد.")
        return
    
    output_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("ملفات نصية", "*.txt")])
    if output_file:
        try:
            generate_project_map(directory, output_file)
            messagebox.showinfo("نجاح", f"تم تصدير خريطة المشروع إلى {output_file}")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ: {str(e)}")

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("مولد خريطة المشروع")

# إنشاء وترتيب العناصر
tk.Label(root, text=":اختر مجلد المشروع", font=("Arial", 12)).pack(pady=5)
directory_entry = tk.Entry(root, width=50, font=("Arial", 10))
directory_entry.pack(side=tk.LEFT, padx=5)
tk.Button(root, text="استعراض", command=select_directory, font=("Arial", 10)).pack(side=tk.LEFT)
tk.Button(root, text="تصدير خريطة المشروع", command=export_project_map, font=("Arial", 12)).pack(pady=10)

# بدء حلقة أحداث واجهة المستخدم الرسومية
root.mainloop()