# FibroTrack

**FibroTrack** is an open-source, standalone deep learning platform equipped with a graphical user interface (GUI) designed to automate and streamline the quantification of fibrosis in histological images of skeletal and cardiac muscle.

---

## ✨ Key Features
- **Deep Learning Segmentation**  
  Utilizes a **YOLOv11-seg** model to accurately isolate muscle tissue from background artifacts with 99.5% mask precision. 

- **Advanced Color Analysis**  
  Integrates **LAB color space normalization** to standardize profiles across images, compensating for variations in staining intensity and microscope settings. 

- **Multi-Stain Support**  
  Optimized for **Sirius Red (SR)**, **Masson’s Trichrome (MT)**, and **Immunohistochemistry (IHC)** (e.g., Collagen I/III).

- **Standalone Accessibility**  
  No programming skills, external toolboxes, or legacy software (like MATLAB) are required.   

- **High Performance**  
  Processes images in approximately **7.3 ms per image** (inference time: 4.4 ms).
  
- **Organized outputs**  
  Automatically generates segmented images, binary masks, and structured CSV/Excel files in timestamped folders.  

---

## 🚀 Workflow

### Step 1: Define Your Pixels  
RGB images are converted to LAB space to facilitate the selection of specific pixel intensity values for fibrotic regions. 

<img width="539" alt="Step 1: Define Pixels" src="https://github.com/user-attachments/assets/62977251-d9bf-4201-8ae8-bb6ba4cafbcc">

### Step 2: Muscle Segmentation  
The YOLOv11 model automatically generates a precise muscle-tissue mask.  

<img width="537" alt="Step 2: Segmentation" src="https://github.com/user-attachments/assets/e423ea06-1c96-43f8-8231-c5af8d5377fc">

### Step 3: Analyze Fibrosis  
The software applies validated thresholds within the spatial constraints of the muscle mask to calculate the final Fibrosis Ratio (FR). 

<img width="536" alt="Step 3: Analyze" src="https://github.com/user-attachments/assets/392ffb3b-c284-4c5b-bede-f47acef1aa3f">

---

## 📊 Validation
FibroTrack was validated against blinded expert pathologists (n=31 samples), demonstrating:
- **High Concordance**: Spearman correlation coefficients of r=0.87 - 0.96.
- **Statistical Robustness**: No significant difference between automated and manual expert assessments (Kruskal-Wallis, p=0.96).
- **High Specificity**: Effectively excludes artifacts and nuclei that often lead to inaccurate quantification in standard RGB or HSV analysis.

---

## 💻 System Requirements
- **OS**: Windows 10/11 Pro 64-bit. 
- **Hardware**: 11th Gen Intel Core i7 or better; 16 GB RAM recommended.

---

