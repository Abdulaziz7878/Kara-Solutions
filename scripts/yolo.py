import torch
import pandas as pd
import os
from pathlib import Path

# Load YOLOv5 model (change 'yolov5s' to 'yolov5m', 'yolov5l', or 'yolov5x' for larger models)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Specify the directory containing images
image_folder = 'C:/Users/Abdulaziz/Desktop/10 Academy/Kara_Solutions/photos'  # Change this to your image folder path
output_csv = 'C:/Users/Abdulaziz/Desktop/10 Academy/Kara_Solutions/data/detections.csv'          # Output CSV file name

# Create a list to hold detection results
results_list = []

# Create output folder if it doesn't exist
output_folder = 'C:/Users/Abdulaziz/Desktop/10 Academy/Kara_Solutions/Detection_results'
Path(output_folder).mkdir(parents=True, exist_ok=True)

# Iterate through all images in the folder
for image_name in os.listdir(image_folder):
    if image_name.endswith(('.png', '.jpg', '.jpeg')):  # Check for image file types
        image_path = os.path.join(image_folder, image_name)
        
        # Perform detection
        results = model(image_path)

        # Process detection results
        detections = results.xyxy[0]  # Get detections for the first image

        # Extract relevant data: bounding box coordinates, confidence scores, and class labels
        for *box, conf, cls in detections:
            x1, y1, x2, y2 = map(int, box)  # Convert coordinates to integers
            confidence = conf.item()         # Get confidence score
            class_id = int(cls.item())       # Get class label
            
            # Append data to results list
            results_list.append({
                'Image': image_name,
                'Class': model.names[class_id],
                'Confidence': confidence,
                'X1': x1,
                'Y1': y1,
                'X2': x2,
                'Y2': y2
            })

        # Save results (with bounding boxes) to output folder as images
        results.save(output_folder)  # Saves detections to output folder

# Convert results list to DataFrame and save to CSV
results_df = pd.DataFrame(results_list)
results_df.to_csv(output_csv, index=False)

print(f"Detection results saved to {output_csv}")
