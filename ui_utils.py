# ui_utils.py
import tkinter as tk
from config import COLORS, FONTS

def add_hover(btn, normal_bg, hover_bg):
    btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg))
    btn.bind("<Leave>", lambda e: btn.config(bg=normal_bg))

def make_btn(parent, text, cmd, bg=None, fg=None, hbg=None, font=FONTS["normal"], padx=10, pady=5, side=tk.LEFT, px=3, py=5):
    bg  = bg  or COLORS["btn"]
    fg  = fg  or COLORS["text"]
    hbg = hbg or COLORS["btn_hover"]
    
    b = tk.Button(parent, text=text, command=cmd, bg=bg, fg=fg, font=font,
                  relief="flat", cursor="hand2", padx=padx, pady=pady,
                  activebackground=hbg, activeforeground=fg, bd=0, highlightthickness=0)
    b.pack(side=side, padx=px, pady=py)
    add_hover(b, bg, hbg)
    return b

def sep(parent, bg_color):
    tk.Frame(parent, width=1, bg=bg_color).pack(side=tk.LEFT, fill=tk.Y, padx=6, pady=6)