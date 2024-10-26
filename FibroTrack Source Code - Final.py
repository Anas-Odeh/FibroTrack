import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    try:
        import pyi_splash
        pyi_splash.update_text("Initializing FibroTrack...")
    except ImportError:
        pass  

import itertools
import threading
from colorama import Fore, Style, init, Back
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
    # Close the splash screen after initialization
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
            self.current_step += 1
            time.sleep(self.delay)
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

print("Imports completed.\n\nPlease wait, you're almost there...\n\nLaunching the FibroTrack application...\n\n", flush=True)

def find_fibrotrack_icons_folder():
    home_dir = os.path.expanduser("~")
    for root_dir, dirs, files in os.walk(home_dir):
        if "FibroTrackIcons" in dirs:
            return os.path.join(root_dir, "FibroTrackIcons")
    raise FileNotFoundError("FibroTrackIcons folder not found.")


try:
    fibrotrack_icons_folder = find_fibrotrack_icons_folder()
except FileNotFoundError as e:
    print(e,flush=True)
    messagebox.showerror("Error", "The FibroTrackIcons folder could not be found.")
    exit()


tab1_path = os.path.join(fibrotrack_icons_folder, "Odeh et al. Define Pixel.png")
tab2_path = os.path.join(fibrotrack_icons_folder, "Odeh et al. Muscle Segmentation.png")
tab3_path = os.path.join(fibrotrack_icons_folder, "Odeh et al. Analyze Fibrosis.png")


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


background_image = ImageTk.PhotoImage(Image.open('Splash Screen.tif'))

