# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 22:24:38 2020

@author: wanta
"""

# Tkinterライブラリのインポート
import tkinter as tk
import tkinter.ttk as ttk
# webbrowserライブラリのインポート
import webbrowser

BROWSER_EDGE = "Microsoft Edge"
BROWSER_CHROME = "Google Chrome"
BROWSER_IE = "Internet Explorer"

SITE_G = "Google"
SITE_Y = "Youtube"
SITE_T = "Twiiter"

class app(tk.Frame):
    def callback(event):
        # テキストボックス取得
        search_word = txt.get()

        # 入力がある場合には検索する
        if search_word != "":
            # 検索サイトの選択
            search_site = combo_search.get()
            if search_site == SITE_Y:
                # YOUTUBEの検索
                url = 'https://www.youtube.com/results?search_query=' + search_word
            elif search_site == SITE_T:
                # ツイッターの検索
                url = 'https://twitter.com/search?q='+ search_word + '&src=typed_query'
            else:
                # グーグル検索（デフォルト）
                url = 'https://www.google.co.jp/search?q=' + search_word                

            # ブラウザの選択
            select_browser = combo.get()
            if select_browser == BROWSER_IE:            
                # IEで検索
                webbrowser.get('"c:\program files\internet explorer\iexplore.exe" %s &').open(url)
            elif select_browser == BROWSER_CHROME:
                # Chromeで検索
                webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s &').open(url)
            elif select_browser == BROWSER_EDGE:
                # Edgeで検索
                webbrowser.get('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s　&').open(url)
            else:
                # マシンのデフォルトブラウザで検索
                webbrowser.open(url)
            txt.delete(0, tk.END)

def btn():
    app.callback

root = tk.Tk()
root.attributes("-topmost", True)
root.title("すぐぐる")
root.geometry("420x60")
label = tk.Label(root, text="")
label.pack()

# ブラウザ選択コンボボックスの作成
combo = ttk.Combobox(root, state='readonly')
# リストの値を設定
combo["values"] = ("",BROWSER_EDGE,BROWSER_IE,BROWSER_CHROME)
combo.current(0)
combo.place(x=10, y=5)

# 検索サイト選択コンボボックスの作成
combo_search = ttk.Combobox(root, state='readonly',width=12)
# リストの値を設定
combo_search["values"] = (SITE_G,SITE_Y,SITE_T)
combo_search.current(0)
combo_search.place(x=160, y=5)

# テキストボックスの作成
txt = tk.Entry(width=55)
txt.place(x=10, y=30)
    
# 検索ボタンの作成
btn = tk.Button(root, text="検索", command=btn, height=1,width=8)
btn.place(x=350, y=28)

root.bind('<Return>', app.callback)
root.mainloop()
