import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

# 각 필터에 따른 처리
def apply_filter(img, filter_type):
    if filter_type == '3x3 mean':
        return cv2.blur(img, (3, 3))
    elif filter_type == '5x5 mean':
        return cv2.blur(img, (5, 5))
    elif filter_type == '3x3 median':
        return cv2.medianBlur(img, 3)
    elif filter_type == '5x5 median':
        return cv2.medianBlur(img, 5)
    elif filter_type == '3x3 laplacian':
        return cv2.Laplacian(img, -1)
    return img

# 필터링된 이미지 디스플레이
def display_image(image, title):
    new_window = tk.Toplevel()
    new_window.title(title)
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(new_window, image=photo)
    label.image = photo  # keep a reference!
    label.pack()

# gui 드롭다운
def on_filter_select(event):
    selected_filter = filter_var.get()
    processed_image = apply_filter(gray_image, selected_filter)
    display_image(processed_image, selected_filter)

# 이미지 로드
original_image = cv2.cvtColor(cv2.imread('./assets/example.png'), cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# 메인화 면
window = tk.Tk()
window.title("공간 필터링")

# 원본 이미지 디스플레이
original_photo = ImageTk.PhotoImage(image=Image.fromarray(original_image))
original_label = tk.Label(window, image=original_photo)
original_label.image = original_photo
original_label.pack()

# 드롭다운 구
filter_var = tk.StringVar(window)
filters = ['3x3 mean', '5x5 mean', '3x3 median', '5x5 median', '3x3 laplacian']
filter_dropdown = ttk.Combobox(window, textvariable=filter_var, values=filters)
filter_dropdown.pack()
filter_dropdown.bind('<<ComboboxSelected>>', on_filter_select)

window.mainloop()