background_label = Label(w, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = Label(w, text='Welcome To FibroTrack!', fg='white', bg='#364FD0')
label1.configure(font=("Arial", 24, "bold"), bg='#364FD0')
label1.place(x=20, y=60)

label2 = Label(w, text='Loading...', fg='white', bg='#364FD0')
label2.configure(font=("Arial", 20))
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

def save_pixel_values():
    global lower_value, upper_value, image_name, image_dir, current_staining_type
    try:
        lower_value = int(lower_entry.get())
        upper_value = int(upper_entry.get())
        print(f"Lower value: {lower_value}, Upper value: {upper_value}")

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

ToolTip(sirius_red_button, "Click here to load a Sirius Red Image").attach()

masson_trichrome_button = ttk.Button(tab1_content, text="Load Masson Trichrome Image", command=lambda: load_image('Masson Trichrome'))
masson_trichrome_button.pack(pady=10)

ToolTip(masson_trichrome_button, "Click here to load a Masson Trichrome Image").attach()

def on_entry_change(entry_widget):
    if entry_widget.get():
        entry_widget.config(font=("Helvetica", 20, "bold"))
    else:
        entry_widget.config(font=("Helvetica", 20))

lower_label = ttk.Label(tab1_content, text="Lower Pixel Value:")
lower_label.pack(pady=5)

lower_entry = ttk.Entry(tab1_content, font=("Helvetica", 12))
lower_entry.pack(pady=5)
lower_entry.bind("<KeyRelease>", lambda event: on_entry_change(lower_entry))

ToolTip(lower_entry, "Hover over the A (Sirius Red) or B (Masson Trichrome) channel\nto see the pixel value corresponding to the darkest yellow (A) or blue (B) color in the image,\ndisplayed in the top-right corner (e.g., 10.0).").attach()

upper_label = ttk.Label(tab1_content, text="Upper Pixel Value:")
upper_label.pack(pady=5)

upper_entry = ttk.Entry(tab1_content, font=("Helvetica", 12))
upper_entry.pack(pady=5)
upper_entry.bind("<KeyRelease>", lambda event: on_entry_change(upper_entry))

ToolTip(upper_entry, "Hover over the A (Sirius Red) or B (Masson Trichrome) channel\nto see the pixel value corresponding to the brightest yellow (A) or blue (B) color in the image\ndisplayed in the top-right corner (e.g., 255.0).").attach()

save_button = ttk.Button(tab1_content, text="Save Pixel Values", command=save_pixel_values)
save_button.pack(pady=10)

ToolTip(save_button, "Click to export pixel values to an Excel file saved in the selected image's folder.").attach()


fig = Figure(figsize=(12, 6))
canvas = FigureCanvasTkAgg(fig, master=tab1_content)
toolbar = NavigationToolbar2Tk(canvas, tab1_content)
toolbar.update()
toolbar.pack(side=tk.TOP, fill=tk.X)


canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def load_image(staining_type):
    global image_data, ax_source, loaded_image_path, image_name, image_dir, current_staining_type
    file_path = easygui.fileopenbox(title=f"Select an image file for {staining_type}", filetypes=["*.jpg", "*.jpeg", "*.png", "*.tif", "*.tiff"])
    if file_path:
        try:
            image_data = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
            if image_data.ndim == 3:
                image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
            loaded_image_path = file_path
            image_name = os.path.basename(file_path)
            image_dir = os.path.dirname(file_path)
            current_staining_type = staining_type
            update_image_display(staining_type)
        except Exception as e:
            print(f"An error occurred: {e}",flush=True)

def update_image_display(staining_type):
    global image_data, fig, ax_source

    if image_data is not None:
        fig.clf()

        ax_source = fig.add_subplot(1, 2, 1)
        ax_source.imshow(image_data)
        ax_source.set_title('Source Image')
        ax_source.axis('on')

        lab_image = cv2.cvtColor(image_data, cv2.COLOR_RGB2Lab)

        if staining_type == 'Sirius Red':
            channel = lab_image[:, :, 1]
            channel_title = 'A Channel'
        elif staining_type == 'Masson Trichrome':
            channel = lab_image[:, :, 2]
            channel_title = 'B Channel'
        else:
            raise ValueError("Unsupported staining type")

        ax = fig.add_subplot(1, 2, 2, sharex=ax_source, sharey=ax_source)
        ax.imshow(channel)
        ax.set_title(f'{channel_title} ({staining_type})')
        ax.axis('on')

        fig.tight_layout()
        fig.canvas.draw()

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

        self.load_images_button = ttk.Button(self.container, text="Load a folder of images for segmentation.", command=self.load_test_images_folder)
        self.load_images_button.grid(row=3, column=0, pady=4, padx=5)
        
        ToolTip(self.load_images_button, "Browse and select the folder containing images for segmentation.").attach()

        self.images_label = ttk.Label(self.container, text="Images Folder: Not loaded")
        self.images_label.grid(row=4, column=0, pady=4, padx=5)

        self.process_images_button = ttk.Button(self.container, text="Start Segmentation", command=self.start_processing_thread, state="disabled")
        self.process_images_button.grid(row=5, column=0, pady=(10, 4), padx=5)
        
        ToolTip(self.process_images_button, "Press to start the segmentation process.").attach()

        self.progress_bar = ttk.Progressbar(self.container, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=6, column=0, pady=(8, 2), padx=5)

        self.progress_label = ttk.Label(self.container, text="Progress: 0%")
        self.progress_label.grid(row=7, column=0, pady=(2, 2), padx=5)

        self.eta_label = ttk.Label(self.container, text="Estimated Time Remaining: Calculating...")
        self.eta_label.grid(row=8, column=0, pady=(2, 10), padx=5)

    def load_model(self):
        self.model_path = filedialog.askopenfilename(title="Select Best.pt (YOLO Model File)", filetypes=[("YOLO model", "*.pt")])
        if self.model_path:
            self.model = YOLO(self.model_path)
            self.model_label.config(text="Model: Loaded")
            self.check_ready_to_process()

    def load_test_images_folder(self):
        self.test_images_folder = filedialog.askdirectory(title="Select folder of images for segmentation")
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

    def process_images(self):
        if not self.model or not self.test_images_folder:
            return

        image_paths = [os.path.join(self.test_images_folder, f) for f in os.listdir(self.test_images_folder)
                       if os.path.isfile(os.path.join(self.test_images_folder, f))]

        total_images = len(image_paths)
        if total_images == 0:
            messagebox.showerror("Error", "No images found in the selected folder.")
            return

        self.results_folder = os.path.join(self.test_images_folder, "results")
        os.makedirs(self.results_folder, exist_ok=True)

        self.start_time = time.time()
        for i, image_path in enumerate(image_paths):
            try:
                results = self.model(image_path)
                result_image = results[0].plot()

                result_image_pil = Image.fromarray(result_image)
                result_image_pil.save(os.path.join(self.results_folder, f"{os.path.basename(image_path)}"))

                progress = (i + 1) / total_images * 100
                elapsed_time = time.time() - self.start_time
                self.progress_queue.put((progress, elapsed_time))
            except Exception as e:
                print(f"Error processing image {image_path}: {e}",flush=True)

        self.analysis_complete = True

yolo_gui = YOLOGUI(tab2_content)

# Tab 3 content (MuscleImageAnalysisApp Integrated)
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

    def create_widgets(self):
        self.select_input_button = tk.Button(self, text="Upload Segmented Images", command=self.select_input_folder, bg='#34495e', fg='#ffffff', font=('Arial Bold', 18))
        self.select_input_button.pack(pady=20)
        
        ToolTip(self.select_input_button, "Select the segmented images from step 2").attach()

        self.pixel_value_range_label = tk.Label(self, text="Pixel Value Range:", bg='#ecf0f1', font=('Arial Bold', 14))
        self.pixel_value_range_label.pack(pady=5)

        self.lower_pixel_value_label = tk.Label(self, text="Lower Value:", bg='#ecf0f1', font=('Arial Bold', 14))
        self.lower_pixel_value_label.pack(pady=5)
        
        ToolTip(self.lower_pixel_value_label, "Select the lower pixel value from Step 1 or from the saved Excel file.").attach()

        self.lower_pixel_value_entry = tk.Entry(self, textvariable=self.lower_pixel_value, bg='white', fg='black', font=('Arial Bold', 14))
        self.lower_pixel_value_entry.pack(pady=5)

        self.upper_pixel_value_label = tk.Label(self, text="Upper Value:", bg='#ecf0f1', font=('Arial Bold', 14))
        self.upper_pixel_value_label.pack(pady=5)
        
        ToolTip(self.upper_pixel_value_label, "Select the upper pixel value from Step 1 or from the saved Excel file.").attach()

        self.upper_pixel_value_entry = tk.Entry(self, textvariable=self.upper_pixel_value, bg='white', fg='black', font=('Arial Bold', 14))
        self.upper_pixel_value_entry.pack(pady=5)

        self.analyze_masson_button = tk.Button(self, text="Analyze Masson Trichrome", command=self.start_masson_analysis_thread, bg='#5dade2', fg='#ffffff', font=('Arial Bold', 18))
        self.analyze_masson_button.pack(pady=20)
        
        ToolTip(self.analyze_masson_button , "Press to analyze masson trichrome images").attach()

        self.analyze_sirius_button = tk.Button(self, text="Analyze Sirius Red", command=self.start_sirius_analysis_thread, bg='#5dade2', fg='#ffffff', font=('Arial Bold', 18))
        self.analyze_sirius_button.pack(pady=20)
        
        ToolTip(self.analyze_sirius_button, "Press to analyze sirius red images").attach()

        # Progress bar and ETA label
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.progress_label = tk.Label(self, text="Progress: 0%", bg='#ecf0f1', font=('Arial Bold', 14))
        self.progress_label.pack(pady=5)

        self.eta_label = tk.Label(self, text="Estimated Time Remaining: Calculating...", bg='#ecf0f1', font=('Arial Bold', 14))
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
            print(f"Selected input folder: {self.input_folder}",flush=True)
            print(f"Output folder created: {self.output_folder}",flush=True)

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

            LAB = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
            GrayImage = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            _, binary_mask = cv2.threshold(GrayImage, 0, 255, cv2.THRESH_BINARY)
            binary_mask_filename = os.path.join(self.output_folder, f'{filename}_binary_mask.tif')
            cv2.imwrite(binary_mask_filename, binary_mask)

            if channel == 'B':
                LAB_channel = LAB[:, :, 2]  
            elif channel == 'A':
                LAB_channel = LAB[:, :, 1]  


            extracted_pixels = np.logical_and(LAB_channel >= lower_pixel_value, LAB_channel <= upper_pixel_value)
            extracted_pixels = extracted_pixels.astype(np.uint8) * 255

            extracted_pixels_cleaned = remove_small_objects(extracted_pixels > 0, min_size=0)
            extracted_pixels_cleaned = extracted_pixels_cleaned.astype(np.uint8) * 255

            extracted_pixels_filename = os.path.join(self.output_folder, f'{filename}_{channel}_extracted_pixels_cleaned.tif')
            cv2.imwrite(extracted_pixels_filename, extracted_pixels_cleaned)

            extracted_area = np.sum(extracted_pixels_cleaned > 0)
            binary_area = np.sum(binary_mask > 0)
            ratio = (extracted_area / binary_area) * 100
            results.append([filename, extracted_area, binary_area, ratio])

            progress = (idx + 1) / total_files * 100
            elapsed_time = time.time() - self.start_time
            self.progress_queue.put((progress, elapsed_time))

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
                writer.writerow({'Image Filename': result[0], 'Collagen Area': result[1], 'Muscle Area': result[2], 'Fibrosis Ratio(%) Normalized - (Collagen Area/Muscle Area)': result[3]})


muscle_analysis_app = MuscleImageAnalysisApp(master=tab3_content)


tabs = {
    "tab1": tab1_content,
    "tab2": tab2_content,
    "tab3": tab3_content
}

switch_tab("tab1")

root.bind("<Configure>", lambda event: adjust_icon_sizes())
root.mainloop()
