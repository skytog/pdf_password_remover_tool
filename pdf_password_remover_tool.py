import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pikepdf

def unlock_pdf(file_path, password):
    try:
        with pikepdf.open(file_path, password=password) as pdf:
            base_name, ext = os.path.splitext(file_path)
            new_file_path = f"{base_name}_unlocked{ext}"
            pdf.save(new_file_path)
        return True, "PDFのパスワードを解除しました"
    except pikepdf._qpdf.PasswordError:
        return False, "パスワードが間違っています"
    except Exception as e:
        return False, str(e)
        
def select_and_unlock_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return

    password = tk.simpledialog.askstring("パスワード入力", "PDFのパスワードを入力してください")
    if not password:
        return

    success, message = unlock_pdf(file_path, password)
    if success:
        messagebox.showinfo("完了", message)
    else:
        messagebox.showerror("エラー", message)

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("PDF Password Remover Tool")
root.geometry("400x300")

# タイトルラベル
title_label = tk.Label(root, text="PDF Password Remover Tool", font=("Arial", 22))
title_label.pack(pady=20)

# 説明ラベル
description_label = tk.Label(root, text="パスワード付きPDFを選択し、パスワードを入力してください")
description_label.pack(pady=10)

# 解除ボタン
unlock_button = tk.Button(root, text="PDFを選択", font=("Arial", 16), command=select_and_unlock_pdf)
unlock_button.pack(pady=20)

# 終了ボタン
exit_button = tk.Button(root, text="終了", font=("Arial", 16), command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
