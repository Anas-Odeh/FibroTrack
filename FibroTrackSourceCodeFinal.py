# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:39:04 2025

@author: AnasO
"""


import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    try:
        import pyi_splash
        pyi_splash.update_text("Initializing FibroTrack...")
    except ImportError:
        pass  

import itertools
import threading
from colorama import Fore, Style, init,Back
import time
from tqdm import tqdm
from PIL import Image, ImageTk

# Your initial application setup here
print("\nInitializing the application...\n\nplease wait...", flush=True)

init(autoreset=True)

def print_welcome_message():
    welcome_message = r"""
                           Welcome To  
 _____                                                  _____ 
( ___ )                                                ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  _____ _ _             _____               _     |   | 
 |   | |  ___(_) |__  _ __ __|_   _| __ __ _  ___| | __ |   | 
 |   | | |_  | | '_ \| '__/ _ \| || '__/ _` |/ __| |/ / |   | 
 |   | |  _| | | |_) | | | (_) | || | | (_| | (__|   <  |   | 
 |   | |_|   |_|_.__/|_|  \___/|_||_|  \__,_|\___|_|\_\ |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                (_____)
 
"""
    print("\n" * 3, flush=True) 
    print(Fore.GREEN + Style.BRIGHT + welcome_message, flush=True)
    time.sleep(1)  

print_welcome_message()

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    try:
        pyi_splash.close()
    except ImportError:
        pass


init(autoreset=True)

class CircularProgress:
    def __init__(self, message="Loading", total_steps=100, delay=0.1):
        self.message = message
        self.total_steps = total_steps
        self.current_step = 0
        self.delay = delay
        self.busy = False
        self.spinner = itertools.cycle(['◜', '◠', '◝', '◞', '◡', '◟'])

    def spinner_task(self):
        while self.busy:
            progress = int(100 * self.current_step / self.total_steps)
            sys.stdout.write(f'\r{self.message} {next(self.spinner)} {progress}%')
            sys.stdout.flush()
            if self.current_step < self.total_steps:
                self.current_step += 1
            time.sleep(self.delay)
            if progress >= 100:
                self.busy = False
        sys.stdout.write('\r' + ' ' * (len(self.message) + 7) + '\r')  # Clean up

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)


with CircularProgress("Importing libraries", total_steps=100):

    import os
    import queue
    import numpy as np
    from datetime import datetime, timedelta
    from ultralytics import YOLO
    import cv2
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    import easygui
    import pandas as pd
    import tkinter.font as tkFont
    from skimage.morphology import remove_small_objects
    import csv
    from tkinter import filedialog, messagebox, ttk
    from tkinter import Tk, Canvas, Button, PhotoImage, messagebox, Label, Frame, SUNKEN
    from skimage.measure import regionprops_table
    from skimage.transform import resize
    import numpy as np
    from PIL import Image
    import os
    import time
    from tkinter import messagebox
    import ctypes 
    
    # Enable DPI awareness for high-resolution displays (Windows-specific)
    try:
        
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Enables per-monitor DPI awareness
        
    except Exception:
        
        pass  # If not on Windows or DPI awareness is already set, ignore

print("Imports completed.\n\nPlease wait, you're almost there...\n\nLaunching the FibroTrack application...\n\n", flush=True)


def find_fibrotrack_icons_folder():
    home_dir = os.path.expanduser("~")
    for root_dir, dirs, files in os.walk(home_dir):
        if "FibroTrack - Software Icons" in dirs:
            return os.path.join(root_dir, "FibroTrack - Software Icons")
    raise FileNotFoundError("FibroTrack - Software Icons folder not found.")


try:
    fibrotrack_icons_folder = find_fibrotrack_icons_folder()
except FileNotFoundError as e:
    print(e,flush=True)
    messagebox.showerror("Error", "The FibroTrack - Software Icons folder could not be found.")
    exit()


tab1_path = os.path.join(fibrotrack_icons_folder, "Odeh et al. Define Pixel.jpg")
tab2_path = os.path.join(fibrotrack_icons_folder, "Odeh et al. Muscle Segmentation.jpg")
tab3_path = os.path.join(fibrotrack_icons_folder, "Odeh et al. Analyze Fibrosis.jpg")


assert os.path.exists(tab1_path), f"File not found: {tab1_path}"
assert os.path.exists(tab2_path), f"File not found: {tab2_path}"
assert os.path.exists(tab3_path), f"File not found: {tab3_path}"

w = Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)
w.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
w.overrideredirect(1)  


background_image = ImageTk.PhotoImage(Image.open('Splash Screen.jpg'))

background_label = Label(w, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = Label(w, text='Welcome To FibroTrack!', fg='white', bg='#364FD0')
label1.configure(font=("Arial", 16, "bold"), bg='#364FD0')
label1.place(x=20, y=60)

label2 = Label(w, text='Loading...', fg='white', bg='#364FD0')
label2.configure(font=("Arial", 14))
label2.place(x=160, y=180)

# Animation Setup
image_a = ImageTk.PhotoImage(Image.open('Group 2.png'))
image_b = ImageTk.PhotoImage(Image.open('Group 1.png'))


spacing = 30  


for i in tqdm(range(10), desc="Loading", ncols=100):  
    labels = [
        Label(w, image=image_a if j == i % 4 else image_b, border=0, relief=SUNKEN).place(x=160 + spacing * j, y=140)
        for j in range(4)
    ]
    w.update_idletasks()
    time.sleep(0.07)


time.sleep(1)

w.destroy()


original_images = {
    "tab1": Image.open(tab1_path),
    "tab2": Image.open(tab2_path),
    "tab3": Image.open(tab3_path)
}

def resize_image(image, width, height):
    image_copy = image.copy()
    image_copy.thumbnail((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image_copy)


def adjust_icon_sizes():
    tab_image_width = root.winfo_width() // 10
    tab_image_height = root.winfo_height() // 10

    if tab_image_width != adjust_icon_sizes.last_width or tab_image_height != adjust_icon_sizes.last_height:
        adjust_icon_sizes.last_width = tab_image_width
        adjust_icon_sizes.last_height = tab_image_height

        global tab1_img, tab2_img, tab3_img
        tab1_img = resize_image(original_images["tab1"], tab_image_width, tab_image_height)
        tab2_img = resize_image(original_images["tab2"], tab_image_width, tab_image_height)
        tab3_img = resize_image(original_images["tab3"], tab_image_width, tab_image_height)

        tab1_button.config(image=tab1_img)
        tab2_button.config(image=tab2_img)
        tab3_button.config(image=tab3_img)

adjust_icon_sizes.last_width = 0
adjust_icon_sizes.last_height = 0


def show_help():
    help_text = (
        "This application allows you to follow these steps:\n\n"
        "1. Define Your Pixels: Select a range of pixels that represent different staining intensities in Masson's trichrome and/or Sirius red stains.\n\n"
        "2. Segment Muscles: Access fully automated tools to perform muscle segmentation.\n\n"
        "3. Analyze Fibrosis: Analyze fibrosis patterns.\n\n"
    )
    messagebox.showinfo("Help", help_text)

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.id = None
        self.x = self.y = 0

    def show_tip(self):
        self.x, self.y, _, _ = self.widget.bbox("insert")
        self.x += self.widget.winfo_rootx() + 25
        self.y += self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (self.x, self.y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                        background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                        font=("tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

    def attach(self):
        self.widget.bind("<Enter>", lambda e: self.show_tip())
        self.widget.bind("<Leave>", lambda e: self.hide_tip())


root = tk.Tk()
root.title("© FibroTrack App - Muscle Segmentation & Fibrosis Analysis")


root.state('zoomed')
root.configure(bg='#1c2833')  

# Help Button
help_button = tk.Button(root, text="Help?", command=show_help, font=("Helvetica", 14, "bold"),
                        bg='#5dade2', fg='#ffffff', relief='flat', bd=0, padx=10, pady=5)
help_button.pack(side="top", pady=10)

def on_enter(e):
    help_button['bg'] = '#2980b9'

def on_leave(e):
    help_button['bg'] = '#5dade2'

help_button.bind("<Enter>", on_enter)
help_button.bind("<Leave>", on_leave)

ToolTip(help_button, "Click here for help with the application").attach()

# Tab Frame
tab_frame = tk.Frame(root, bg='#1c2833')
tab_frame.pack(side="left", fill="y", padx=5, pady=5)

# Switch tab functionality
def switch_tab(tab_name):
    for tab in content_frame.winfo_children():
        tab.pack_forget()
    for btn in tab_buttons.values():
        btn.config(font=("Helvetica", 12, "bold"), bg='#34495e')  
    tabs[tab_name].pack(expand=1, fill="both")
    tab_buttons[tab_name].config(font=("Helvetica", 12, "bold"), bg='#5dade2')  

# Tab Buttons
tab_buttons = {}
tab1_button = tk.Button(tab_frame, text="Step 1:\nDefine Your Pixels", command=lambda: switch_tab("tab1"),
                        font=("Helvetica", 12, "bold"), compound='top', bg='#34495e', fg='#ecf0f1', bd=0)
tab1_button.pack(fill="x", pady=5, padx=5, expand=True)
tab_buttons["tab1"] = tab1_button

ToolTip(tab1_button, "Go to Step 1: Define Your Pixels").attach()


tab2_button = tk.Button(tab_frame, text="Step 2:\nSegment Muscles", command=lambda: switch_tab("tab2"),
                        font=("Helvetica", 12, "bold"), compound='top', bg='#34495e', fg='#ecf0f1', bd=0)
tab2_button.pack(fill="x", pady=5, padx=5, expand=True)
tab_buttons["tab2"] = tab2_button

ToolTip(tab2_button, "Go to Step 2: Segment Muscles").attach()


tab3_button = tk.Button(tab_frame, text="Step 3:\nAnalyze Fibrosis", command=lambda: switch_tab("tab3"),
                        font=("Helvetica", 12, "bold"), compound='top', bg='#34495e', fg='#ecf0f1', bd=0)
tab3_button.pack(fill="x", pady=5, padx=5, expand=True)
tab_buttons["tab3"] = tab3_button

ToolTip(tab3_button, "Go to Step 3: Analyze Fibrosis").attach()


# Content Frame
content_frame = tk.Frame(root, bg='#ecf0f1')
content_frame.pack(side="right", expand=1, fill="both")

# Tab 1 content 
tab1_content = tk.Frame(content_frame, bg='#ecf0f1')

# ---- GLOBALS ----
image_data_display = None  # Global for display in matplotlib
auto_selected_lower = None   # <--- NEW
auto_selected_upper = None   # <--- NEW
auto_selected_staining = None  # <--- NEW

def save_pixel_values():
    global lower_value, upper_value, image_name, image_dir, current_staining_type
    global auto_selected_lower, auto_selected_upper, auto_selected_staining  # <--- NEW
    try:
        lower_value = int(lower_entry.get())
        upper_value = int(upper_entry.get())
        print(f"Lower value: {lower_value}, Upper value: {upper_value}")

        # --- Update globals for use in other tabs ---
        auto_selected_lower = lower_value       # <--- NEW
        auto_selected_upper = upper_value       # <--- NEW
        auto_selected_staining = current_staining_type  # <--- NEW

        data = {
            "Image Name": [image_name],
            "Lower Pixel Value": [lower_value],
            "Upper Pixel Value": [upper_value],
            "Staining Name": [current_staining_type]
        }
        df = pd.DataFrame(data, columns=["Image Name", "Lower Pixel Value", "Upper Pixel Value", "Staining Name"])

        excel_file = os.path.join(image_dir, "Defined_pixel_values.xlsx")

        if os.path.exists(excel_file):
            existing_df = pd.read_excel(excel_file)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_excel(excel_file, index=False)
        else:
            df.to_excel(excel_file, index=False)

        print(f"Data saved to {excel_file}",flush=True)
        messagebox.showinfo("Success", f"Pixel values for {current_staining_type} staining saved successfully!")

    except ValueError:
        print("Please enter valid integer values for lower and upper bounds.",flush=True)
    except Exception as e:
        print(f"An error occurred while saving to Excel: {e}",flush=True)
        messagebox.showerror("Error", f"An error occurred while saving to Excel: {e}")

sirius_red_button = ttk.Button(tab1_content, text="Load Sirius Red Image", command=lambda: load_image('Sirius Red'))
sirius_red_button.pack(pady=10)

# ToolTip setup omitted for brevity

masson_trichrome_button = ttk.Button(tab1_content, text="Load Masson Trichrome Image", command=lambda: load_image('Masson Trichrome'))
masson_trichrome_button.pack(pady=10)

# ToolTip setup omitted for brevity

def on_entry_change(entry_widget):
    global current_staining_type
    if entry_widget.get():
        entry_widget.config(font=("Helvetica", 20, "bold"))
    else:
        entry_widget.config(font=("Helvetica", 20))

    # Update the display (re-draw mask) when entry changes
    if image_data_display is not None and current_staining_type:
        update_image_display(current_staining_type)

lower_label = ttk.Label(tab1_content, text="Lower Pixel Value:")
lower_label.pack(pady=5)

lower_entry = ttk.Entry(tab1_content, font=("Helvetica", 12))
lower_entry.pack(pady=5)
lower_entry.bind("<KeyRelease>", lambda event: on_entry_change(lower_entry))

# ToolTip omitted for brevity

upper_label = ttk.Label(tab1_content, text="Upper Pixel Value:")
upper_label.pack(pady=5)

upper_entry = ttk.Entry(tab1_content, font=("Helvetica", 12))
upper_entry.pack(pady=5)
upper_entry.bind("<KeyRelease>", lambda event: on_entry_change(upper_entry))

# ToolTip omitted for brevity

save_button = ttk.Button(tab1_content, text="Save Pixel Values", command=save_pixel_values)
save_button.pack(pady=10)

# ToolTip omitted for brevity

fig = Figure(figsize=(12, 6))
canvas = FigureCanvasTkAgg(fig, master=tab1_content)
toolbar = NavigationToolbar2Tk(canvas, tab1_content)
toolbar.update()
toolbar.pack(side=tk.TOP, fill=tk.X)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def get_mean_and_std_color(x):
    mean, std = cv2.meanStdDev(x)
    mean = np.around(mean.flatten(), 2)
    std = np.around(std.flatten(), 2)
    return mean, std

def compute_current_mask(image_data, staining_type, lower_value, upper_value):
    lab_image = cv2.cvtColor(image_data, cv2.COLOR_RGB2Lab)
    if staining_type == 'Sirius Red':
        channel = lab_image[:, :, 1]
    elif staining_type == 'Masson Trichrome':
        channel = lab_image[:, :, 2]
    else:
        channel = lab_image[:, :, 0]

    # Exclude background (white pixels)
    background = np.all(image_data > 220, axis=2)  # tune 220 if needed
    tissue_mask = ~background

    value_mask = (channel >= lower_value) & (channel <= upper_value)
    final_mask = value_mask & tissue_mask
    return final_mask.astype(np.uint8)

def load_image(staining_type):
    global image_data, image_data_display, ax_source, loaded_image_path, image_name, image_dir, current_staining_type
    global auto_selected_lower, auto_selected_upper, auto_selected_staining  # Globals for pixel values

    file_path = easygui.fileopenbox(
        title=f"Select an image file for {staining_type}",
        filetypes=["*.jpg", "*.jpeg", "*.png", "*.tif", "*.tiff"]
    )
    if file_path:
        try:
            # Load the image
            image_data = cv2.imread(file_path, cv2.IMREAD_COLOR)  # BGR format
            if image_data is None:
                messagebox.showerror("Error", "Failed to load image.")
                return

            # Store details about the loaded image
            loaded_image_path = file_path
            image_name = os.path.basename(file_path)
            image_dir = os.path.dirname(file_path)
            current_staining_type = staining_type

            # Ask user if they want to normalize images
            do_normalization = messagebox.askyesno(
                "Color Normalization",
                "Do you want to perform color normalization for all images in this folder? (It's highly recommended)"
            )

            if do_normalization:
                # --- Perform normalization ---
                progress_win = tk.Toplevel()
                progress_win.title("Normalizing Images...")
                progress_label = ttk.Label(progress_win, text="Normalizing images, please wait...")
                progress_label.pack(padx=20, pady=(20, 0))
                progress_bar = ttk.Progressbar(progress_win, orient="horizontal", length=400, mode="determinate")
                progress_bar.pack(padx=20, pady=20)
                progress_bar["value"] = 0
                progress_win.update()

                # Get all image filenames in the directory
                image_list = [f for f in os.listdir(image_dir)
                              if os.path.isfile(os.path.join(image_dir, f)) and
                              f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff'))]
                means, stds = [], []

                # Compute mean and std for all images
                for i, img_name in enumerate(image_list):
                    img_path = os.path.join(image_dir, img_name)
                    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
                    if img is not None:
                        mean, std = get_mean_and_std_color(img)
                        means.append(mean)
                        stds.append(std)

                    # Update progress bar
                    progress_bar["value"] = (i + 1) * 100 / len(image_list)
                    progress_label.config(text=f"Computing statistics: {i + 1}/{len(image_list)}")
                    progress_win.update()

                # Compute median mean and std
                means = np.array(means)
                stds = np.array(stds)
                median_mean = np.median(means, axis=0)
                median_std = np.median(stds, axis=0)

                # Find the template image (closest to median mean/std)
                min_dist = float('inf')
                template_img_name = None
                template_mean = None
                template_std = None
                for i, img_name in enumerate(image_list):
                    dist = np.linalg.norm(means[i] - median_mean) + np.linalg.norm(stds[i] - median_std)
                    if dist < min_dist:
                        min_dist = dist
                        template_img_name = img_name
                        template_mean = means[i]
                        template_std = stds[i]

                # Normalize all images
                norm_save_dir = os.path.join(image_dir, "Median_Normalized_Images")
                os.makedirs(norm_save_dir, exist_ok=True)
                normalized_img_for_display = None
                for i, img_name in enumerate(image_list):
                    img_path = os.path.join(image_dir, img_name)
                    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
                    if img is None:
                        continue
                    img_mean, img_std = get_mean_and_std_color(img)
                    if np.any(img_std == 0) or np.any(template_std == 0):
                        continue
                    normalized_img = np.zeros_like(img, dtype=np.uint8)
                    for c in range(img.shape[2]):
                        normalized_img[:, :, c] = np.clip(
                            (img[:, :, c] - img_mean[c]) * (template_std[c] / img_std[c]) + template_mean[c],
                            0, 255
                        ).astype(np.uint8)
                    cv2.imwrite(os.path.join(norm_save_dir, "Color_Normalized_" + img_name), normalized_img)
                    if img_name == image_name:
                        normalized_img_for_display = normalized_img

                    # Update progress bar
                    progress_bar["value"] = (i + 1) * 100 / len(image_list)
                    progress_label.config(text=f"Normalizing images: {i + 1}/{len(image_list)}")
                    progress_win.update()

                # Close progress window
                progress_bar["value"] = 100
                progress_label.config(text="Normalization complete!")
                progress_win.update()
                progress_win.after(700, progress_win.destroy)  # Close after 0.7s

                # Set the normalized image for display
                if normalized_img_for_display is not None:
                    image_data_display = cv2.cvtColor(normalized_img_for_display, cv2.COLOR_BGR2RGB)
                    messagebox.showinfo("Color Normalization", f"Normalization complete. Template used: {template_img_name}")
                else:
                    image_data_display = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
                    messagebox.showinfo("Color Normalization", "Normalization complete but no normalized image found for display.")

            else:
                # No normalization; use the original image
                image_data_display = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)

            # --- Auto-select lower and upper pixel values (dark pixels) ---
            lab_image = cv2.cvtColor(image_data_display, cv2.COLOR_RGB2Lab)

            # Select the channel based on the staining type
            if staining_type == 'Sirius Red':
                channel = lab_image[:, :, 1]  # A channel
            elif staining_type == 'Masson Trichrome':
                channel = lab_image[:, :, 2]  # B channel
            else:
                channel = lab_image[:, :, 0]  # Default to L channel for unknown staining

            # Exclude background (white pixels)
            background = np.all(image_data_display > 230, axis=2)
            tissue_mask = ~background
            tissue_channel = channel[tissue_mask]  # Only consider tissue pixels

            # Refine the thresholding logic
            if staining_type == 'Sirius Red':
                # Sirius Red: Focus on brighter pixel values (collagen in high A channel)
                lower = int(np.percentile(tissue_channel, 70))  # Bottom 30% ignored
                upper = int(np.percentile(tissue_channel, 99))  # Top 1% brightest pixels included

            elif staining_type == 'Masson Trichrome':
                # Masson Trichrome: Include all dark pixel values (collagen in low B channel)
                lower = int(np.percentile(tissue_channel, 0))   # Minimum value (0th percentile)
                upper = int(np.percentile(tissue_channel, 5))   # Darkest 5% included
                upper = min(upper, 150)  # Clamp to avoid including very bright pixels
            else:
                # General case: Use Otsu's method as fallback
                otsu_thresh, _ = cv2.threshold(
                    tissue_channel.astype(np.uint8), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
                )
                lower = int(otsu_thresh)
                upper = int(tissue_channel.max())

            # Populate the auto-selected values into the UI fields
            lower_entry.delete(0, tk.END)
            lower_entry.insert(0, str(lower))
            upper_entry.delete(0, tk.END)
            upper_entry.insert(0, str(upper))

            # Update globals
            auto_selected_lower = lower
            auto_selected_upper = upper
            auto_selected_staining = staining_type

            # Notify user
            messagebox.showinfo(
                "Auto-Selected Pixel Values",
                f"Automatically selected pixel values:\n\nLower: {lower}\nUpper: {upper}\n\nYou can manually adjust these values if needed."
            )

            # Update the displayed image and mask
            update_image_display(staining_type)

        except Exception as e:
            print(f"An error occurred: {e}", flush=True)

def update_image_display(staining_type):
    global image_data_display, fig, ax_source, canvas

    if image_data_display is not None:
        fig.clf()

        # Original image
        ax_source = fig.add_subplot(1, 3, 1)
        ax_source.imshow(image_data_display)
        ax_source.set_title('Source Image')
        ax_source.axis('off')

        # Channel image
        lab_image = cv2.cvtColor(image_data_display, cv2.COLOR_RGB2Lab)
        if staining_type == 'Sirius Red':
            channel = lab_image[:, :, 1]
            channel_title = 'A Channel'
        elif staining_type == 'Masson Trichrome':
            channel = lab_image[:, :, 2]
            channel_title = 'B Channel'
        else:
            raise ValueError("Unsupported staining type")

        ax_chan = fig.add_subplot(1, 3, 2, sharex=ax_source, sharey=ax_source)
        ax_chan.imshow(channel, cmap='viridis')
        ax_chan.set_title(f'{channel_title} ({staining_type})')
        ax_chan.axis('off')

        try:
            lower = int(lower_entry.get())
            upper = int(upper_entry.get())
        except Exception:
            lower, upper = 0, 255

        # Only update mask if lower <= upper
        if lower <= upper:
            mask = compute_current_mask(image_data_display, staining_type, lower, upper)
        else:
            mask = np.zeros(channel.shape, dtype=np.uint8)
        mask_display = mask * 255  # 0 = black, 255 = white
        ax_mask = fig.add_subplot(1, 3, 3, sharex=ax_source, sharey=ax_source)
        ax_mask.imshow(mask_display, cmap='gray', vmin=0, vmax=255)
        ax_mask.set_title('Binary Mask')
        ax_mask.axis('off')

        canvas.draw()

tab2_content = tk.Frame(content_frame, bg='#ecf0f1')

class YOLOGUI:
    def __init__(self, parent):
        self.parent = parent
        self.model_path = None
        self.test_images_folder = None
        self.model = None
        self.results_folder = None
        self.progress_queue = queue.Queue()
        self.analysis_complete = False
        self.start_time = None
        self.custom_font = tkFont.Font(family="Helvetica", size=18)
        self.bold_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
        self.style = ttk.Style()
        self.style.configure('TButton', font=self.bold_font)
        self.style.configure('TLabel', font=self.custom_font)
        self.style.configure('TEntry', font=self.custom_font)
        self.container = tk.Frame(self.parent, bg='#ecf0f1')
        self.container.grid(sticky="nsew")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_rowconfigure(1, weight=0)
        self.container.grid_rowconfigure(2, weight=0)
        self.container.grid_rowconfigure(3, weight=0)
        self.container.grid_rowconfigure(4, weight=0)
        self.container.grid_rowconfigure(5, weight=0)
        self.container.grid_rowconfigure(6, weight=0)
        self.container.grid_rowconfigure(7, weight=0)
        self.container.grid_rowconfigure(8, weight=0)
        self.container.grid_rowconfigure(9, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.load_model_button = ttk.Button(self.container, text="Load YOLO Model", command=self.load_model)
        self.load_model_button.grid(row=1, column=0, pady=4, padx=5)
        ToolTip(self.load_model_button, "Select Best.pt (YOLO Model)").attach()
        self.model_label = ttk.Label(self.container, text="Model: Not loaded")
        self.model_label.grid(row=2, column=0, pady=4, padx=5)
        self.load_images_button = ttk.Button(self.container, text="Load a folder of images for segmentation.",
                                             command=self.load_test_images_folder)
        self.load_images_button.grid(row=3, column=0, pady=4, padx=5)
        ToolTip(self.load_images_button, "Browse and select the folder containing images for segmentation.").attach()
        self.images_label = ttk.Label(self.container, text="Images Folder: Not loaded")
        self.images_label.grid(row=4, column=0, pady=4, padx=5)
        self.process_images_button = ttk.Button(self.container, text="Start Segmentation",
                                                 command=self.start_processing_thread, state="disabled")
        self.process_images_button.grid(row=5, column=0, pady=(10, 4), padx=5)
        ToolTip(self.process_images_button, "Press to start the segmentation process.").attach()
        self.progress_bar = ttk.Progressbar(self.container, orient="horizontal", length=300,
                                             mode="determinate")
        self.progress_bar.grid(row=6, column=0, pady=(8, 2), padx=5)
        self.progress_label = ttk.Label(self.container, text="Progress: 0%")
        self.progress_label.grid(row=7, column=0, pady=(2, 2), padx=5)
        self.eta_label = ttk.Label(self.container, text="Estimated Time Remaining: Calculating...")
        self.eta_label.grid(row=8, column=0, pady=(2, 10), padx=5)

    def load_model(self):
        self.model_path = filedialog.askopenfilename(title="Select Best.pt (YOLO Model File)",
                                                       filetypes=[("YOLO model", "*.pt")])
        if self.model_path:
            self.model = YOLO(self.model_path)
            self.model_label.config(text="Model: Loaded")
            self.check_ready_to_process()

    def load_test_images_folder(self):
        self.test_images_folder = filedialog.askdirectory(
            title="Select folder of images for segmentation")
        if self.test_images_folder:
            self.images_label.config(text="Images Folder: Loaded")
            self.check_ready_to_process()

    def check_ready_to_process(self):
        if self.model and self.test_images_folder:
            self.process_images_button.config(state="normal")

    def start_processing_thread(self):
        self.analysis_complete = False
        self.progress_bar['value'] = 0
        self.progress_label['text'] = "Progress: 0%"
        self.eta_label['text'] = "Estimated Time Remaining: Calculating..."
        threading.Thread(target=self.process_images).start()
        self.update_progress_bar()

    def update_progress_bar(self):
        try:
            while not self.progress_queue.empty():
                progress, elapsed_time = self.progress_queue.get_nowait()
                self.progress_bar['value'] = progress
                self.progress_label['text'] = f"Progress: {int(progress)}%"
                self.update_eta(progress, elapsed_time)
                self.parent.update_idletasks()
        except queue.Empty:
            pass
        if not self.analysis_complete:
            self.parent.after(100, self.update_progress_bar)
        else:
            self.progress_bar['value'] = 100
            self.progress_label['text'] = "Progress: 100%"
            self.eta_label['text'] = "Processing Complete!"

    def update_eta(self, progress, elapsed_time):
        if progress > 0:
            total_time = elapsed_time * 100 / progress
            remaining_time = total_time - elapsed_time
            eta = timedelta(seconds=int(remaining_time))
            self.eta_label['text'] = f"Estimated Time Remaining: {eta}"

    def remove_near_white(self, image_path, output_path, threshold=200):
        """
        Removes near-white pixels from an image, making them transparent, and pastes the result
        onto a black background.

        Args:
            image_path (str): The path to the input image.
            output_path (str): The path to save the output image (PNG format).
            threshold (int): The threshold value for considering a pixel as near-white.
                             Pixels with RGB values all greater than this threshold are considered near-white.
        """
        try:
            # Open the image
            img = Image.open(image_path)
            img = img.convert("RGBA")  # Ensure the image is in RGBA mode

            datas = img.getdata()
            new_data = []
            for item in datas:
                # Check if the pixel is near-white
                if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                    new_data.append((0, 0, 0, 0))  # Make it transparent BLACK
                else:
                    new_data.append(item)  # Keep the original color
            img.putdata(new_data)

            # Create a black background
            black_background = Image.new("RGBA", img.size, (0, 0, 0, 255))  # Black background, fully opaque

            # Paste the image with white removed onto the black background
            black_background.paste(img, (0, 0), img)
            black_background.save(output_path, "PNG")

            print(f"Processed image saved to {output_path}")

        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}", flush=True)

    def process_images(self):
        if not self.model or not self.test_images_folder:
            return

        # Get all valid image paths
        image_paths = [
            os.path.join(self.test_images_folder, f)
            for f in os.listdir(self.test_images_folder)
            if os.path.isfile(os.path.join(self.test_images_folder, f))
        ]
        total_images = len(image_paths)
        if total_images == 0:
            messagebox.showerror("Error", "No images found in the selected folder.")
            return

        # Create results folders
        with_bbox_folder = os.path.join(self.test_images_folder, "Segmented_images_with_bbox")
        without_bbox_folder = os.path.join(self.test_images_folder, "Segmented_images_without_bbox") # changed name
        binary_masks_folder = os.path.join(self.test_images_folder, "Binary_masks_YOLOV11_results")
        removed_white_folder = os.path.join(self.test_images_folder, "Removed_blood_vessels_and_inner_empty_chamber") # New folder
        removed_white_masks_folder = os.path.join(removed_white_folder, "Binary_masks_removed_blood_vessels_and_inner_empty_chamber")  # New folder for masks
        os.makedirs(with_bbox_folder, exist_ok=True)
        os.makedirs(without_bbox_folder, exist_ok=True) # changed
        os.makedirs(binary_masks_folder, exist_ok=True)
        os.makedirs(removed_white_folder, exist_ok=True) # New folder
        os.makedirs(removed_white_masks_folder, exist_ok=True)  # Make the new mask folder
        # Initialize data for Excel file
        area_data = []
        area_data_removed_white = [] # separate excel
        PROPS = {
            'Area': 'area',
            'Centroid': 'centroid',
            'Orientation': 'orientation',
            'Eccentricity': 'eccentricity',
            'Extent': 'extent',
            'Perimeter': 'perimeter',
            'Solidity': 'solidity',
            'MajorAxisLength': 'axis_major_length',
            'MinorAxisLength': 'axis_minor_length',
        }
        # Initialize progress tracking
        self.start_time = time.time()
        for i, image_path in enumerate(image_paths):
            try:
                # Perform segmentation with the model
                results = self.model(image_path)
                new_result = results[0]
                # Filter to keep only the detection with the highest confidence
                if len(new_result.boxes) > 0:
                    confidences = new_result.boxes.conf.cpu().numpy()
                    max_conf_index = np.argmax(
                        confidences)  # Index of the highest confidence detection
                    # Keep only the highest confidence detection
                    new_result.boxes = new_result.boxes[max_conf_index:max_conf_index + 1]
                    new_result.masks.data = new_result.masks.data[
                        max_conf_index:max_conf_index + 1]
                # Save segmented image with bounding boxes
                result_image_with_bbox = new_result.plot()
                result_image_with_bbox_pil = Image.fromarray(result_image_with_bbox)
                result_image_with_bbox_pil.save(
                    os.path.join(with_bbox_folder, f"segmented_{os.path.basename(image_path)}"))
                # Save instance-segmented image without bounding boxes
                if new_result.masks is not None:
                    masks = new_result.masks.data.cpu().numpy()
                    original_image_array = np.array(
                        Image.open(image_path).convert("RGB"))
                    black_background = np.zeros_like(original_image_array)
                    resized_mask_original_scale = None # To store the resized mask at original image scale

                    for idx, mask in enumerate(masks):
                        # Resize mask to match the original image dimensions
                        resized_mask = resize(mask, (original_image_array.shape[0], original_image_array.shape[1]),
                                              order=1, preserve_range=True,
                                              anti_aliasing=True)
                        resized_mask = resized_mask > 0.5
                        resized_mask_original_scale = resized_mask # Store this for later use

                        # Apply mask to create instance-segmented image
                        black_background[resized_mask] = original_image_array[
                            resized_mask]
                        # Save binary mask (based on the segmentation)
                        binary_mask = (resized_mask > 0.5).astype(np.uint8) * 255
                        binary_mask_image = Image.fromarray(binary_mask).convert("L")
                        binary_mask_image.save(
                            os.path.join(binary_masks_folder,
                                         f"mask_{idx}_{os.path.basename(image_path)}"))
                        # Calculate region properties and save them
                        props = regionprops_table(binary_mask,
                                                  properties=list(PROPS.values()))
                        for key, value in PROPS.items():
                            if key in props:
                                props[key] = props[value]
                        props_data = {
                            "Image Name": os.path.basename(image_path),
                            **{prop: props[prop][0] for prop in props.keys() if
                               len(props[prop]) > 0}
                        }
                        area_data.append(props_data)

                    # Save the instance-segmented image without bounding boxes
                    result_image_without_bbox_pil = Image.fromarray(black_background)
                    result_image_without_bbox_pil.save(
                        os.path.join(without_bbox_folder, f"segmented_{os.path.basename(image_path)}")) # added back saving the original

                    # Remove near-white pixels and save the image to the new folder
                    removed_white_output_path = os.path.join(removed_white_folder,
                                                            f"removed_bw_{os.path.basename(image_path)}")
                    self.remove_near_white(image_path, removed_white_output_path)

                    # Create binary mask for the removed white image (non-black pixels)
                    removed_white_image = Image.open(removed_white_output_path).convert("RGBA")
                    removed_white_array = np.array(removed_white_image)
                    non_black_mask = np.any(removed_white_array[:, :, :3] != [0, 0, 0], axis=-1).astype(np.uint8) * 255
                    removed_white_binary_mask_image = Image.fromarray(non_black_mask).convert("L")
                    removed_white_binary_mask_image.save(
                        os.path.join(removed_white_masks_folder, f"mask_non_black_{os.path.basename(image_path)}"))

                    # Calculate region properties for removed white (using the non-black mask)
                    props_removed_white = regionprops_table(non_black_mask,
                                                              properties=list(PROPS.values()))
                    for key, value in PROPS.items():
                        if key in props_removed_white:
                            props_removed_white[key] = props_removed_white[value]
                    props_data_removed_white = {
                        "Image Name": os.path.basename(image_path),
                        **{prop: props_removed_white[prop][0] for prop in props_removed_white.keys() if
                           len(props_removed_white[prop]) > 0}
                    }
                    area_data_removed_white.append(props_data_removed_white)


                # Update progress
                progress = (i + 1) / total_images * 100
                elapsed_time = time.time() - self.start_time
                self.progress_queue.put((progress, elapsed_time))
            except Exception as e:
                print(f"Error processing image {image_path}: {e}", flush=True)
        # Save area data to Excel
        if area_data:
            area_df = pd.DataFrame(area_data)
            excel_path = os.path.join(binary_masks_folder, "Muscle_Region_Properties_YOLOV11.xlsx") # Changed to binary_masks_folder
            area_df.to_excel(excel_path, index=False)
            messagebox.showinfo("Excel Saved", f"Excel file saved at: {excel_path}")

        if area_data_removed_white: #save new excel file.
            area_df_removed_white = pd.DataFrame(area_data_removed_white)
            excel_path_removed_white = os.path.join(removed_white_folder, "Muscle_Region_Properties_Without_Blood_vessels_And_Inner_Heart_Chamber.xlsx") #changed
            area_df_removed_white.to_excel(excel_path_removed_white, index=False)
            messagebox.showinfo("Excel Saved", f"Excel file saved at: {excel_path_removed_white}")
        # Mark analysis as complete
        self.analysis_complete = True


yolo_gui = YOLOGUI(tab2_content)


tab3_content = tk.Frame(content_frame, bg='#ecf0f1')

class MuscleImageAnalysisApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='#ecf0f1')
        self.master = master
        self.pack(fill='both', expand=True)

        self.lower_pixel_value = tk.StringVar(value='')
        self.upper_pixel_value = tk.StringVar(value='')
        self.create_widgets()
        self.progress_queue = queue.Queue()
        self.analysis_complete = False

    def transfer_pixel_values_from_tab1(self):
        """
        Sync pixel values from Tab 1 globals (auto_selected_lower/upper) to this tab's entries.
        This should be called when the tab is shown.
        """
        global auto_selected_lower, auto_selected_upper
        if auto_selected_lower is not None and auto_selected_upper is not None:
            self.lower_pixel_value.set(str(auto_selected_lower))
            self.upper_pixel_value.set(str(auto_selected_upper))
            print(f"[Muscle Tab] Pixel values loaded from Tab 1: lower={auto_selected_lower}, upper={auto_selected_upper}")

    def load_pixel_values_from_excel(self, staining_type=None):
        """
        Load the most recent pixel values from Defined_pixel_values.xlsx in the input folder.
        Optionally, provide a staining_type ('Sirius Red' or 'Masson Trichrome') to filter.
        """
        try:
            excel_file = os.path.join(self.input_folder, "Defined_pixel_values.xlsx")
            if os.path.exists(excel_file):
                df = pd.read_excel(excel_file)
                if staining_type is not None:
                    df = df[df["Staining Name"] == staining_type]
                if not df.empty:
                    latest = df.iloc[-1]
                    self.lower_pixel_value.set(str(latest["Lower Pixel Value"]))
                    self.upper_pixel_value.set(str(latest["Upper Pixel Value"]))
                    print(f"Loaded pixel values: lower={latest['Lower Pixel Value']}, upper={latest['Upper Pixel Value']}")
                else:
                    print("No matching staining type found in Excel file.")
            else:
                print("No pixel value Excel file found in input folder.")
        except Exception as e:
            print(f"Error loading pixel values from Excel: {e}")

    def create_widgets(self):
        self.select_input_button = tk.Button(
            self, text="Upload Segmented Images",
            command=self.select_input_folder,
            bg='#34495e', fg='#ffffff', font=('Arial Bold', 18)
        )
        self.select_input_button.pack(pady=20)
        ToolTip(self.select_input_button, "Select the segmented images from step 2").attach()

        self.pixel_value_range_label = tk.Label(
            self, text="Pixel Value Range:", bg='#ecf0f1', font=('Arial Bold', 14)
        )
        self.pixel_value_range_label.pack(pady=5)

        self.lower_pixel_value_label = tk.Label(
            self, text="Lower Value:", bg='#ecf0f1', font=('Arial Bold', 14)
        )
        self.lower_pixel_value_label.pack(pady=5)
        ToolTip(self.lower_pixel_value_label, "Select the lower pixel value from Step 1 or from the saved Excel file.").attach()

        self.lower_pixel_value_entry = tk.Entry(
            self, textvariable=self.lower_pixel_value,
            bg='white', fg='black', font=('Arial Bold', 14)
        )
        self.lower_pixel_value_entry.pack(pady=5)

        self.upper_pixel_value_label = tk.Label(
            self, text="Upper Value:", bg='#ecf0f1', font=('Arial Bold', 14)
        )
        self.upper_pixel_value_label.pack(pady=5)
        ToolTip(self.upper_pixel_value_label, "Select the upper pixel value from Step 1 or from the saved Excel file.").attach()

        self.upper_pixel_value_entry = tk.Entry(
            self, textvariable=self.upper_pixel_value,
            bg='white', fg='black', font=('Arial Bold', 14)
        )
        self.upper_pixel_value_entry.pack(pady=5)

        self.analyze_masson_button = tk.Button(
            self, text="Analyze Masson Trichrome",
            command=self.start_masson_analysis_thread,
            bg='#5dade2', fg='#ffffff', font=('Arial Bold', 18)
        )
        self.analyze_masson_button.pack(pady=20)
        ToolTip(self.analyze_masson_button, "Press to analyze masson trichrome images").attach()

        self.analyze_sirius_button = tk.Button(
            self, text="Analyze Sirius Red",
            command=self.start_sirius_analysis_thread,
            bg='#5dade2', fg='#ffffff', font=('Arial Bold', 18)
        )
        self.analyze_sirius_button.pack(pady=20)
        ToolTip(self.analyze_sirius_button, "Press to analyze sirius red images").attach()

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.progress_label = tk.Label(
            self, text="Progress: 0%", bg='#ecf0f1', font=('Arial Bold', 14)
        )
        self.progress_label.pack(pady=5)

        self.eta_label = tk.Label(
            self, text="Estimated Time Remaining: Calculating...", bg='#ecf0f1', font=('Arial Bold', 14)
        )
        self.eta_label.pack(pady=5)

    def select_input_folder(self):
        self.input_folder = filedialog.askdirectory(title='Select Input Folder')
        if not self.input_folder:
            messagebox.showinfo("Info", "No folder selected.")
        else:
            now = datetime.now()
            date_time = now.strftime("%d-%m-%Y_%H-%M-%S")
            day_name = now.strftime("%A")  
            self.output_folder = os.path.join(self.input_folder, f'Final_Results_Analyzed_Fibrotic_Muscles_{day_name}_{date_time}')
            os.makedirs(self.output_folder, exist_ok=True)
            print(f"Selected input folder: {self.input_folder}", flush=True)
            print(f"Output folder created: {self.output_folder}", flush=True)
            # Notify user that the folder was selected
            messagebox.showinfo("Folder Selected", f"Segmented images folder selected:\n\n{self.input_folder}\n\nNow transferring pixel values from Step 1 ...")
            self.load_pixel_values_from_excel()
            self.transfer_pixel_values_from_tab1()  # Always try to use the latest from Tab 1
    
    def transfer_pixel_values_from_tab1(self):
        """
        Sync pixel values from Tab 1 globals (auto_selected_lower/upper) to this tab's entries.
        This should be called when the tab is shown.
        """
        global auto_selected_lower, auto_selected_upper
        if auto_selected_lower is not None and auto_selected_upper is not None:
            self.lower_pixel_value.set(str(auto_selected_lower))
            self.upper_pixel_value.set(str(auto_selected_upper))
            print(f"[Muscle Tab] Pixel values loaded from Tab 1: lower={auto_selected_lower}, upper={auto_selected_upper}")
            # Notify user that the values were transferred
            messagebox.showinfo(
                "Pixel Values Transferred",
                f"Automatic pixel values from Step 1 have been transferred:\n\n"
                f"Lower: {auto_selected_lower}\nUpper: {auto_selected_upper}\n\n"
                f"Please confirm or adjust if necessary before analysis."
            )

    def start_masson_analysis_thread(self):
        self.start_analysis_thread(channel='B')

    def start_sirius_analysis_thread(self):
        self.start_analysis_thread(channel='A')

    def start_analysis_thread(self, channel):
        self.analysis_complete = False
        self.progress_bar['value'] = 0
        self.progress_label['text'] = "Progress: 0%"
        self.eta_label['text'] = "Estimated Time Remaining: Calculating..."

        try:
            lower_pixel_value = int(self.lower_pixel_value.get())
            upper_pixel_value = int(self.upper_pixel_value.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid integers.")
            return

        if not hasattr(self, 'input_folder') or not hasattr(self, 'output_folder'):
            messagebox.showerror("Error", "Please select an input folder.")
            return

        self.start_time = time.time()
        threading.Thread(target=self.analyze_images, args=(lower_pixel_value, upper_pixel_value, channel), daemon=True).start()
        self.update_progress_bar()

    def update_progress_bar(self):
        try:
            while not self.progress_queue.empty():
                progress, elapsed_time = self.progress_queue.get_nowait()
                self.progress_bar['value'] = progress
                self.progress_label['text'] = f"Progress: {int(progress)}%"
                self.update_eta(progress, elapsed_time)
                self.master.update_idletasks()
        except queue.Empty:
            pass

        if not self.analysis_complete:
            self.master.after(100, self.update_progress_bar)
        else:
            self.progress_bar['value'] = 100
            self.progress_label['text'] = "Progress: 100%"
            self.eta_label['text'] = "Your Analysis Is Done!"

    def update_eta(self, progress, elapsed_time):
        if progress > 0:
            total_time = elapsed_time * 100 / progress
            remaining_time = total_time - elapsed_time
            eta = timedelta(seconds=int(remaining_time))
            self.eta_label['text'] = f"Estimated Time Remaining: {eta}"

    def analyze_images(self, lower_pixel_value, upper_pixel_value, channel):
        image_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff'))]
        total_files = len(image_files)
        results = []
        
        for idx, filename in enumerate(image_files):
            image_path = os.path.join(self.input_folder, filename)
            src = cv2.imread(image_path)
            if src is None:
                continue  
        
            # Convert the image to LAB color space
            LAB = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
        
            # Select the appropriate channel (A or B)
            if channel == 'B':
                LAB_channel = LAB[:, :, 2]  # 'B' channel
            elif channel == 'A':
                LAB_channel = LAB[:, :, 1]  # 'A' channel
        
            # Apply the pixel range directly to the selected LAB channel
            binary_mask = np.logical_and(LAB_channel >= lower_pixel_value, LAB_channel <= upper_pixel_value)
            binary_mask = binary_mask.astype(np.uint8) * 255  # Convert to binary mask (Collagen Area)
        
            # Save the binary mask for Collagen Area
            binary_mask_filename = os.path.join(self.output_folder, f'{filename}_collagen_binary_mask.tif')
            cv2.imwrite(binary_mask_filename, binary_mask)
        
            # Generate the binary mask for Muscle Area from the segmented input image
            muscle_mask = cv2.imread(image_path)  # Reload the segmented image
            muscle_mask = np.any(muscle_mask > [0, 0, 0], axis=-1)  # Identify non-black pixels
            muscle_mask = muscle_mask.astype(np.uint8) * 255  # Convert to binary mask
        
            # Save the Muscle Area binary mask
            muscle_mask_filename = os.path.join(self.output_folder, f'{filename}_muscle_binary_mask.tif')
            cv2.imwrite(muscle_mask_filename, muscle_mask)
        
            # Calculate areas and ratios
            collagen_area = np.sum(binary_mask > 0)  # Collagen Area (no cleaned mask)
            muscle_area = np.sum(muscle_mask > 0)    # Muscle Area
            fibrosis_ratio = (collagen_area / muscle_area) * 100 if muscle_area > 0 else 0  # Fibrosis Ratio (%)
        
            # Append the results
            results.append([filename, collagen_area, muscle_area, fibrosis_ratio])
        
            # Update progress
            progress = (idx + 1) / total_files * 100
            elapsed_time = time.time() - self.start_time
            self.progress_queue.put((progress, elapsed_time))
        
        # Save the results to a CSV file
        self.save_results_to_csv(results, channel)
        self.analysis_complete = True
        messagebox.showinfo("Info", "Analysis Complete")
    
    def save_results_to_csv(self, results, channel):
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y_%H-%M-%S")
        day_name = now.strftime("%A")
        csv_filename = os.path.join(self.output_folder, f'Fibrosis(%)_Results_{channel}_{day_name}_{date_time}.csv')
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ['Image Filename', 'Collagen Area', 'Muscle Area', 'Fibrosis Ratio(%) Normalized - (Collagen Area/Muscle Area)']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                writer.writerow({
                    'Image Filename': result[0],
                    'Collagen Area': result[1],
                    'Muscle Area': result[2],
                    'Fibrosis Ratio(%) Normalized - (Collagen Area/Muscle Area)': result[3]
                })

muscle_analysis_app = MuscleImageAnalysisApp(master=tab3_content)


tabs = {
    "tab1": tab1_content,
    "tab2": tab2_content,
    "tab3": tab3_content
}

switch_tab("tab1")

root.bind("<Configure>", lambda event: adjust_icon_sizes())
root.mainloop()