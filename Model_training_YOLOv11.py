# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:00:43 2024

@author: AnasO
"""

#%%
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

#%%
from ultralytics import YOLO
import torch
import yaml

#%%
# Enable shared memory usage
torch.cuda.set_per_process_memory_fraction(0.3)  
torch.cuda.empty_cache()  # Clear any existing allocations

def main():
    # Instance
    model = YOLO('yolo11n-seg.yaml')  
    model = YOLO('yolo11n-seg.pt')

    # Read data.yaml
    file_path = r"C:\Users\AnasO\Documents\Anas Odeh - Ph.D\Computational Projects\FibroTrack - Muscle fibrosis\Dataset\FibroTrack_YOLOv11_Dataset_Split\data.yaml"
    with open(file_path, 'r') as stream:
        data_yaml = yaml.safe_load(stream)
        num_classes = str(data_yaml['nc'])
        print(f"Number of classes: {num_classes}")

    # Define project and name
    project = r"C:\Users\AnasO\Documents\Anas Odeh - Ph.D\Computational Projects\FibroTrack - Muscle fibrosis\Dataset\FibroTrack_YOLOv11_Dataset_Split\results"
    name = "epochs-shared-memory"

    # Train the model
    results = model.train(
        data=file_path,
        project=project,
        name=name,
        epochs=2000,
        patience=0,
        batch=2,
        lr0=0.0001,
        lrf=0.001,
        device=0,
        cache='ram',
        amp=True
    )

if __name__ == '__main__':
    main()