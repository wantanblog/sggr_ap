# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 22:26:31 2020

@author: wanta
"""
# Tkinterライブラリのインポート
import tkinter as tk
# webbrowserライブラリのインポート
import webbrowser

class app(tk.Frame):
    def callback(event):
        # テキストボックス取得
        search_word = txt.get()
        if search_word != "":
            url = 'https://www.google.co.jp/search?q=' + search_word
            webbrowser.open(url)
            txt.delete(0, tk.END)

root = tk.Tk()
# 常に最前表示
root.attributes("-topmost", True)
root.title("すぐぐる")
root.geometry("420x40")
label = tk.Label(root, text="")
label.pack()
# テキストボックス
txt = tk.Entry(width=65)
txt.place(x=10, y=10)
# エンターで検索処理
root.bind('<Return>', app.callback)
root.mainloop()
