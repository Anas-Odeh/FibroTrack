# FibroTrack

**FibroTrack** is a standalone deep learning platform for **automated fibrosis quantification** in histological images of **skeletal and cardiac muscle tissues**.  

The tool uniquely combines **LAB color space normalization** with a **YOLOv11 segmentation model** trained on 2,034 annotated images. This integration enables robust and reproducible fibrosis analysis across **Sirius Red (SR)**, **Masson’s Trichrome (MT)**, and **immunohistochemistry (IHC)** stainings.  

FibroTrack delivers **>97% precision**, demonstrates excellent concordance with blinded pathologists (Spearman r = 0.87–0.96), and produces structured outputs (segmented images + spreadsheets) in a fully automated workflow.  

---

## ✨ Key Features
- **LAB color space normalization**  
  Superior separation of fibrotic tissue from artifacts compared to RGB/HSV. Robust across SR, MT, and IHC stains.  

- **YOLOv11 segmentation**  
  Trained on a diverse dataset of 2,034 images with data augmentation (exposure, brightness, blur). Achieves mask precision of 97.5% and recall of 95.3%.  

- **Objective fibrosis ratio measurement**  
  Calculates the percentage of fibrotic tissue relative to the total muscle area with high reproducibility.  

- **Cross‑validated performance**  
  Agreement with blinded pathologists (r = 0.87–0.96) and no significant differences compared to manual scoring.  

- **Standalone, user‑friendly GUI**  
  Requires no programming skills or external software. Supports JPG, PNG, TIFF.  

- **Organized outputs**  
  Automatically generates segmented images, binary masks, and structured CSV/Excel files in timestamped folders.  

- **High throughput**  
  Processes images in ~5 ms each, suitable for large‑scale studies.  

---

## 🚀 Workflow

### Step 1: Define Your Pixels  
Users define pixel intensity thresholds in **LAB color space**. Auto‑selection is provided, with optional manual refinement.  

<img width="539" alt="Step 1: Define Pixels" src="https://github.com/user-attachments/assets/62977251-d9bf-4201-8ae8-bb6ba4cafbcc">

### Step 2: Muscle Segmentation  
YOLOv11 performs whole‑tissue segmentation, robust to staining variability and imaging artifacts.  

<img width="537" alt="Step 2: Segmentation" src="https://github.com/user-attachments/assets/e423ea06-1c96-43f8-8231-c5af8d5377fc">

### Step 3: Analyze Fibrosis  
Fibrosis ratios are calculated automatically and exported in structured CSV files.  

<img width="536" alt="Step 3: Analyze" src="https://github.com/user-attachments/assets/392ffb3b-c284-4c5b-bede-f47acef1aa3f">

---

## 🧪 Applications
FibroTrack can be applied in both **preclinical** and **clinical** contexts, including:  
- **Duchenne Muscular Dystrophy (DMD)** – quantification of progressive muscle replacement by fibrosis.  
- **Cardiac hypertrophy and heart failure** – evaluation of pathological remodeling.  
- **Clinical biopsies** – correlation of fibrosis levels with prognosis, outcomes, or response to therapies.  

---

## 💻 System Requirements
- **OS**: Windows 10/11 Pro 64‑bit or Windows Server 2019 Standard  
- **Processor**: Intel Core i7 (11th Gen or newer, ≥2.5 GHz)  
- **RAM**: 16 GB recommended (minimum 8 GB)  
- **Storage**: ~700 MB available space  

---

## ⚙️ Installation
1. Download the installation package: [FibroTrack Installer](https://drive.google.com/file/d/1PvTxR_7k43wXrBx1fXlQomSxXSApQrA2/view?usp=sharing)  
2. Extract the folder `FibroTrack installation.zip`.  
3. Run **Install FibroTrack Graphical User Interface.exe**.  
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
If you use **FibroTrack**, please cite:  

> Odeh A, Salem R, Abu Saleh M, Shemesh A, Stein P, Livneh I, Hasson P.  
> *FibroTrack: A Standalone Deep Learning Platform for Automated Fibrosis Quantification in Muscle and Cardiac Histology.*  
> **Artificial Intelligence in Medicine.** 2025.  

---