## ⚙️ Installation
1. Download the installation package: [FibroTrack Installer](https://drive.google.com/file/d/1P38xbORR3kxTRPxbpgdbAxLhrRFLsMKt/view?usp=sharing)  
2. Extract the folder `FibroTrack installation.zip`.  
3. Run **FibroTrack Software.exe**.  
4. The GUI will install and configure automatically.  

---

## 📖 Usage
- For usage instructions, see the [Documentation](./docs/USAGE.md).  
- Input supported: JPG, PNG, TIFF.  
- Outputs include segmented images, binary masks, and fibrosis ratios in CSV/Excel format.  

---

## 🛠 Troubleshooting

If the analysis hangs (e.g., spinning for 30+ minutes) or the results folder remains empty, please verify the following:

> [!WARNING]
> ## Large Image & Memory Warning
>
> FibroTrack may close unexpectedly when processing images with very large pixel dimensions. **The file size in MB is not a reliable indicator of memory usage**, because compressed images are expanded when opened and may require several additional full-resolution arrays during analysis.
>
> For example, an image measuring **7000 × 6000 pixels** contains approximately **42 million pixels (42 megapixels)**. Although the image file may be only **7.5–8 MB**, it can consume hundreds of megabytes—or more—of RAM and GPU memory during processing.
>
> If FibroTrack closes while analyzing a large image, downsample the image or divide it into smaller tiles before trying again.
>
> ### Resize an image to 50% using ImageJ or Fiji
>
> To reduce both the width and height by a factor of **0.5**:
>
> 1. Open the image in **ImageJ** or **Fiji**.
> 2. From the menu, select **Image → Scale...**
> 3. Enter:
>    - **X Scale:** `0.5`
>    - **Y Scale:** `0.5`
> 4. Enable **Constrain Aspect Ratio** if available.
> 5. Enable **Interpolate** for smoother resizing.
> 6. Enable **Average When Downsizing** if available.
> 7. Click **OK**.
> 8. Save the resized image as a **new file** using **File → Save As**. Do not overwrite the original image unless you have a backup.
>
> ### Example
>
> | Original image | Scale factor | Resized image |
> |---|---:|---:|
> | 7000 × 6000 pixels | 0.5 | 3500 × 3000 pixels |
>
> Reducing both dimensions by half reduces the total pixel count from approximately **42 megapixels to 10.5 megapixels**. This is a **75% reduction in total pixels**, which can significantly reduce memory usage during analysis.
>
> ### Recommended precautions
>
> - Always keep a copy of the original full-resolution image.
> - Check the image’s **pixel dimensions**, not only its file size in MB.
> - Close other memory-intensive applications before running FibroTrack.
> - Process fewer images at one time.
> - If resizing to 50% is insufficient, use a smaller scale factor or divide the image into smaller tiles.
> - Confirm that the resized image still provides enough resolution for reliable biological analysis.
>
> **Note:** FibroTrack does not currently enforce a universal fixed megapixel limit. The practical image-size limit depends on available system RAM, GPU memory, image format, bit depth, batch size, and the selected analysis workflow.

> [!IMPORTANT]
> **Shorten your File Path**  
> Long or complex folder paths are the most common cause of execution failure. If your images are buried in many sub-folders, the software may not be able to "reach" them.
> * **❌ Avoid:** `C:\Users\Name\Documents\Lab_Research\2026\Project_Alpha\Data\Batch_01\Images`
> * **✅ Recommended:** Move your folder directly to the **Desktop** (e.g., `C:\Users\Name\Desktop\Analysis`) and run it from there.

> [!NOTE]
> **Verify Image Formats**  
> FibroTrack is optimized for **.jpg**, **.png**, and **.tiff** files. Ensure your extensions match exactly. If you are using a different format, please convert them before starting the analysis.

> [!TIP]
> **Permissions**  
> If the software fails to save the final Excel/CSV data, try **Running as Administrator**. This ensures the program has full permission to create new folders and files on your drive.

---

### Still having trouble?
If these steps don't solve the issue, please [open an issue](https://github.com/Anas-Odeh/FibroTrack/issues) and include:
1. A **screenshot** of the GUI where the process hangs.
2. The **specific image type** and resolution you are using.
3. A copy of the **Full File Path** you are trying to use.

---

## 📚 Data & Code Availability
- **Raw images, dataset splits, and YOLOv11 configs**: [FibroTrack Dataset](https://github.com/Anas-Odeh/FibroTrack)  
- **Source code (Python)**: `FibroTrackSourceCodeFinal.py` under [MIT License](./LICENSE).  

---

## 📜 License
FibroTrack is released under the [MIT License](./LICENSE).  

---

## 📖 Citation
If you use FibroTrack in your research, please cite our paper: 

> Odeh, A., Salem, R., Saleh, M.A. et al. FibroTrack: a standalone deep learning platform for automated fibrosis quantification in muscle and cardiac histology. Skeletal Muscle 16, 13 (2026). https://doi.org/10.1186/s13395-026-00415-8
