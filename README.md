# FibroTrack

**FibroTrack** is an open-source, standalone deep learning platform equipped with a graphical user interface (GUI) designed to automate and streamline the quantification of fibrosis in histological images of skeletal and cardiac muscle

---

## ✨ Key Features
- **Deep Learning Segmentation**  
  Utilizes a **YOLOv11-seg** model to accurately isolate muscle tissue from background artifacts with 99.5% mask precision. 

- **Advanced Color Analysis**  
  Integrates **LAB color space normalization** to standardize profiles across images, compensating for variations in staining intensity and microscope settings. 

- **Multi-Stain Support**  
  Optimized for **Sirius Red (SR)**, **Masson’s Trichrome (MT)**, and **Immunohistochemistry (IHC)** (e.g., Collagen I/III)

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
---











